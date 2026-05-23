import os
import platform
import shutil
import sys
from pathlib import Path

import allure
import pytest
from playwright.sync_api import APIRequestContext, Playwright

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
if str(ROOT / "src") not in sys.path:
    sys.path.insert(0, str(ROOT / "src"))

from automation_exercise.reporting.allure_hooks import (
    apply_test_labels,
    attach_playwright_artifacts,
)
from config.settings import get_settings

ALLURE_RESULTS_DIR = Path(os.getenv("ALLURE_RESULTS_DIR", ROOT / "reports" / "allure-results"))
ALLURE_CONFIG_DIR = ROOT / "config" / "allure"


def pytest_configure(config: pytest.Config) -> None:
    alluredir = config.getoption("--alluredir", default=None)
    if alluredir:
        results_dir = Path(alluredir)
        results_dir.mkdir(parents=True, exist_ok=True)
        _write_environment_properties(results_dir)
        _copy_allure_metadata(results_dir)


def pytest_sessionfinish(session: pytest.Session, exitstatus: int) -> None:
    alluredir = session.config.getoption("--alluredir", default=None)
    if alluredir:
        _copy_allure_metadata(Path(alluredir))


def _copy_allure_metadata(results_dir: Path) -> None:
    for filename in ("categories.json", "executor.json"):
        source = ALLURE_CONFIG_DIR / filename
        if source.exists():
            shutil.copy(source, results_dir / filename)


def pytest_runtest_setup(item: pytest.Item) -> None:
    apply_test_labels(item)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item: pytest.Item, call: pytest.CallInfo) -> None:
    outcome = yield
    report = outcome.get_result()

    if report.when != "call" or not report.failed:
        return

    page = item.funcargs.get("page")
    if page is not None:
        with allure.step("Attach UI artifacts on failure"):
            attach_playwright_artifacts(page)

def _write_environment_properties(results_dir: Path) -> None:
    settings = get_settings()
    lines = [
        f"BASE_URL={settings.base_url}",
        f"API_BASE_URL={settings.api_base_url}",
        f"HEADLESS={settings.headless}",
        f"Python={platform.python_version()}",
        f"Platform={platform.platform()}",
        f"Project=automation-exercise-test",
    ]
    (results_dir / "environment.properties").write_text("\n".join(lines) + "\n", encoding="utf-8")


@pytest.fixture(scope="session")
def settings():
    return get_settings()


@pytest.fixture(scope="session")
def browser_context_args(settings):
    return {
        "base_url": settings.base_url,
        "ignore_https_errors": True,
    }


@pytest.fixture(scope="session")
def browser_type_launch_args(settings):
    return {
        "headless": settings.headless,
        "slow_mo": settings.slow_mo,
    }


@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright, settings) -> APIRequestContext:
    context = playwright.request.new_context(
        base_url=settings.api_base_url,
        extra_http_headers={"Accept": "application/json"},
    )
    yield context
    context.dispose()
