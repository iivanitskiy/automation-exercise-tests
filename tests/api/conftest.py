import pytest

from automation_exercise.api.client import ApiClient
from automation_exercise.api.services.account_api import AccountApi
from automation_exercise.api.services.brands_api import BrandsApi
from automation_exercise.api.services.products_api import ProductsApi
from automation_exercise.api.services.search_api import SearchApi
from automation_exercise.data.user_factory import UserData, UserFactory


@pytest.fixture
def api_client(api_request_context) -> ApiClient:
    return ApiClient(api_request_context)


@pytest.fixture
def products_api(api_client) -> ProductsApi:
    return ProductsApi(api_client)


@pytest.fixture
def brands_api(api_client) -> BrandsApi:
    return BrandsApi(api_client)


@pytest.fixture
def search_api(api_client) -> SearchApi:
    return SearchApi(api_client)


@pytest.fixture
def account_api(api_client) -> AccountApi:
    return AccountApi(api_client)


@pytest.fixture
def new_user() -> UserData:
    return UserFactory.build()


@pytest.fixture
def registered_user(account_api, new_user) -> UserData:
    response = account_api.create_account(new_user)
    body = response.json()
    assert body.get("responseCode") == 201, body
    yield new_user
    delete_response = account_api.delete_account(new_user.email, new_user.password)
    assert delete_response.json().get("responseCode") == 200
