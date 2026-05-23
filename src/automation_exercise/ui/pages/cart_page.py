from playwright.sync_api import Page, expect

from automation_exercise.ui.pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.heading = page.locator("#cart_info_table")
        self.rows = page.locator("#cart_info_table tbody tr")
        self.proceed_checkout = page.locator(".btn.check_out")
        self.subscription_heading = page.get_by_role("heading", name="Subscription")
        self.subscription_email = page.locator("#susbscribe_email")
        self.subscription_submit = page.locator("#subscribe")

    def open(self) -> None:
        self.goto("/view_cart")

    def verify_loaded(self) -> None:
        expect(self.page).to_have_url(self.settings.base_url + "/view_cart")
        expect(self.page.get_by_text("Shopping Cart")).to_be_visible()

    def expect_product_count(self, count: int) -> None:
        expect(self.rows).to_have_count(count)

    def expect_product_names(self, names: list[str]) -> None:
        for name in names:
            expect(self.page.locator("#cart_info_table")).to_contain_text(name)

    def remove_product(self, index: int = 0) -> None:
        self.page.locator(".cart_quantity_delete").nth(index).click()

    def expect_empty_or_no_product(self, name: str) -> None:
        expect(self.page.locator("#cart_info_table")).not_to_contain_text(name)

    def subscribe(self, email: str) -> None:
        self.subscription_heading.scroll_into_view_if_needed()
        self.subscription_email.fill(email)
        self.subscription_submit.click()

    def expect_subscription_success(self) -> None:
        expect(self.page.locator(".alert-success")).to_contain_text(
            "You have been successfully subscribed!"
        )
