# syntax=docker/dockerfile:1

FROM python:3.8-slim-bullseye

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY chat.py chat.py
COPY webapp.py main.py
COPY config.json config.json

CMD ["python3", "main.py"]