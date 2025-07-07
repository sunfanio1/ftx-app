SERVICE_DIR := src
TXT_BOLD := \e[1m
TXT_MAGENTA := \e[35m
TXT_RESET := \e[0m

setup:
	@uv sync

lint:
	@printf "${TXT_BOLD}${TXT_MAGENTA}=========================== RUFF ==============================${TXT_RESET}\n"
	@uv run ruff check --fix --show-fixes --exit-non-zero-on-fix .
	@printf "${TXT_BOLD}${TXT_MAGENTA}=========================== MYPY ==============================${TXT_RESET}\n"
	@uv run mypy $(SERVICE_DIR)/

start:
	@uv run $(SERVICE_DIR)/api_app.py