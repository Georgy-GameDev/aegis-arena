from datetime import datetime

from pydantic import BaseModel, Field


class SubmitScoreRequest(BaseModel):
    room_id: int
    score: int = Field(ge=0, le=100000)
    match_duration_seconds: int = Field(ge=10, le=3600)


class ScoreResponse(BaseModel):
    username: str
    score: int
    room_id: int
    validation_status: str
    created_at: datetime
