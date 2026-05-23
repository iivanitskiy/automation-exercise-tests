from typing import Any

from playwright.sync_api import APIResponse


def assert_status(response: APIResponse, expected: int) -> None:
    assert response.status == expected, (
        f"Expected HTTP {expected}, got {response.status}. Body: {response.text()}"
    )


def assert_response_code(body: dict[str, Any], expected: int) -> None:
    actual = body.get("responseCode")
    assert actual == expected, f"Expected responseCode {expected}, got {actual}. Body: {body}"


def assert_message(body: dict[str, Any], expected: str) -> None:
    message = body.get("message", "")
    assert expected in message, f"Expected message containing '{expected}', got '{message}'"
