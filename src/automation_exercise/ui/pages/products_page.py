import re

from playwright.sync_api import Locator, Page, expect

from automation_exercise.ui.helpers.consent import dismiss_cookie_consent
from automation_exercise.ui.pages.base_page import BasePage


class ProductsPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.heading = page.get_by_text("All Products")
        self.search_input = page.locator("#search_product")
        self.search_button = page.locator("#submit_search")
        self.product_cards = page.locator(".features_items .productinfo")
        self.sidebar_categories = page.locator(".left-sidebar .category-products")
        self.sidebar_brands = page.locator(".left-sidebar .brands_products")

    def open(self) -> None:
        self.goto("/products")
        dismiss_cookie_consent(self.page)

    def verify_loaded(self) -> None:
        expect(self.page).to_have_url(self.settings.base_url + "/products")
        expect(self.heading).to_be_visible()
        expect(self.product_cards.first).to_be_visible()

    def search(self, query: str) -> None:
        self.search_input.fill(query)
        self.search_button.click()

    def expect_search_results(self, query: str) -> None:
        import re

        expect(self.page.get_by_text("Searched Products")).to_be_visible()
        expect(self.product_cards.first).to_be_visible()
        pattern = re.compile(query, re.IGNORECASE)
        expect(self.product_cards.filter(has_text=pattern).first).to_be_visible()

    def view_product_by_index(self, index: int = 0) -> None:
        dismiss_cookie_consent(self.page)
        self.page.locator("a[href*='product_details']").nth(index).click()
        expect(self.page).to_have_url(re.compile(r".*/product_details/\d+"))

    def add_to_cart_by_index(self, index: int) -> None:
        dismiss_cookie_consent(self.page)
        card = self.product_cards.nth(index)
        card.hover()
        add_btn = card.locator("a.add-to-cart, .overlay-content .add-to-cart").first
        add_btn.click(force=True)

    def click_category(self, category: str) -> None:
        self.page.locator(f"a[href*='category_products']").filter(has_text=category).first.click()

    def click_subcategory(self, name: str) -> None:
        self.page.locator(".panel-body a").filter(has_text=name).first.click()

    def click_brand(self, brand: str) -> None:
        self.page.locator(".brands-name a").filter(has_text=brand).first.click()

    def expect_category_title(self, text: str) -> None:
        expect(self.page.locator(".title")).to_contain_text(text, ignore_case=True)
