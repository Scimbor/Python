# syntax=docker/dockerfile:1

FROM python:3.10.1-slim-buster

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt; \
    pip3 install python-dotenv; \
    pip3 install requests

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]