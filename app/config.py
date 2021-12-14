from enum import Enum

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    APP_TITLE: str
    APP_DESCRIPTION: str
    APP_VERSION: str
    RABBITMQ_USER: str = Field("user")
    RABBITMQ_PASSWORD: str = Field("bitnami")
    RABBITMQ_HOST: str = Field("localhost")
    RABBITMQ_PORT: str = Field("5672")
    DB_API: str = Field(...)
    ENVIRONMENT: str = Field(...)
    WORKER_ROUTER: str = Field(...)
    QUEUE_INTAKE: str = Field(...)


class StatusName(Enum):
    DOC_START_POSTRPROCESS: str = "Postprocessing started"
    DOC_START_PREPROCESS: str = "Preprocessing started"
    ELEMENT_START_PREPROCESS: str = "Preprocessing started"
    ELEMENT_END_PREPROCESS: str = "Preprocessing finished"


settings = Settings()
