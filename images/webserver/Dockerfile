FROM python:2.7-slim
MAINTAINER  lomadi <lomadi@mac.com>


RUN apt-get update
RUN apt-get -qq update
RUN apt-get install -my curl wget gnupg
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get install -y nodejs npm
RUN pip install --upgrade pip

COPY . /requirements
WORKDIR /requirements

# install requirements
RUN pip install -r requirements.txt
