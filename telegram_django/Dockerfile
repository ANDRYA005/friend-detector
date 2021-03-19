FROM python:3

ENV PYTHONUNBUFFERED=1

WORKDIR /telegram_django
COPY requirements.txt /telegram_django/
RUN pip install -r requirements.txt
COPY . /telegram_django/

# EXPOSE 8020

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8020"]