FROM python:3

ENV PYTHONUNBUFFERED=1

WORKDIR /telegram_bot
COPY requirements.txt /telegram_bot/
RUN pip install -r requirements.txt
COPY . /telegram_bot/

# CMD ["python", "name_setter_bot.py", "--set_staged_endpoint", "http://0.0.0.0:8020/telegram_hook/set_staged/", "--get_staged_endpoint", "http://0.0.0.0:8020/telegram_hook/get_staged/"]
