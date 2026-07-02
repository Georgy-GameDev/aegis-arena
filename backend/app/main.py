from fastapi import FastAPI

from app.api import auth, health, rooms, leaderboard
from app.db.session import engine
from app.db.models import Base


def create_app() -> FastAPI:
    app = FastAPI(
        title="Aegis Arena API",
        description="Secure multiplayer game backend prototype for GameDevSecOps portfolio.",
        version="0.1.0",
    )

    @app.on_event("startup")
    def on_startup() -> None:
        # For MVP only. In production, use Alembic migrations.
        Base.metadata.create_all(bind=engine)

    app.include_router(health.router, tags=["health"])
    app.include_router(auth.router, prefix="/auth", tags=["auth"])
    app.include_router(rooms.router, prefix="/rooms", tags=["rooms"])
    app.include_router(leaderboard.router, prefix="/leaderboard", tags=["leaderboard"])

    return app


app = create_app()
