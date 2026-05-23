import pytest

from automation_exercise.api.assertions import assert_message, assert_response_code
from automation_exercise.api.services.account_api import AccountApi
from automation_exercise.data.user_factory import UserData, UserFactory

pytestmark = [pytest.mark.api, pytest.mark.regression]


class TestVerifyLoginApi:
    def test_api_07_verify_login_valid_details(
        self, account_api: AccountApi, registered_user: UserData
    ) -> None:
        response = account_api.verify_login(registered_user.email, registered_user.password)
        body = response.json()

        assert response.status == 200
        assert_response_code(body, 200)
        assert_message(body, "User exists!")

    def test_api_08_verify_login_missing_email(self, account_api: AccountApi) -> None:
        response = account_api.verify_login_password_only("anypassword")
        body = response.json()

        assert response.status == 200
        assert_response_code(body, 400)
        assert_message(body, "email or password parameter is missing")

    def test_api_09_delete_verify_login_not_supported(self, account_api: AccountApi) -> None:
        response = account_api.delete_verify_login()
        body = response.json()

        assert response.status == 200
        assert_response_code(body, 405)
        assert_message(body, "This request method is not supported.")

    def test_api_10_verify_login_invalid_details(self, account_api: AccountApi) -> None:
        response = account_api.verify_login("invalid@example.com", "wrongpassword")
        body = response.json()

        assert response.status == 200
        assert_response_code(body, 404)
        assert_message(body, "User not found!")


class TestAccountCrudApi:
    def test_api_11_create_user_account(self, account_api: AccountApi, new_user: UserData) -> None:
        response = account_api.create_account(new_user)
        body = response.json()

        assert response.status == 200
        assert_response_code(body, 201)
        assert_message(body, "User created!")

        account_api.delete_account(new_user.email, new_user.password)

    def test_api_12_delete_user_account(self, account_api: AccountApi, new_user: UserData) -> None:
        account_api.create_account(new_user)
        response = account_api.delete_account(new_user.email, new_user.password)
        body = response.json()

        assert response.status == 200
        assert_response_code(body, 200)
        assert_message(body, "Account deleted!")

    def test_api_13_update_user_account(self, account_api: AccountApi, registered_user: UserData) -> None:
        updated = UserFactory.build(
            email=registered_user.email,
            password=registered_user.password,
            firstname="UpdatedFirst",
        )
        response = account_api.update_account(updated)
        body = response.json()

        assert response.status == 200
        assert_response_code(body, 200)
        assert_message(body, "User updated!")

    def test_api_14_get_user_detail_by_email(
        self, account_api: AccountApi, registered_user: UserData
    ) -> None:
        response = account_api.get_user_by_email(registered_user.email)
        body = response.json()

        assert response.status == 200
        assert_response_code(body, 200)
        assert "user" in body
        assert body["user"]["email"] == registered_user.email
