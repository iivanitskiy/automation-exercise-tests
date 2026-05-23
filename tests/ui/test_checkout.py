import pytest

from automation_exercise.data.user_factory import UserData
from automation_exercise.ui.helpers.modal import dismiss_added_to_cart_modal
from automation_exercise.ui.pages.account_info_page import AccountInfoPage
from automation_exercise.ui.pages.cart_page import CartPage
from automation_exercise.ui.pages.checkout_page import CheckoutPage
from automation_exercise.ui.pages.home_page import HomePage
from automation_exercise.ui.pages.products_page import ProductsPage
from automation_exercise.ui.pages.signup_login_page import SignupLoginPage

pytestmark = [pytest.mark.ui, pytest.mark.regression]


class TestCheckout:
    @pytest.mark.smoke
    def test_case_15_place_order_register_before_checkout(
        self,
        home_page: HomePage,
        signup_login_page: SignupLoginPage,
        account_info_page: AccountInfoPage,
        products_page: ProductsPage,
        cart_page: CartPage,
        checkout_page: CheckoutPage,
        new_user: UserData,
        page,
    ) -> None:
        home_page.open()
        home_page.header.open_signup_login()
        signup_login_page.start_signup(new_user.name, new_user.email)
        account_info_page.fill_and_submit(new_user)
        account_info_page.confirm_created_and_continue()
        home_page.header.expect_logged_in_as(new_user.name)

        home_page.header.open_products()
        products_page.add_to_cart_by_index(0)
        dismiss_added_to_cart_modal(page, action="view_cart")
        cart_page.verify_loaded()
        cart_page.proceed_checkout.click()

        checkout_page.verify_checkout_loaded()
        checkout_page.place_order_with_comment("Automated order comment")
        checkout_page.pay()

        account_info_page.delete_account_and_continue()
