#!/bin/sh
set +e
. .venv/bin/activate

pytest --browser "$BROWSER" \
      --log_level "$LOG_LEVEL" \
      --browser_ver "$BROWSER_VER" \
      --numprocesses="$XDIST" \
      --remote_start \
      --remote_url="$REMOTE_URL" \
      --alluredir="$ALLURE_RESULTS"

chmod -R 777 "$ALLURE_RESULTS"

echo "=== После тестов ==="
ls -la "$ALLURE_RESULTS" || echo "Директория $ALLURE_RESULTS не существует"
find . -name "*.json" | xargs ls -la 2>/dev/null || echo "JSON-файлы не найдены"

exit 0