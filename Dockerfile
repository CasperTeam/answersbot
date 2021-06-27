
FROM python:3.8.5-slim-buster

WORKDIR /app


ENV PIP_NO_CACHE_DIR 1

ENV LANG C.UTF-8


ENV DEBIAN_FRONTEND noninteractive


RUN sed -i.bak 's/us-west-2\.ec2\.//' /etc/apt/sources.list


COPY . .


RUN pip3 install --no-cache-dir -r requirements.txt


CMD ["python3", "-m", "bot"]
