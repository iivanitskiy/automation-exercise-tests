from playwright.sync_api import Page, expect

from automation_exercise.data.user_factory import UserData
from automation_exercise.ui.pages.base_page import BasePage


class SignupLoginPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.new_user_heading = page.get_by_text("New User Signup!")
        self.login_heading = page.get_by_text("Login to your account")
        self.signup_name = page.locator("[data-qa='signup-name']")
        self.signup_email = page.locator("[data-qa='signup-email']")
        self.signup_button = page.locator("[data-qa='signup-button']")
        self.login_email = page.locator("[data-qa='login-email']")
        self.login_password = page.locator("[data-qa='login-password']")
        self.login_button = page.locator("[data-qa='login-button']")
        self.login_error = page.locator("[data-qa='login-error']")
        self.signup_error = page.locator("[data-qa='signup-error']")

    def start_signup(self, name: str, email: str) -> None:
        expect(self.new_user_heading).to_be_visible()
        self.signup_name.fill(name)
        self.signup_email.fill(email)
        self.signup_button.click()

    def login(self, email: str, password: str) -> None:
        expect(self.login_heading).to_be_visible()
        self.login_email.fill(email)
        self.login_password.fill(password)
        self.login_button.click()

    def expect_login_error(self, message: str) -> None:
        expect(self.page.get_by_text(message)).to_be_visible()

    def expect_signup_error(self, message: str) -> None:
        expect(self.page.get_by_text(message)).to_be_visible()

    def expect_login_form_visible(self) -> None:
        expect(self.login_heading).to_be_visible()
