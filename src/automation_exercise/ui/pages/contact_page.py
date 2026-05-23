from pathlib import Path

from playwright.sync_api import Page, expect

from automation_exercise.ui.helpers.consent import dismiss_cookie_consent
from automation_exercise.ui.pages.base_page import BasePage


class ContactPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.heading = page.get_by_text("Get In Touch")
        self.name = page.locator("[data-qa='name']")
        self.email = page.locator("[data-qa='email']")
        self.subject = page.locator("[data-qa='subject']")
        self.message = page.locator("[data-qa='message']")
        self.upload = page.locator("input[name='upload_file']")
        self.submit = page.locator("[data-qa='submit-button']")
        self.success = page.locator(".status.alert.alert-success")
        self.home = page.locator(".btn.btn-success")

    def open(self) -> None:
        self.goto("/contact_us")
        dismiss_cookie_consent(self.page)

    def submit_form(
        self,
        name: str,
        email: str,
        subject: str,
        message: str,
        file_path: Path | None = None,
    ) -> None:
        expect(self.heading).to_be_visible()
        self.name.fill(name)
        self.email.fill(email)
        self.subject.fill(subject)
        self.message.fill(message)
        if file_path:
            self.upload.set_input_files(str(file_path))
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.submit.click()

    def accept_dialog_and_verify_success(self) -> None:
        expect(self.page.locator("#contact-page .alert-success")).to_contain_text(
            "Success! Your details have been submitted successfully.",
            timeout=15_000,
        )

    def go_home(self) -> None:
        self.home.click()
