# Aegis Arena

[![Backend Tests](https://github.com/Georgy-GameDev/aegis-arena/actions/workflows/backend-tests.yml/badge.svg)](https://github.com/Georgy-GameDev/aegis-arena/actions/workflows/backend-tests.yml)

**Aegis Arena** is a secure multiplayer game backend prototype for a GameDevSecOps portfolio.

The project demonstrates how game development, cybersecurity, and DevOps intersect in online game systems.

The goal is not just to build a small game backend, but to show the full lifecycle of a production-oriented online game system:

- backend architecture
- authentication
- multiplayer rooms
- leaderboard logic
- Docker-based local infrastructure
- server-side score validation
- automated tests
- GitHub Actions CI workflow
- documented security reasoning

---

## Portfolio Narrative

Aegis Arena is built around the idea of **GameDevSecOps**:

> secure development, deployment, and protection of online game systems.

The project focuses on a common problem in multiplayer games: the backend should not blindly trust the game client.

For example, a player should not be able to submit an impossible score and appear on the leaderboard. Even in this early MVP, the backend includes basic server-side validation to reject unrealistic leaderboard submissions.

---

## Current Status

The current version includes a working backend MVP:

- user registration
- user login
- JWT-based authentication
- multiplayer room creation
- room listing
- leaderboard submission
- basic anti-cheat score validation
- PostgreSQL persistence
- Redis service included for future lobby/session logic
- Docker Compose local environment
- Pytest-based unit tests
- GitHub Actions workflow for backend tests

---

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- Redis
- Docker
- Docker Compose
- SQLAlchemy
- JWT authentication
- Pytest
- GitHub Actions

---

## Architecture

Current MVP architecture:

```text
Client / Swagger UI
        |
        v
FastAPI Backend
        |
        |---- PostgreSQL
        |       - users
        |       - rooms
        |       - scores
        |
        |---- Redis
                - reserved for future lobby/session logic
```

Current API flow:

```text
register user
      |
authorize with JWT token
      |
create room
      |
submit score
      |
validate score on server
      |
store accepted result
      |
show leaderboard
```

---

## Security Logic

The MVP includes basic anti-cheat validation for leaderboard submissions.

The backend checks whether the submitted score is plausible based on match duration.

Example:

```json
{
  "room_id": 1,
  "score": 99999,
  "match_duration_seconds": 10
}
```

This request is rejected because the score is impossible for the given match duration.

Expected response:

```json
{
  "detail": "Score rejected: score_exceeds_possible_rate"
}
```

This is an early security control. In later versions, this will be replaced with a stronger **server-authoritative game session model**, where the client sends actions and the server calculates the final result.

---

## Project Structure

```text
aegis-arena/
  backend/
    app/
      api/
      core/
      db/
      schemas/
      services/
      main.py
    tests/
      test_score_validation.py
    Dockerfile
    requirements.txt

  docs/
    architecture.md
    threat_model.md
    security_decisions.md
    portfolio_notes.md

  .github/
    workflows/
      backend-tests.yml

  docker-compose.yml
  .env.example
  .gitignore
  README.md
```

---

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Georgy-GameDev/aegis-arena.git
cd aegis-arena
```

### 2. Create local environment file

```bash
cp .env.example .env
```

On Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

### 3. Start the project

```bash
docker compose up
```

Or rebuild and start:

```bash
docker compose up --build
```

### 4. Open API documentation

```text
http://localhost:8000/docs
```

---

## API Flow

### 1. Register user

```text
POST /auth/register
```

Example request:

```json
{
  "username": "testuser",
  "password": "testpassword123"
}
```

Expected response:

```json
{
  "access_token": "...",
  "token_type": "bearer"
}
```

### 2. Authorize

In Swagger UI, click **Authorize** and paste the access token.

### 3. Create room

```text
POST /rooms
```

Example request:

```json
{
  "name": "First Arena",
  "max_players": 2
}
```

### 4. List rooms

```text
GET /rooms
```

### 5. Submit score

```text
POST /leaderboard/submit
```

Example request:

```json
{
  "room_id": 1,
  "score": 100,
  "match_duration_seconds": 30
}
```

### 6. Get leaderboard

```text
GET /leaderboard
```

---

## Run Tests

Run backend tests inside the Docker container:

```bash
docker compose exec backend pytest -p no:cacheprovider
```

Expected result:

```text
3 passed
```

The current tests check:

- valid score is accepted
- impossible score is rejected
- negative score is rejected

---

## GitHub Actions

The repository includes a GitHub Actions workflow:

```text
.github/workflows/backend-tests.yml
```

The workflow automatically runs backend tests on:

- push to `main`
- pull requests

This provides a basic CI layer for the project.

---

## Documentation

Additional documentation is stored in the `docs/` folder:

- `architecture.md` — current system architecture
- `threat_model.md` — security risks and controls
- `security_decisions.md` — key security-related design decisions
- `portfolio_notes.md` — how to present the project in a portfolio

---

## Roadmap

### Version 0.1 — Backend MVP

- [x] FastAPI backend
- [x] PostgreSQL database
- [x] Redis service
- [x] Docker Compose setup
- [x] user registration
- [x] user login
- [x] JWT authentication
- [x] room creation
- [x] room listing
- [x] leaderboard submission
- [x] basic score validation
- [x] unit tests
- [x] GitHub Actions workflow

### Version 0.2 — Secure Game Session

- [ ] WebSocket connection
- [ ] real-time game session prototype
- [ ] server-authoritative game state
- [ ] action-based scoring
- [ ] suspicious event logging
- [ ] stronger anti-cheat validation

### Version 0.3 — DevOps Layer

- [ ] deployment environment
- [ ] health checks
- [ ] structured logging
- [ ] monitoring basics
- [ ] dependency scanning
- [ ] Docker hardening improvements

### Version 0.4 — Game Client

- [ ] simple Godot or Unity client
- [ ] login screen
- [ ] room list screen
- [ ] simple arena gameplay
- [ ] leaderboard UI

---

## Current Portfolio Value

This project currently demonstrates:

- backend development for online games
- authentication and access control
- Docker-based local infrastructure
- basic database-backed game state
- leaderboard integrity concerns
- server-side validation against obvious cheating
- automated testing
- CI workflow with GitHub Actions
- security-aware engineering documentation

---

## Status

Current stage:

```text
Working backend MVP with tests and CI
```

Next major step:

```text
WebSocket-based server-authoritative game session
```