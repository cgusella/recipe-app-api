FROM python:3.8-alpine3.15
ENV PYTHONUBUFFERED 1
COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql
RUN apk add --update --no-cache --virtual .tmp-build-deps\
        gcc libc-dev linux-headers postgresql-dev
RUN pip install -r requirements.txt
RUN apk del .tmp-build-deps
RUN apk add shadow
RUN mkdir /app
RUN groupadd -g 449600105 my_group
RUN useradd -u 449600105 -g 449600105 my_user
WORKDIR /app
COPY ./app /app
USER my_user