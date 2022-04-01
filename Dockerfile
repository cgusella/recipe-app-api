FROM python:3.8-alpine3.15
ENV PYTHONUBUFFERED 1
COPY ./requirements.txt /requirements.txt
RUN apk add --no-cache --virtual .build-deps gcc musl-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del .build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user