
from logging import getLogger

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.debugger import initialize_fastapi_server_debugger_if_needed
from app.api.api import api_router

log = getLogger(__name__)


def create_application() -> FastAPI:
    initialize_fastapi_server_debugger_if_needed()
    application = FastAPI(title=settings.APP_TITLE, description=settings.APP_DESCRIPTION, version=settings.APP_VERSION)
    application.include_router(api_router, prefix="/api")
    return application


app = create_application()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():

    log.info("Starting up...")


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")