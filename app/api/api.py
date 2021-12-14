from fastapi import APIRouter

from app.api.endpoints import reservation

api_router = APIRouter()

api_router.include_router(reservation.router, prefix="/reservation", tags=["Reservation"])