import gc
from asyncio import create_task, run
from timeit import default_timer
from typing import List


from app.core.celery import celery_app
from app.logging import get_logging
from app.schemas.reservation import EventXUser
from app.services.db import reservation_service


log = get_logging(__name__)


@celery_app.task(bind=True, max_retries=2, acks_late=True)
def init_reservation(
    self,
    user_id: int,
    event_id: int
) -> None:

    try:
        params_reservation = EventXUser(
            user_id=user_id,
            event_id=event_id
        )

        registry_ids = run(
            reservation_into(
                params = params_reservation
            )
        )

        log.info(f"DB Response: {registry_ids}")

    except Exception as exc:
        log.error(exc)
        if self.request.retries == self.max_retries:
            print("[ERROR]: Se alcanzó el número máximo de intentos fallidos")
        raise self.retry(exc=exc, countdown=10)


async def reservation_into(*, params : EventXUser) -> dict:
    params = params.dict()
    registry_ids = await reservation_service.create_reservation(payload=params)
    print(registry_ids)
    return registry_ids
