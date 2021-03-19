import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
from argparse import ArgumentParser
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
if TELEGRAM_TOKEN is None:
    logging.info("TELEGRAM_TOKEN not in environment.")
    exit()


def start(update, context):
    user = update.message.from_user

    update.message.reply_text(
        text=f"Hey {user.first_name}! Enter the person you would like to stage for classification."
    )


def set_staged_name(update, context):

    if context.args:
        name = context.args[0]
    else:
        update.message.reply_text(
            text="No name was supplied."
        )

    logger.info("Setting %s as staged name", name)

    response = post_staged_name_to_django(name)

    if response.ok:
        update.message.reply_text(
            text=f"The name {name} has been staged."
        )
    else:
        update.message.reply_text(
            text="There was an error staging the name."
        )


def get_staged_name(update, context):

    logger.info("Getting staged name")
    response = get_staged_name_from_django()

    if response.ok:
        update.message.reply_text(
            text=f"The current staged name is: {response.json()['name']}."
        )
    else:
        update.message.reply_text(
            text="There was an error getting the staged name."
        )


def post_staged_name_to_django(name):
    response = requests.post(set_staged_endpoint, data = {'name': name})
    # logger.info(f"Data returned from post request: {response.text}")
    return response


def get_staged_name_from_django():
    response = requests.get(get_staged_endpoint)
    # logger.info(f"Data returned from get request: {response.text}")
    return response


def main(dev_or_prod):

    # Create the Updater and pass it your bot's token.
    updater = Updater(TELEGRAM_TOKEN, use_context=True)

    if dev_or_prod == "prod":
        print("deployment")
        PORT = int(os.environ.get('PORT', '8443'))

        # add handlers
        updater.start_webhook(listen="0.0.0.0",
                              port=PORT,
                              url_path=TELEGRAM_TOKEN)

        updater.bot.set_webhook("https://quiet-lowlands-14424.herokuapp.com/" + TELEGRAM_TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('stage', set_staged_name, pass_args=True))
    dp.add_handler(CommandHandler('get_staged', get_staged_name))
    

    if dev_or_prod == "dev":
        print("local dev")
        # Start the Bot
        updater.start_polling()

    updater.idle()


if __name__=='__main__':

    parser = ArgumentParser(
        description="Uses telegram bot to post names to django endpoint."
    )

    parser.add_argument(
        "--set_staged_endpoint",
        help="The api endpoint for setting a name as staged.",
        type=str,
        default='http://localhost:8000/telegram_hook/set_staged/',
    )
    parser.add_argument(
        "--get_staged_endpoint",
        help="The api endpoint for getting the staged name.",
        type=str,
        default='http://localhost:8000/telegram_hook/get_staged/',
    )
    parser.add_argument(
        "--dev_or_prod",
        help="Development of production.",
        type=str,
        default='dev',
    )

    args = parser.parse_args()

    set_staged_endpoint = args.set_staged_endpoint
    get_staged_endpoint = args.get_staged_endpoint

    logger.info(set_staged_endpoint)
    logger.info(get_staged_endpoint)

    main(args.dev_or_prod)