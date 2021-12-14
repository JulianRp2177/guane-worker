from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app.config import settings
from app.core.celery import celery_app
from app.schemas.reservation import EventXUser, TaskResponse
from app.logging import get_logging


log = get_logging(__name__)

router = APIRouter()
WORKER_ENVIRONMENT = "-dev" if settings.ENVIRONMENT else ""


@router.post(
    "/",
    response_class=JSONResponse,
    response_model=str,
    status_code=200,
    responses={
        200: {"description": "Task was send"},
        404: {"description": "task not submitted"}
    },
)
async def generate_task(reservation: EventXUser):
    task = celery_app.send_task(
        settings.WORKER_ROUTER,
        args=[
            reservation.user_id,
            reservation.event_id,
        ],
        queue=settings.QUEUE_INTAKE,
    )
    if task:
        log.info(f"Task was send successfully {task.id}")
        response = TaskResponse(task_id=task.id)
        response = jsonable_encoder(response)
        return JSONResponse(status_code=200, content=response)
    else:
        log.error(f"An error occurred while submitting the task {task}")
        return JSONResponse(status_code=404, content={})
