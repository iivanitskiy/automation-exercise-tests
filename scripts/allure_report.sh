#!/usr/bin/env bash
# Генерация и открытие Allure HTML-отчёта
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

RESULTS_DIR="${ALLURE_RESULTS_DIR:-reports/allure-results}"
REPORT_DIR="${ALLURE_REPORT_DIR:-reports/allure-report}"
CONFIG_DIR="${ROOT}/config/allure"
SERVE="${SERVE:-false}"

if ! command -v allure >/dev/null 2>&1; then
  echo "Allure CLI не найден. Установите: https://allurereport.org/docs/install/"
  exit 1
fi

if [[ ! -d "$RESULTS_DIR" ]]; then
  echo "Нет результатов: $RESULTS_DIR"
  exit 1
fi

allure generate "$RESULTS_DIR" -o "$REPORT_DIR" --clean --config "$CONFIG_DIR"

if [[ "$SERVE" == "true" ]]; then
  allure open "$REPORT_DIR"
else
  echo "Report: ${REPORT_DIR}/index.html"
  if command -v xdg-open >/dev/null; then
    xdg-open "${REPORT_DIR}/index.html"
  elif command -v open >/dev/null; then
    open "${REPORT_DIR}/index.html"
  fi
fi
