#!/bin/sh

set -e

. .venv/bin/activate

echo "=== Перед тестами ==="
echo "ALLURE_RESULTS: $ALLURE_RESULTS"
echo "Текущая директория: $(pwd)"
ls -la "$ALLURE_RESULTS" || echo "Папка $ALLURE_RESULTS не существует"

pytest --browser "$BROWSER" \
      --log_level "$LOG_LEVEL" \
      --browser_ver "$BROWSER_VER" \
      --numprocesses="$XDIST" \
      --remote_start \
      --remote_url="$REMOTE_URL" \
      --alluredir="$ALLURE_RESULTS"

set +e
echo "=== После тестов ==="
ls -la "$ALLURE_RESULTS" || echo "Директория $ALLURE_RESULTS не существует"
find . -name "*.json" | xargs ls -la 2>/dev/null || echo "JSON-файлы не найдены"

exit 0