FROM python:3.9-slim-buster

ENV FLASK_APP=app:app
ENV FLASK_RUN_HOST=0.0.0.0
ENV PYTHONDONTWRITEBYTECODE=1
ENV REDIS_HOST=microservice-fun_redis_1
ENV REDIS_PORT=6379
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

WORKDIR /app

COPY ./app ./app

EXPOSE 5000
CMD ["flask", "run"]