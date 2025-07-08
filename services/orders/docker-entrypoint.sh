#!/bin/sh

set -e

## Apply migrations
#poetry run alembic --name calls upgrade head
#poetry run alembic --name chats upgrade head
#poetry run alembic --name profiles upgrade head

# Start application
uv run python -m src.api_app