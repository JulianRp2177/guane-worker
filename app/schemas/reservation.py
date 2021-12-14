from pydantic import BaseModel, Field

class EventXUser(BaseModel):
    user_id: int
    event_id: int

class TaskResponse(BaseModel):
    task_id: str