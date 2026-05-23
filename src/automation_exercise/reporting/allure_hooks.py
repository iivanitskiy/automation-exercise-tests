import json
import re
from typing import Any

import allure
from playwright.sync_api import Page

_TC_PATTERN = re.compile(r"test_(?:case|api)_(\d+)", re.IGNORECASE)


def apply_test_labels(item) -> None:
    
    path = str(item.fspath).replace("\\", "/")

    if "/tests/api/" in path:
        allure.dynamic.parent_suite("API")
        allure.dynamic.epic("Automation Exercise API")
        allure.dynamic.feature("REST API")
    elif "/tests/ui/" in path:
        allure.dynamic.parent_suite("UI")
        allure.dynamic.epic("Automation Exercise UI")
        allure.dynamic.feature("Web UI")

    if item.cls:
        allure.dynamic.suite(item.cls.__name__)

    allure.dynamic.story(item.name)

    match = _TC_PATTERN.search(item.name)
    if match:
        tc_id = match.group(1).zfill(2)
        prefix = "API" if "/tests/api/" in path else "TC"
        allure.dynamic.label("testCase", f"{prefix}-{tc_id}")
        allure.dynamic.title(f"{prefix}-{tc_id}: {item.name}")

    for marker in item.iter_markers():
        allure.dynamic.tag(marker.name)
        if marker.name == "smoke":
            allure.dynamic.severity(allure.severity_level.CRITICAL)
        elif marker.name == "regression":
            allure.dynamic.severity(allure.severity_level.NORMAL)


def attach_playwright_artifacts(page: Page | None) -> None:
    if page is None or page.is_closed():
        return

    try:
        screenshot = page.screenshot(full_page=True)
        allure.attach(
            screenshot,
            name="screenshot",
            attachment_type=allure.attachment_type.PNG,
            extension="png",
        )
    except Exception as exc:
        allure.attach(
            str(exc),
            name="screenshot-error",
            attachment_type=allure.attachment_type.TEXT,
        )

    try:
        allure.attach(
            page.url,
            name="page-url",
            attachment_type=allure.attachment_type.URI_LIST,
        )
    except Exception:
        pass

    try:
        html = page.content()
        if len(html) > 500_000:
            html = html[:500_000] + "\n<!-- truncated -->"
        allure.attach(
            html,
            name="page-source",
            attachment_type=allure.attachment_type.HTML,
            extension="html",
        )
    except Exception:
        pass


def attach_api_response(response: Any, label: str = "last-api-response") -> None:
    if response is None:
        return

    try:
        body = response.json()
        payload = json.dumps(body, indent=2, ensure_ascii=False)
        attachment_type = allure.attachment_type.JSON
    except Exception:
        payload = response.text()
        attachment_type = allure.attachment_type.TEXT

    allure.attach(
        f"Status: {response.status}\n\n{payload}",
        name=label,
        attachment_type=attachment_type,
        extension="json" if attachment_type == allure.attachment_type.JSON else "txt",
    )
