#!/bin/sh
set +e

. .venv/bin/activate

ALLURE_RESULTS="${ALLURE_RESULTS:-/root/WebAuto_Otus/allure-results}"
mkdir -p $ALLURE_RESULTS

echo "=== Пишем результаты в: $ALLURE_RESULTS ==="

pytest --browser "$BROWSER" \
      --log_level "$LOG_LEVEL" \
      --browser_ver "$BROWSER_VER" \
      --numprocesses="$XDIST" \
      --remote_start \
      --remote_url="$REMOTE_URL" \
      --alluredir=$ALLURE_RESULTS

chmod -R 777 $ALLURE_RESULTS

echo "=== Содержимое $ALLURE_RESULTS ==="
ls -la $ALLURE_RESULTS

echo "=== Проверка первого JSON-файла ==="
head -n 20 "$(find "$ALLURE_RESULTS" -name "*.json" -type f | head -1)"
