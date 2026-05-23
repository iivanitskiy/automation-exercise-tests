from playwright.sync_api import Page, expect

from automation_exercise.ui.pages.base_page import BasePage


class ProductDetailPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.name = page.locator(".product-information h2, .product-details h2").first
        self.category = page.locator(".product-information p").nth(0)
        self.price = page.locator(".product-information span span")
        self.availability = page.locator(".product-information p").nth(1)
        self.condition = page.locator(".product-information p").nth(2)
        self.brand = page.locator(".product-information p").nth(3)
        self.quantity = page.locator("#quantity")
        self.add_to_cart = page.locator("button.cart")
        self.review_heading = page.get_by_text("Write Your Review")
        self.review_name = page.locator("#name")
        self.review_email = page.locator("#email")
        self.review_text = page.locator("#review")
        self.review_submit = page.locator("#button-review")

    def verify_details_visible(self) -> None:
        expect(self.name).to_be_visible()
        expect(self.category).to_be_visible()
        expect(self.price).to_be_visible()
        expect(self.availability).to_be_visible()
        expect(self.condition).to_be_visible()
        expect(self.brand).to_be_visible()

    def set_quantity(self, qty: int) -> None:
        self.quantity.fill(str(qty))

    def click_add_to_cart(self) -> None:
        self.add_to_cart.click()

    def submit_review(self, name: str, email: str, review: str) -> None:
        from automation_exercise.ui.helpers.consent import dismiss_cookie_consent

        dismiss_cookie_consent(self.page)
        expect(self.review_heading).to_be_visible()
        self.review_name.fill(name)
        self.review_email.fill(email)
        self.review_text.fill(review)
        self.review_submit.click()
        expect(self.page.get_by_text("Thank you for your review.")).to_be_visible(timeout=15_000)
