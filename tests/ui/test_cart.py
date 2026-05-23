import pytest
from playwright.sync_api import expect

from automation_exercise.ui.helpers.modal import dismiss_added_to_cart_modal
from automation_exercise.ui.pages.cart_page import CartPage
from automation_exercise.ui.pages.home_page import HomePage
from automation_exercise.ui.pages.product_detail_page import ProductDetailPage
from automation_exercise.ui.pages.products_page import ProductsPage

pytestmark = [pytest.mark.ui, pytest.mark.regression]


class TestCart:
    @pytest.mark.smoke
    def test_case_12_add_products_in_cart(
        self, home_page: HomePage, products_page: ProductsPage, cart_page: CartPage, page
    ) -> None:
        home_page.open()
        home_page.header.open_products()
        products_page.add_to_cart_by_index(0)
        dismiss_added_to_cart_modal(page, action="continue")
        products_page.add_to_cart_by_index(1)
        dismiss_added_to_cart_modal(page, action="view_cart")
        cart_page.verify_loaded()
        cart_page.expect_product_count(2)

    def test_case_13_verify_product_quantity_in_cart(
        self,
        home_page: HomePage,
        product_detail_page: ProductDetailPage,
        cart_page: CartPage,
        page,
    ) -> None:
        home_page.open()
        home_page.first_product_view_link().click()
        product_detail_page.set_quantity(4)
        product_detail_page.click_add_to_cart()
        dismiss_added_to_cart_modal(page, action="view_cart")
        cart_page.verify_loaded()
        expect_qty = page.locator(".cart_quantity button").first
        expect(expect_qty).to_have_text("4")

    def test_case_17_remove_products_from_cart(
        self, home_page: HomePage, products_page: ProductsPage, cart_page: CartPage, page
    ) -> None:
        home_page.open()
        home_page.header.open_products()
        products_page.add_to_cart_by_index(0)
        dismiss_added_to_cart_modal(page, action="view_cart")
        cart_page.verify_loaded()
        cart_page.remove_product(0)
        cart_page.expect_product_count(0)
