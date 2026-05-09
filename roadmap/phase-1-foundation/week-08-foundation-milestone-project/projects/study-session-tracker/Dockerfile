FROM python:3.14-slim

WORKDIR /app

COPY sql ./sql
COPY src ./src
COPY data ./data

ENV HOST=0.0.0.0
ENV PORT=8000
ENV APP_DB_PATH=/app/data/study_tracker.db

EXPOSE 8000

CMD ["python", "src/server.py"]
