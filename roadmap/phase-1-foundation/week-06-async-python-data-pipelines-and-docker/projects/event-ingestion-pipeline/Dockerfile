FROM python:3.12-slim

WORKDIR /app

COPY app ./app
COPY data ./data

RUN mkdir -p /app/output

CMD ["python", "-m", "app.main"]
