import re

from playwright.sync_api import Locator, Page, expect

from automation_exercise.ui.helpers.consent import dismiss_cookie_consent
from automation_exercise.ui.pages.base_page import BasePage


class Header(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        nav = page.locator("#header, .navbar-nav").first
        self.signup_login_link = nav.get_by_role("link", name="Signup / Login")
        self.logout_link = nav.get_by_role("link", name="Logout")
        self.products_link = nav.locator("a[href='/products']")
        self.cart_link = nav.locator("a[href='/view_cart']")
        self.contact_us_link = nav.locator("a[href='/contact_us']")
        self.test_cases_link = nav.locator("a[href='/test_cases']")
        self.home_link = nav.locator("a[href='/']")
        self.delete_account_link = page.locator("a[href='/delete_account'], [data-qa='delete-account']")

    @property
    def logged_in_label(self) -> Locator:
        return self.page.locator("li").filter(has_text=re.compile(r"Logged in as"))

    def _click(self, locator) -> None:
        dismiss_cookie_consent(self.page)
        locator.click()

    def open_signup_login(self) -> None:
        self._click(self.signup_login_link)

    def open_products(self) -> None:
        self._click(self.products_link)

    def open_cart(self) -> None:
        self._click(self.cart_link)

    def open_contact_us(self) -> None:
        self._click(self.contact_us_link)

    def open_test_cases(self) -> None:
        self._click(self.test_cases_link)

    def delete_account(self) -> None:
        self._click(self.delete_account_link)

    def logout(self) -> None:
        self._click(self.logout_link)

    def expect_logged_in_as(self, username: str) -> None:
        expect(self.logged_in_label).to_contain_text(f"Logged in as {username}")

    def expect_not_logged_in(self) -> None:
        expect(self.logout_link).not_to_be_visible()
