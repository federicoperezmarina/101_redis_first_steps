FROM redis:alpine

COPY . /tmp/

USER root
RUN chmod -R 777 /tmp

RUN apk add python3 && \
    apk add py3-pip && \
    pip3 install redis