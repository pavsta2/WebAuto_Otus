#!/bin/sh
set -e

. .venv/bin/activate

ALLURE_RESULTS="/root/WebAuto_Otus/allure-results"
mkdir -p "$ALLURE_RESULTS"

chmod -R 777 "$ALLURE_RESULTS"

pytest tests/test_adm_login_page_elems.py --browser "$BROWSER" \
      --log_level "$LOG_LEVEL" \
      --browser_ver "$BROWSER_VER" \
      --numprocesses="$XDIST" \
      --remote_start \
      --remote_url="$REMOTE_URL" \
      --alluredir="$ALLURE_RESULTS"
