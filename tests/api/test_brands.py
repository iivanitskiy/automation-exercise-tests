import pytest

from automation_exercise.api.assertions import assert_message, assert_response_code
from automation_exercise.api.services.brands_api import BrandsApi

pytestmark = [pytest.mark.api, pytest.mark.regression]


class TestBrandsApi:
    def test_api_03_get_all_brands_list(self, brands_api: BrandsApi) -> None:
        response = brands_api.get_all()
        body = response.json()

        assert response.status == 200
        assert_response_code(body, 200)
        assert "brands" in body
        assert len(body["brands"]) > 0

    def test_api_04_put_to_all_brands_list_not_supported(self, brands_api: BrandsApi) -> None:
        response = brands_api.put_all()
        body = response.json()

        assert response.status == 200
        assert_response_code(body, 405)
        assert_message(body, "This request method is not supported.")
