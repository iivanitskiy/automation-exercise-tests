from playwright.sync_api import Locator, Page, expect

from automation_exercise.ui.components.header import Header
from automation_exercise.ui.pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.header = Header(page)
        self.hero_heading = page.get_by_role(
            "heading",
            name="Full-Fledged practice website for Automation Engineers",
        ).first
        self.subscription_heading = page.get_by_role("heading", name="Subscription")
        self.subscription_email = page.locator("#susbscribe_email")
        self.subscription_submit = page.locator("#subscribe")
        self.scroll_up_button = page.locator("#scrollUp")

    def open(self) -> None:
        self.goto("/")

    def verify_loaded(self) -> None:
        expect(self.page).to_have_url(self.settings.base_url + "/")
        expect(self.hero_heading).to_be_visible()

    def subscribe(self, email: str) -> None:
        from automation_exercise.ui.helpers.consent import dismiss_cookie_consent

        dismiss_cookie_consent(self.page)
        self.subscription_email.scroll_into_view_if_needed()
        self.subscription_email.fill(email)
        self.subscription_submit.click()

    def expect_subscription_success(self) -> None:
        expect(self.page.locator(".alert-success")).to_contain_text(
            "You have been successfully subscribed!"
        )

    def scroll_to_footer(self) -> None:
        self.subscription_heading.scroll_into_view_if_needed()

    def scroll_up_via_arrow(self) -> None:
        self.scroll_up_button.click()

    def first_product_view_link(self) -> Locator:
        return self.page.locator(".features_items .product-image-wrapper").first.locator(
            "a[href*='product_details']"
        )
