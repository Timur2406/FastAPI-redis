FROM python:3.11.8-slim

EXPOSE 5000
WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY src/ .

CMD ["docker/backend.sh"]