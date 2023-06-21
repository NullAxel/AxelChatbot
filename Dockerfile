# syntax=docker/dockerfile:1

FROM python:3.8-slim-bullseye

WORKDIR /app

COPY requirements.txt requirements.txt
RUN apt update && apt install -y build-dep python3-lxml # For armhf
RUN apt install -y libxml2-dev libxslt-dev python-dev
RUN pip3 install -r requirements.txt

COPY chat.py chat.py
COPY webapp.py main.py
COPY responses.json responses.json
RUN mkdir templates
COPY templates/index.html templates/index.html
COPY templates/result.html templates/result.html

CMD ["python3", "main.py"]
