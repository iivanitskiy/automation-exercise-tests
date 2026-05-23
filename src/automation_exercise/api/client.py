from typing import Any

import allure
from playwright.sync_api import APIRequestContext, APIResponse

from automation_exercise.reporting.allure_hooks import attach_api_response
from config.settings import get_settings


class ApiClient:

    def __init__(self, request_context: APIRequestContext) -> None:
        self._request = request_context
        self._settings = get_settings()

    @property
    def base_url(self) -> str:
        return self._settings.api_base_url

    def get(self, path: str, **kwargs: Any) -> APIResponse:
        return self._execute("GET", path, self._request.get, **kwargs)

    def post(self, path: str, **kwargs: Any) -> APIResponse:
        return self._execute("POST", path, self._request.post, **kwargs)

    def put(self, path: str, **kwargs: Any) -> APIResponse:
        return self._execute("PUT", path, self._request.put, **kwargs)

    def delete(self, path: str, **kwargs: Any) -> APIResponse:
        return self._execute("DELETE", path, self._request.delete, **kwargs)

    def _execute(self, method: str, path: str, handler: Any, **kwargs: Any) -> APIResponse:
        url = f"{self.base_url}{path}"
        with allure.step(f"{method} {path}"):
            allure.attach(
                _format_request_details(method, url, kwargs),
                name="request",
                attachment_type=allure.attachment_type.TEXT,
            )
            response = handler(url, **kwargs)
            attach_api_response(response, label="response")
            return response

    @staticmethod
    def parse_json(response: APIResponse) -> dict[str, Any]:
        return response.json()


def _format_request_details(method: str, url: str, kwargs: dict[str, Any]) -> str:
    parts = [f"{method} {url}"]
    if params := kwargs.get("params"):
        parts.append(f"params: {params}")
    if form := kwargs.get("form"):
        safe_form = {k: ("***" if k == "password" else v) for k, v in form.items()}
        parts.append(f"form: {safe_form}")
    if data := kwargs.get("data"):
        parts.append(f"data: {data}")
    return "\n".join(parts)
