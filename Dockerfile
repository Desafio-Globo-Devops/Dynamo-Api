FROM python:3.7-alpine
LABEL maintainer='Dynamo-API'

WORKDIR /app

ADD requirements.txt /app/

RUN apk update \
    && apk add --no-cache --virtual .build-deps \
    build-base \
    gcc \
    musl-dev \
    postgresql-dev \
    libpq \
    && pip install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED=1 \
    FLASK_ENV=dev \
    TZ=America/Sao_Paulo

ADD ./ /app/

EXPOSE 8100

CMD ["flask", "run", "-h", "0.0.0.0", "-p", "8100"]