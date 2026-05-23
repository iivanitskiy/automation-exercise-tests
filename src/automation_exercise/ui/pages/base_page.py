from playwright.sync_api import Locator, Page, expect

from config.settings import get_settings


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.settings = get_settings()
        self.page.set_default_timeout(self.settings.timeout_ms)

    def goto(self, path: str = "/") -> None:
        from automation_exercise.ui.helpers.consent import dismiss_cookie_consent

        url = path if path.startswith("http") else f"{self.settings.base_url}{path}"
        self.page.goto(url, wait_until="domcontentloaded")
        dismiss_cookie_consent(self.page)

    def locator(self, selector: str) -> Locator:
        return self.page.locator(selector)

    def expect_visible(self, locator: Locator) -> None:
        expect(locator).to_be_visible()

    def expect_text(self, locator: Locator, text: str | list[str]) -> None:
        expect(locator).to_contain_text(text)
