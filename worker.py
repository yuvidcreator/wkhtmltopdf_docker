import os
from celery import Celery


from dotenv import load_dotenv


load_dotenv(f".env.{os.getenv('ENVIRONMENT', 'development')}")

REDIS_URL = os.getenv("REDIS_URL")

# Celery Configuration
celery_app = Celery(
    "tasks",
    broker=REDIS_URL,
    backend=REDIS_URL,
    broker_connection_retry_on_startup = True
)

celery_app.autodiscover_tasks(['app.utils.tasks'])
celery_app.conf.timezone = "UTC"
celery_app.conf.enable_utc = True

celery_app.conf.task_routes = {"app.utils.tasks.add": {"queue": "reports"}}


celery_app.conf.update(
    worker_concurrency=4,  # 4 parallel tasks
    task_acks_late=True,    # Avoid duplicate processing
    result_expires=3600     # Auto-delete old results
)
