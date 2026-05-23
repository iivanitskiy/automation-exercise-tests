from playwright.sync_api import Page, expect

from automation_exercise.data.user_factory import UserData
from automation_exercise.ui.pages.base_page import BasePage


class AccountInfoPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.heading = page.get_by_text("Enter Account Information")
        self.password = page.locator("#password")
        self.day = page.locator("#days")
        self.month = page.locator("#months")
        self.year = page.locator("#years")
        self.newsletter = page.locator("#newsletter")
        self.offers = page.locator("#optin")
        self.first_name = page.locator("#first_name")
        self.last_name = page.locator("#last_name")
        self.company = page.locator("#company")
        self.address1 = page.locator("#address1")
        self.address2 = page.locator("#address2")
        self.country = page.locator("#country")
        self.state = page.locator("#state")
        self.city = page.locator("#city")
        self.zipcode = page.locator("#zipcode")
        self.mobile = page.locator("#mobile_number")
        self.create_account_btn = page.locator("[data-qa='create-account']")
        self.account_created = page.get_by_text("Account Created!")
        self.continue_btn = page.locator("[data-qa='continue-button']")
        self.delete_account_btn = page.locator("a[href='/delete_account'], [data-qa='delete-account']")
        self.account_deleted = page.get_by_text("Account Deleted!")

    def fill_and_submit(self, user: UserData) -> None:
        expect(self.heading).to_be_visible()
        self.page.locator(f"input[value='{user.title}']").check()
        self.password.fill(user.password)
        self.day.select_option(user.birth_date)
        self.month.select_option(user.birth_month)
        self.year.select_option(user.birth_year)
        self.newsletter.check()
        self.offers.check()
        self.first_name.fill(user.firstname)
        self.last_name.fill(user.lastname)
        self.company.fill(user.company)
        self.address1.fill(user.address1)
        self.address2.fill(user.address2)
        self.country.select_option(user.country)
        self.state.fill(user.state)
        self.city.fill(user.city)
        self.zipcode.fill(user.zipcode)
        self.mobile.fill(user.mobile_number)
        self.create_account_btn.click()

    def confirm_created_and_continue(self) -> None:
        expect(self.account_created).to_be_visible()
        self.continue_btn.click()

    def delete_account_and_continue(self) -> None:
        from automation_exercise.ui.components.header import Header

        Header(self.page).delete_account()
        expect(self.account_deleted).to_be_visible()
        self.continue_btn.click()
