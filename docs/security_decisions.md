# Security Decisions

## 1. Passwords are hashed

Plain-text passwords are never stored.

## 2. JWT is used only for MVP auth

JWT is acceptable for the first prototype, but production design would require stricter token lifecycle management.

## 3. Server-side score validation is included from the beginning

Even the MVP avoids accepting arbitrary scores without checks.

## 4. Secrets are externalized

The repository contains `.env.example`, not real credentials.

## 5. Docker container runs as non-root user

The backend Dockerfile creates and uses a non-root application user.

## 6. Database migrations are not implemented yet

For MVP speed, tables are created on startup. This must be replaced with Alembic before production-like deployment.
