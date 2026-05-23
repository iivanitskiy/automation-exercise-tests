import pytest

from automation_exercise.api.assertions import assert_message, assert_response_code
from automation_exercise.api.services.search_api import SearchApi

pytestmark = [pytest.mark.api, pytest.mark.regression]


class TestSearchApi:
    @pytest.mark.parametrize("search_term", ["top", "tshirt", "jean"])
    def test_api_05_post_search_product(self, search_api: SearchApi, search_term: str) -> None:
        response = search_api.search(search_term)
        body = response.json()

        assert response.status == 200
        assert_response_code(body, 200)
        assert "products" in body

    def test_api_06_post_search_product_missing_parameter(self, search_api: SearchApi) -> None:
        response = search_api.search_without_param()
        body = response.json()

        assert response.status == 200
        assert_response_code(body, 400)
        assert_message(body, "search_product parameter is missing")
