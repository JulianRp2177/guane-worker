from celery import Celery

from app.config import settings

CELERY_BROKER = f"amqp://{settings.RABBITMQ_USER}:{settings.RABBITMQ_PASSWORD}@{settings.RABBITMQ_HOST}:{settings.RABBITMQ_PORT}//"

celery_config = {
    "broker_url": CELERY_BROKER,
    "result_expires": 7200,
    "worker_prefetch_multiplier": 1,
}

celery_app = Celery("worker", config_source=celery_config)

celery_app.conf.task_routes = {
    settings.WORKER_ROUTER: {"queue": settings.QUEUE_INTAKE}
}

celery_app.conf.update(
    task_track_started=True, task_serializer="pickle", accept_content=["pickle", "json"]
)
