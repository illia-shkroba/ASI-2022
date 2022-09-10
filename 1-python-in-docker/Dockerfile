FROM python:3.10.7-bullseye

WORKDIR /usr/local/lib/data-processor

COPY lib/data-processor/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY lib/data-processor/setup.py .
COPY lib/data-processor/src src
RUN pip install --no-cache-dir -e .
