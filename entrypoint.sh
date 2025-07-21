#!/bin/sh

set -e

. .venv/bin/activate

BROWSER=""
LOG_LEVEL=""
BROWSER_VER=""
XDIST_NUM=""
REMOTE_URL=""

while [ $# -gt 0 ]; do
  case $1 in
    --browser)
      BROWSER=$2
      shift
      shift
      ;;
    --log_level)
      LOG_LEVEL=$2
      shift
      shift
      ;;
    --browser_ver)
      BROWSER_VER=$2
      shift
      shift
      ;;
    --xdist)
      XDIST_NUM=$2
      shift
      shift
      ;;
    --remote_url)
      REMOTE_URL=$2
      shift
      shift
      ;;
  esac
done

pytest --browser "$BROWSER" --log_level "$LOG_LEVEL" --browser_ver "$BROWSER_VER" -n="$XDIST_NUM" --remote_start --remote_url="$REMOTE_URL"
