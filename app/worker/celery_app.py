import os
from dotenv import load_dotenv
from celery import Celery


load_dotenv(f".env.{os.getenv('ENVIRONMENT', 'development')}")

REDIS_URL = os.getenv("REDIS_URL")

print(REDIS_URL)

celery_app = Celery(
    "tasks",
    broker=REDIS_URL,
    backend=REDIS_URL,
    broker_connection_retry_on_startup = True
)

# celery_app = Celery(
#     "tasks",
#     broker="redis://127.0.0.1:6379/0",
#     backend="redis://127.0.0.1:6379/0",
#     broker_connection_retry_on_startup = True
# )

# celery_app.config_from_object('app.worker.celeryconfig')


celery_app.autodiscover_tasks(['app.utils.tasks'])
celery_app.conf.timezone = "UTC"
celery_app.conf.enable_utc = True

celery_app.conf.task_routes = {"tasks.add": {"queue": "reports"}}

celery_app.conf.update(
    worker_concurrency=4,  # 4 parallel tasks
    task_acks_late=True,    # Avoid duplicate processing
    result_expires=3600     # Auto-delete old results
)

'''
celery -A tasks worker --loglevel=INFO -E
'''