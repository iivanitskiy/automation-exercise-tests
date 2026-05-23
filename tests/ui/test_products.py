import pytest
from playwright.sync_api import expect

from automation_exercise.ui.helpers.modal import dismiss_added_to_cart_modal
from automation_exercise.ui.pages.cart_page import CartPage
from automation_exercise.ui.pages.home_page import HomePage
from automation_exercise.ui.pages.product_detail_page import ProductDetailPage
from automation_exercise.ui.pages.products_page import ProductsPage

pytestmark = [pytest.mark.ui, pytest.mark.regression]


class TestProducts:
    @pytest.mark.smoke
    def test_case_08_verify_all_products_and_detail(
        self, home_page: HomePage, products_page: ProductsPage, product_detail_page: ProductDetailPage
    ) -> None:
        home_page.open()
        home_page.verify_loaded()
        home_page.header.open_products()
        products_page.verify_loaded()
        products_page.view_product_by_index(0)
        product_detail_page.verify_details_visible()

    @pytest.mark.smoke
    def test_case_09_search_product(self, home_page: HomePage, products_page: ProductsPage) -> None:
        home_page.open()
        home_page.header.open_products()
        products_page.verify_loaded()
        products_page.search("Top")
        products_page.expect_search_results("Top")

    def test_case_18_view_category_products(self, home_page: HomePage, page) -> None:
        home_page.open()
        page.locator("a[href='#Women']").click()
        page.locator(".panel-body a").filter(has_text="Dress").first.click()
        expect(page.locator(".title")).to_contain_text("Women - Dress", ignore_case=True)

    def test_case_19_view_brand_products(self, home_page: HomePage, products_page: ProductsPage) -> None:
        home_page.open()
        products_page.open()
        products_page.click_brand("Polo")
        products_page.expect_category_title("Brand - Polo products")

    def test_case_21_add_review_on_product(
        self,
        home_page: HomePage,
        products_page: ProductsPage,
        product_detail_page: ProductDetailPage,
    ) -> None:
        home_page.open()
        home_page.header.open_products()
        products_page.view_product_by_index(0)
        product_detail_page.submit_review("Reviewer", "review@test.com", "Great product for automation practice.")

    def test_case_22_add_to_cart_from_recommended(
        self, home_page: HomePage, cart_page: CartPage, page
    ) -> None:
        from automation_exercise.ui.helpers.consent import dismiss_cookie_consent

        home_page.open()
        dismiss_cookie_consent(page)
        page.locator(".recommended_items").scroll_into_view_if_needed()
        page.locator("#recommended-item-carousel .item.active .add-to-cart, .recommended_items .active .add-to-cart").first.click(
            force=True
        )
        dismiss_added_to_cart_modal(page, action="view_cart")
        cart_page.verify_loaded()
        cart_page.expect_product_count(1)
