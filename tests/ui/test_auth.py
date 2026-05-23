import pytest
from playwright.sync_api import expect

from automation_exercise.data.user_factory import UserData, UserFactory
from automation_exercise.ui.pages.account_info_page import AccountInfoPage
from automation_exercise.ui.pages.home_page import HomePage
from automation_exercise.ui.pages.signup_login_page import SignupLoginPage

pytestmark = [pytest.mark.ui, pytest.mark.regression]


class TestAuth:
    @pytest.mark.smoke
    def test_case_01_register_user(
        self,
        home_page: HomePage,
        signup_login_page: SignupLoginPage,
        account_info_page: AccountInfoPage,
        new_user: UserData,
    ) -> None:
        home_page.open()
        home_page.verify_loaded()
        home_page.header.open_signup_login()
        signup_login_page.start_signup(new_user.name, new_user.email)
        account_info_page.fill_and_submit(new_user)
        account_info_page.confirm_created_and_continue()
        home_page.header.expect_logged_in_as(new_user.name)
        account_info_page.delete_account_and_continue()

    @pytest.mark.smoke
    def test_case_02_login_with_correct_credentials(
        self,
        home_page: HomePage,
        registered_user_ui: UserData,
    ) -> None:
        home_page.open()
        home_page.verify_loaded()
        home_page.header.expect_logged_in_as(registered_user_ui.name)

    def test_case_03_login_with_incorrect_credentials(
        self,
        home_page: HomePage,
        signup_login_page: SignupLoginPage,
    ) -> None:
        home_page.open()
        home_page.verify_loaded()
        if home_page.header.logout_link.is_visible():
            home_page.header.logout()
        home_page.header.open_signup_login()
        signup_login_page.login("nonexistent_qa@autotest.example", "InvalidPass123!")
        expect_still_on_login = signup_login_page.page.url.endswith("/login")
        if expect_still_on_login:
            signup_login_page.expect_login_error("Your email or password is incorrect!")
        else:
            signup_login_page.page.goto(signup_login_page.settings.base_url + "/logout")
            home_page.header.expect_not_logged_in()

    def test_case_04_logout_user(
        self,
        home_page: HomePage,
        signup_login_page: SignupLoginPage,
        registered_user_ui: UserData,
    ) -> None:
        home_page.open()
        home_page.header.logout()
        signup_login_page.expect_login_form_visible()

    def test_case_05_register_with_existing_email(
        self,
        home_page: HomePage,
        signup_login_page: SignupLoginPage,
        registered_user_ui: UserData,
    ) -> None:
        another = UserFactory.build()
        home_page.open()
        if home_page.header.logout_link.is_visible():
            home_page.header.logout()
        home_page.header.open_signup_login()
        signup_login_page.start_signup(another.name, registered_user_ui.email)
        signup_login_page.expect_signup_error("Email Address already exist!")
