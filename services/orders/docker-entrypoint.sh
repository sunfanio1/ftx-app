#!/bin/sh

set -e

# Apply migrations
uv run alembic upgrade head

# Start application
uv run python -m src.api_app