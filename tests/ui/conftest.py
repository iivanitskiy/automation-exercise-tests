import pytest

from automation_exercise.data.user_factory import UserData, UserFactory
from automation_exercise.ui.pages.account_info_page import AccountInfoPage
from automation_exercise.ui.pages.cart_page import CartPage
from automation_exercise.ui.pages.checkout_page import CheckoutPage
from automation_exercise.ui.pages.contact_page import ContactPage
from automation_exercise.ui.pages.home_page import HomePage
from automation_exercise.ui.pages.product_detail_page import ProductDetailPage
from automation_exercise.ui.pages.products_page import ProductsPage
from automation_exercise.ui.pages.signup_login_page import SignupLoginPage


@pytest.fixture
def home_page(page) -> HomePage:
    return HomePage(page)


@pytest.fixture
def signup_login_page(page) -> SignupLoginPage:
    return SignupLoginPage(page)


@pytest.fixture
def account_info_page(page) -> AccountInfoPage:
    return AccountInfoPage(page)


@pytest.fixture
def products_page(page) -> ProductsPage:
    return ProductsPage(page)


@pytest.fixture
def product_detail_page(page) -> ProductDetailPage:
    return ProductDetailPage(page)


@pytest.fixture
def cart_page(page) -> CartPage:
    return CartPage(page)


@pytest.fixture
def checkout_page(page) -> CheckoutPage:
    return CheckoutPage(page)


@pytest.fixture
def contact_page(page) -> ContactPage:
    return ContactPage(page)


@pytest.fixture
def new_user() -> UserData:
    return UserFactory.build()


@pytest.fixture
def registered_user_ui(
    home_page: HomePage,
    signup_login_page: SignupLoginPage,
    account_info_page: AccountInfoPage,
    new_user: UserData,
) -> UserData:
    home_page.open()
    home_page.header.open_signup_login()
    signup_login_page.start_signup(new_user.name, new_user.email)
    account_info_page.fill_and_submit(new_user)
    account_info_page.confirm_created_and_continue()
    home_page.header.expect_logged_in_as(new_user.name)
    yield new_user
    home_page.open()
    if not home_page.header.logout_link.is_visible():
        home_page.header.open_signup_login()
        signup_login_page.login(new_user.email, new_user.password)
    home_page.header.delete_account()
    account_info_page.account_deleted.wait_for()
    account_info_page.continue_btn.click()
