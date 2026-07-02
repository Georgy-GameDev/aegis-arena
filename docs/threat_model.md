# Threat Model

## System

Aegis Arena is a small online multiplayer game backend.

## Assets

- user accounts
- access tokens
- game rooms
- scores
- leaderboard integrity
- backend availability
- database integrity

## Threats

### 1. Fake score submission

A malicious player submits an impossible score.

**Risk:** leaderboard loses integrity.

**Current control:** score is checked against maximum plausible score per second.

**Future control:** server-authoritative game state.

---

### 2. Client-side trust

The game client claims that an action happened, but the server does not verify it.

**Risk:** cheating, item duplication, fake movement, impossible actions.

**Current control:** documented as a known MVP limitation.

**Future control:** validate movement, item state and timing on the server.

---

### 3. Credential attacks

An attacker guesses weak passwords or reuses leaked credentials.

**Risk:** account takeover.

**Current control:** password hashing and minimum password length.

**Future control:** rate limiting, login throttling, MFA option.

---

### 4. Token leakage

JWT is stolen from local storage or logs.

**Risk:** account takeover until token expiry.

**Current control:** token expiry.

**Future control:** short-lived access tokens, refresh token rotation, secure client storage.

---

### 5. API abuse

A malicious player sends too many requests.

**Risk:** degraded backend availability.

**Current control:** not implemented yet.

**Future control:** rate limiting, IP/user throttling, abuse logs.

---

### 6. Secrets exposure

Database passwords or JWT secret are committed to GitHub.

**Risk:** infrastructure compromise.

**Current control:** `.env.example` only; real `.env` is ignored.

**Future control:** GitHub secret scanning, CI checks, managed secrets.
