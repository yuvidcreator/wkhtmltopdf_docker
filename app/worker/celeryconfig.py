import os
from dotenv import load_dotenv


load_dotenv(f".env.{os.getenv('ENVIRONMENT', 'development')}")

REDIS_URL = os.getenv("REDIS_URL")


## Broker settings.
broker_url = REDIS_URL
# broker_url = 'redis://127.0.0.1:6379/0'

# List of modules to import when the Celery worker starts.
imports = ('app.utils.tasks',)

## Using the database to store task state and results.
result_backend = REDIS_URL
# result_backend = 'redis://127.0.0.1:6379/0'

task_annotations = {'tasks.add': {'rate_limit': '10/s'}}

task_queues = {
    'test-queue': {
        'exchange': 'test-queue',
    }
}
task_routes = {
    "process_report_task": "test-queue"
    # "app.utils.tasks.add":{"queue": "reports"},
    # "app.worker.celery_worker.long_task": "test-queue"
}
task_track_started = True

worker_concurrency = 1
worker_prefetch_multiplier = 3
worker_max_tasks_per_child = 10000




# celery_app.autodiscover_tasks(['app.utils.tasks'])
# celery_app.conf.timezone = "UTC"
# celery_app.conf.enable_utc = True

# celery_app.conf.task_routes = {"app.utils.tasks.add": {"queue": "reports"}}


# celery_app.conf.update(
#     worker_concurrency=4,  # 4 parallel tasks
#     task_acks_late=True,    # Avoid duplicate processing
#     result_expires=3600     # Auto-delete old results
# )
