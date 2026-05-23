from playwright.sync_api import APIResponse

from automation_exercise.api.client import ApiClient


class SearchApi:
    PATH = "/searchProduct"

    def __init__(self, client: ApiClient) -> None:
        self._client = client

    def search(self, search_product: str) -> APIResponse:
        return self._client.post(
            self.PATH,
            form={"search_product": search_product},
        )

    def search_without_param(self) -> APIResponse:
        return self._client.post(self.PATH)
