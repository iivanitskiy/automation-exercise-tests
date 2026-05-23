#!/usr/bin/env bash
# Запуск тестов с Allure-результатами (Linux/macOS)
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

RESULTS_DIR="${ALLURE_RESULTS_DIR:-reports/allure-results}"
MARKERS="${1:-}"

PYTEST="${ROOT}/.venv/bin/pytest"
if [[ ! -x "$PYTEST" ]]; then
  PYTEST="pytest"
fi

ARGS=(tests "--alluredir=${RESULTS_DIR}" "--clean-alluredir" "--browser" "chromium" -v)
if [[ -n "$MARKERS" ]]; then
  ARGS+=(-m "$MARKERS")
fi

echo ">> $PYTEST ${ARGS[*]}"
"$PYTEST" "${ARGS[@]}"
echo "Allure results: ${RESULTS_DIR}"
echo "Generate: ./scripts/allure_report.sh"
