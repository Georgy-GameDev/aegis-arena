from datetime import datetime

from pydantic import BaseModel, Field


class RoomCreateRequest(BaseModel):
    name: str = Field(min_length=3, max_length=80)
    max_players: int = Field(default=2, ge=2, le=8)


class RoomResponse(BaseModel):
    id: int
    name: str
    owner_id: int
    status: str
    max_players: int
    created_at: datetime

    class Config:
        from_attributes = True
