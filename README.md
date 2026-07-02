# Aegis Arena

**Aegis Arena** is a secure multiplayer game prototype for a GameDevSecOps portfolio.

The goal is not just to build a small online game, but to demonstrate the full lifecycle of a production-oriented game system:

- game backend
- authentication
- multiplayer rooms
- leaderboard
- Docker-based local infrastructure
- basic security controls
- documented threat model
- future CI/CD and deployment pipeline

## Portfolio narrative

This project is designed for a GameDevSecOps portfolio:

> Secure development and deployment of online game systems.

It shows how game development, cybersecurity and DevOps intersect in online games and interactive systems.

## Tech stack

- FastAPI
- PostgreSQL
- Redis
- Docker Compose
- JWT authentication
- SQLAlchemy

## Current MVP

Version 0.1 includes:

- health endpoint
- user registration
- user login
- JWT access token
- create/list/join game rooms
- submit validated score
- leaderboard

## Run locally

1. Copy environment file:

```bash
cp .env.example .env
```

2. Start services:

```bash
docker compose up --build
```

3. Open API docs:

```text
http://localhost:8000/docs
```

## Basic API flow

1. `POST /auth/register`
2. `POST /auth/login`
3. Copy the returned `access_token`
4. Use `Authorize` in Swagger with:

```text
Bearer <access_token>
```

5. `POST /rooms`
6. `GET /rooms`
7. `POST /rooms/{room_id}/join`
8. `POST /leaderboard/submit`
9. `GET /leaderboard`

## Security design

See:

- `docs/threat_model.md`
- `docs/architecture.md`
- `docs/security_decisions.md`

## Roadmap

### Version 0.1 — Backend foundation

- [x] Docker Compose
- [x] FastAPI backend
- [x] PostgreSQL
- [x] Redis
- [x] Auth
- [x] Rooms
- [x] Leaderboard
- [x] Basic score validation

### Version 0.2 — Secure gameplay backend

- [ ] server-authoritative game state
- [ ] WebSocket game sessions
- [ ] anti-cheat event validation
- [ ] rate limiting
- [ ] structured logs
- [ ] automated tests

### Version 0.3 — DevOps pipeline

- [ ] GitHub Actions
- [ ] dependency scanning
- [ ] Docker image build
- [ ] staging deployment
- [ ] health checks
- [ ] rollback notes

### Version 0.4 — Game client

- [ ] Godot/Unity client
- [ ] login screen
- [ ] lobby screen
- [ ] simple multiplayer arena
- [ ] leaderboard UI
