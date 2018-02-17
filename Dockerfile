FROM python:3.6


RUN pip install aiodocker pytest pytest-asyncio

ENV BASE_DIR=/app
WORKDIR $BASE_DIR

COPY . $BASE_DIR
