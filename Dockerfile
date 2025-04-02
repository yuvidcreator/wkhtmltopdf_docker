FROM python:3.11

WORKDIR /
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# CMD ["celery", "-A", "app.worker.celery_app", "worker", "--loglevel=INFO", "-E"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
