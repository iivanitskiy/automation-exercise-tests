from typing import Any

from playwright.sync_api import APIResponse

from automation_exercise.api.client import ApiClient
from automation_exercise.data.user_factory import UserData


class AccountApi:
    VERIFY_LOGIN = "/verifyLogin"
    CREATE = "/createAccount"
    DELETE = "/deleteAccount"
    UPDATE = "/updateAccount"
    GET_BY_EMAIL = "/getUserDetailByEmail"

    def __init__(self, client: ApiClient) -> None:
        self._client = client

    def verify_login(self, email: str, password: str) -> APIResponse:
        return self._client.post(
            self.VERIFY_LOGIN,
            form={"email": email, "password": password},
        )

    def verify_login_password_only(self, password: str) -> APIResponse:
        return self._client.post(self.VERIFY_LOGIN, form={"password": password})

    def delete_verify_login(self) -> APIResponse:
        return self._client.delete(self.VERIFY_LOGIN)

    def create_account(self, user: UserData) -> APIResponse:
        return self._client.post(self.CREATE, form=user.to_api_payload())

    def delete_account(self, email: str, password: str) -> APIResponse:
        return self._client.delete(
            self.DELETE,
            form={"email": email, "password": password},
        )

    def update_account(self, user: UserData) -> APIResponse:
        return self._client.put(self.UPDATE, form=user.to_api_payload())

    def get_user_by_email(self, email: str) -> APIResponse:
        return self._client.get(self.GET_BY_EMAIL, params={"email": email})
