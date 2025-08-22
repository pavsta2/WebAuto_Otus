#!/bin/sh

set -e

. .venv/bin/activate


pytest --browser "$BROWSER" \
      --log_level "$LOG_LEVEL" \
      --browser_ver "$BROWSER_VER" \
      --numprocesses="$XDIST" \
      --remote_start \
      --remote_url="$REMOTE_URL" \
      --alluredir="$ALLURE_RESULTS"