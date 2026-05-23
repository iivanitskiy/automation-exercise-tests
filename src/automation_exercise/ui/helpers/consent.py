import re

from playwright.sync_api import Page


def dismiss_cookie_consent(page: Page) -> None:

    overlay = page.locator(".fc-dialog-overlay")
    if not overlay.is_visible():
        return

    for selector in (
        "button.fc-cta-consent",
        "button.fc-button-label:has-text('Consent')",
        "button:has-text('Consent')",
        "button:has-text('Accept all')",
        "button:has-text('Accept')",
        "button:has-text('Agree')",
    ):
        button = page.locator(selector).first
        if button.is_visible():
            button.click(force=True)
            overlay.wait_for(state="hidden", timeout=15_000)
            return

    consent_btn = page.get_by_role("button", name=re.compile(r"consent|accept|agree", re.I)).first
    if consent_btn.is_visible():
        consent_btn.click(force=True)
        overlay.wait_for(state="hidden", timeout=15_000)
