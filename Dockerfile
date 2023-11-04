FROM python:3.11-slim-buster  
#Берем образ берем слим бустер (очень облегченный debian). Обычно юзают образ на базе alpine, но в нем не работают pandas и numpy

WORKDIR /usr/src/app 
#создаем внутри контейнера директорию

ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONUNBUFFERED 1

#ставим проги чтобы установить библиотеки
RUN pip install --upgrade pip \ 
    && apt-get update; \
    apt-get install -y \
    libpq-dev \
    gcc \
    musl-dev \
    g++;

#устанавливаем библиотеки для проекта
COPY ./requirements.txt .
RUN pip install -r requirements.txt 

#копируем с компа с директории в которой докерфайл в созданную выше директорию /usr/src/app
COPY . . 
#переходим в директорию в которой manage.py чтобы скрипты внутри контейнера выполнять не меняя папку
WORKDIR /usr/src/app/Shop 