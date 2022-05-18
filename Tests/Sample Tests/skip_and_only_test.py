import pytest

@pytest.mark.skip_browser("firefox")
def test_skip_on_firefox(page):
    """
    This test clicks a button on the default page but will be skipped
    by firefox
    """
    page.goto("/")
    page.click("text=Click")
    page.click("#badButton")

@pytest.mark.only_browser("chromium")
def test_only_run_on_chrome(page):
    """
    This test clicks a button on the default page but will be skipped by 
    all browsers but chromium
    """
    page.goto("/")
    page.click("text=Click")
    page.click("#badButton")