# conftest.py
import pytest

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    mocked_device = playwright.devices['iPhone 12 Pro']
    return {
        **browser_context_args,
        **mocked_device,
    }

def test_browser(page):
    """
    This test navigates to the client side delay link which takes 15 
    seconds to load and verifies client data is loaded after the delay.
    This test also should run on an the device setup in 
    browser_context_args.
    """
    page.goto("/clientdelay")
    page.click(".btn-primary")
    assert page.inner_text(".bg-success")=="Data calculated on the client side."