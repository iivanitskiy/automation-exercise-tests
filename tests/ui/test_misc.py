from pathlib import Path

import pytest
from playwright.sync_api import expect

from automation_exercise.ui.pages.cart_page import CartPage
from automation_exercise.ui.pages.contact_page import ContactPage
from automation_exercise.ui.pages.home_page import HomePage

pytestmark = [pytest.mark.ui, pytest.mark.regression]


class TestMisc:
    def test_case_06_contact_us_form(self, home_page: HomePage, contact_page: ContactPage) -> None:
        upload_file = Path(__file__).resolve().parents[2] / "testdata" / "upload.txt"
        home_page.open()
        contact_page.open()
        contact_page.submit_form(
            name="Auto Tester",
            email="contact@test.com",
            subject="Automation",
            message="Contact form automated test",
            file_path=upload_file,
        )
        contact_page.accept_dialog_and_verify_success()
        contact_page.go_home()
        home_page.verify_loaded()

    def test_case_07_verify_test_cases_page(self, home_page: HomePage, page) -> None:
        home_page.open()
        home_page.header.open_test_cases()
        expect(page).to_have_url(home_page.settings.base_url + "/test_cases")
        expect(page.locator("b").filter(has_text="Test Cases")).to_be_visible()

    @pytest.mark.smoke
    def test_case_10_subscription_on_home_page(self, home_page: HomePage) -> None:
        home_page.open()
        home_page.scroll_to_footer()
        expect(home_page.subscription_heading).to_be_visible()
        home_page.subscribe("subscribe_home@test.com")
        home_page.expect_subscription_success()

    def test_case_11_subscription_on_cart_page(self, home_page: HomePage, cart_page: CartPage) -> None:
        home_page.open()
        home_page.header.open_cart()
        cart_page.verify_loaded()
        cart_page.subscribe("subscribe_cart@test.com")
        cart_page.expect_subscription_success()

    def test_case_25_scroll_up_with_arrow(self, home_page: HomePage) -> None:
        home_page.open()
        home_page.scroll_to_footer()
        expect(home_page.subscription_heading).to_be_visible()
        home_page.scroll_up_via_arrow()
        expect(home_page.hero_heading).to_be_in_viewport()

    def test_case_26_scroll_up_without_arrow(self, home_page: HomePage, page) -> None:
        home_page.open()
        home_page.verify_loaded()
        home_page.scroll_to_footer()
        page.evaluate("window.scrollTo(0, 0)")
        expect(home_page.hero_heading).to_be_in_viewport()
