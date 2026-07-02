from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.security import get_current_user
from app.db.models import Room, RoomPlayer, User
from app.db.session import get_db
from app.schemas.rooms import RoomCreateRequest, RoomResponse

router = APIRouter()


@router.post("", response_model=RoomResponse, status_code=status.HTTP_201_CREATED)
def create_room(
    payload: RoomCreateRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    room = Room(
        name=payload.name,
        owner_id=current_user.id,
        max_players=payload.max_players,
    )
    db.add(room)
    db.commit()
    db.refresh(room)

    db.add(RoomPlayer(room_id=room.id, user_id=current_user.id))
    db.commit()

    return room


@router.get("", response_model=list[RoomResponse])
def list_rooms(db: Session = Depends(get_db)):
    return db.query(Room).order_by(Room.created_at.desc()).limit(50).all()


@router.post("/{room_id}/join")
def join_room(
    room_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    room = db.query(Room).filter(Room.id == room_id).first()
    if not room:
        raise HTTPException(status_code=404, detail="Room not found.")

    player_count = db.query(RoomPlayer).filter(RoomPlayer.room_id == room_id).count()
    if player_count >= room.max_players:
        raise HTTPException(status_code=409, detail="Room is full.")

    existing = (
        db.query(RoomPlayer)
        .filter(RoomPlayer.room_id == room_id, RoomPlayer.user_id == current_user.id)
        .first()
    )
    if existing:
        return {"status": "already_joined", "room_id": room_id}

    db.add(RoomPlayer(room_id=room_id, user_id=current_user.id))
    db.commit()

    return {"status": "joined", "room_id": room_id}
