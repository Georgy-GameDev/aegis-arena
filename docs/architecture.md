# Aegis Arena Architecture

## Current architecture

```text
Game Client / Swagger
        |
        v
FastAPI Backend
        |
        |---- PostgreSQL: users, rooms, scores
        |
        |---- Redis: future lobby/session cache
```

## Design principle

The server should become authoritative over game state.

In insecure game systems, the client often tells the server what happened:

```text
client -> server: I scored 999999 points
```

In a safer design, the client sends actions, and the server validates consequences:

```text
client -> server: I moved to X,Y
client -> server: I collected item #123
server -> server: validate distance, timing, item state
server -> database: store verified score
```

## MVP limitation

The current MVP still accepts a submitted score, but validates whether it is plausible based on match duration.

This is not final security. It is an intentional first step that will be replaced with a server-authoritative game loop in version 0.2.
