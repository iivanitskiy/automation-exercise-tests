from playwright.sync_api import Page

from automation_exercise.ui.helpers.consent import dismiss_cookie_consent


def dismiss_added_to_cart_modal(page: Page, action: str = "continue") -> None:
    dismiss_cookie_consent(page)
    modal = page.locator("#cartModal")
    modal.wait_for(state="visible")
    if action == "view_cart":
        modal.get_by_text("View Cart").click()
    else:
        modal.get_by_text("Continue Shopping").click()
