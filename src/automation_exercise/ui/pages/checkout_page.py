from playwright.sync_api import Page, expect

from automation_exercise.data.user_factory import UserData
from automation_exercise.ui.helpers.consent import dismiss_cookie_consent
from automation_exercise.ui.pages.base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.address_heading = page.get_by_text("Address Details")
        self.review_heading = page.get_by_text("Review Your Order")
        self.comment = page.locator("textarea[name='message']")
        self.place_order = page.locator("a.check_out")
        self.name_on_card = page.locator("[data-qa='name-on-card']")
        self.card_number = page.locator("[data-qa='card-number']")
        self.cvc = page.locator("[data-qa='cvc']")
        self.expiry_month = page.locator("[data-qa='expiry-month']")
        self.expiry_year = page.locator("[data-qa='expiry-year']")
        self.pay_confirm = page.locator("[data-qa='pay-button']")
        self.order_success = page.get_by_text("Order Placed!")
        self.download_invoice = page.locator("a[href*='download_invoice']")

    def verify_checkout_loaded(self) -> None:
        expect(self.address_heading).to_be_visible()
        expect(self.review_heading).to_be_visible()

    def verify_address_matches_user(self, user: UserData) -> None:
        delivery = self.page.locator("#address_delivery")
        billing = self.page.locator("#address_invoice")
        for field in (user.firstname, user.lastname, user.address1, user.city, user.zipcode):
            expect(delivery).to_contain_text(field)
            expect(billing).to_contain_text(field)

    def place_order_with_comment(self, comment: str) -> None:
        dismiss_cookie_consent(self.page)
        self.comment.fill(comment)
        self.place_order.click(force=True)

    def pay(self) -> None:
        self.name_on_card.fill("Test User")
        self.card_number.fill("4111111111111111")
        self.cvc.fill("123")
        self.expiry_month.fill("12")
        self.expiry_year.fill("2030")
        self.pay_confirm.click()
        expect(self.order_success).to_be_visible()
