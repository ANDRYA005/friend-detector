from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


def main():

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Create the Updater and pass it your bot's token.
    updater = Updater("1617267363:AAEarpdWi-uRVcTV73Lqy9BPStRoIfwCIvI", use_context=True)

    # if len(sys.argv) == 1:
    #     print("deployment")
    #     PORT = int(os.environ.get('PORT', '8443'))

    #     # add handlers
    #     updater.start_webhook(listen="0.0.0.0",
    #                           port=PORT,
    #                           url_path="1130067780:AAGXw3FA4rk4Bddw5B5YCO4npBM1SO-9FdY")
    #     updater.bot.set_webhook("https://fin-rec-bot.herokuapp.com/" + "1130067780:AAGXw3FA4rk4Bddw5B5YCO4npBM1SO-9FdY")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dp.add_handler(start_handler)
    

    # if len(sys.argv) == 2:
    print("local dev")
    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__=='__main__':

    main()