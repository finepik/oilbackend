FROM python:3.11-slim-buster  

ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip \ 
    && apt-get update; \
    apt-get install -y \
    libpq-dev \
    gcc \
    musl-dev \
    g++;

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY Shop .
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
