# pyrefly: ignore [missing-import]
from playwright.sync_api import Page

def fechar_popup(page: Page):
    close_button = page.locator('button[aria-label="Close dialog"].klaviyo-close-form')
    try:
        close_button.wait_for(state="visible", timeout=15000)
        close_button.click()
        
        page.locator('div[role="dialog"][aria-label="POPUP Form"]').wait_for(state="hidden", timeout=10000)
    except Exception:
        
        pass