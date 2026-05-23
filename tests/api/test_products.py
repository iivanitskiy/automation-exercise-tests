import pytest

from automation_exercise.api.assertions import assert_message, assert_response_code
from automation_exercise.api.services.products_api import ProductsApi

pytestmark = [pytest.mark.api, pytest.mark.regression]


class TestProductsApi:
    def test_api_01_get_all_products_list(self, products_api: ProductsApi) -> None:
        response = products_api.get_all()
        body = response.json()

        assert response.status == 200
        assert_response_code(body, 200)
        assert "products" in body
        assert len(body["products"]) > 0

    def test_api_02_post_to_all_products_list_not_supported(self, products_api: ProductsApi) -> None:
        response = products_api.post_all()
        body = response.json()

        assert response.status == 200
        assert_response_code(body, 405)
        assert_message(body, "This request method is not supported.")
