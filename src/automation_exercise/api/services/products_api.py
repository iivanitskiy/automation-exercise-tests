from playwright.sync_api import APIResponse

from automation_exercise.api.client import ApiClient


class ProductsApi:
    PATH = "/productsList"

    def __init__(self, client: ApiClient) -> None:
        self._client = client

    def get_all(self) -> APIResponse:
        return self._client.get(self.PATH)

    def post_all(self) -> APIResponse:
        return self._client.post(self.PATH)
