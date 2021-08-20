FROM python:3.9-slim-buster


ENV PYTHONDONTWRITEBYTECODE=1
ENV REDIS_HOST=cache
ENV REDIS_PORT=6379

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

WORKDIR /app

COPY ./app ./app

EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", ":5000", "app:app"]
