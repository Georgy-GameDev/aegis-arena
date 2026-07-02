from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.security import get_current_user
from app.db.models import Room, Score, User
from app.db.session import get_db
from app.schemas.leaderboard import ScoreResponse, SubmitScoreRequest
from app.services.score_validation import validate_score

router = APIRouter()


@router.post("/submit", status_code=status.HTTP_201_CREATED)
def submit_score(
    payload: SubmitScoreRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    room = db.query(Room).filter(Room.id == payload.room_id).first()
    if not room:
        raise HTTPException(status_code=404, detail="Room not found.")

    is_valid, status_reason = validate_score(
        score=payload.score,
        match_duration_seconds=payload.match_duration_seconds,
    )

    if not is_valid:
        # In a real system, rejected submissions should also be logged for abuse detection.
        raise HTTPException(status_code=400, detail=f"Score rejected: {status_reason}")

    score = Score(
        user_id=current_user.id,
        room_id=payload.room_id,
        score=payload.score,
        match_duration_seconds=payload.match_duration_seconds,
        validation_status=status_reason,
    )
    db.add(score)
    db.commit()

    return {"status": "accepted", "score": payload.score}


@router.get("", response_model=list[ScoreResponse])
def get_leaderboard(db: Session = Depends(get_db)):
    rows = (
        db.query(Score, User)
        .join(User, User.id == Score.user_id)
        .order_by(Score.score.desc(), Score.created_at.asc())
        .limit(20)
        .all()
    )

    return [
        ScoreResponse(
            username=user.username,
            score=score.score,
            room_id=score.room_id,
            validation_status=score.validation_status,
            created_at=score.created_at,
        )
        for score, user in rows
    ]
