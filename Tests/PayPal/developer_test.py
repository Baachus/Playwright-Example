def test_help_link(page):
    """Navigates to the developer page and verifies the URL."""
    page.goto("https://www.paypal.com")
    page.click("text=Developer")
    assert page.url == "https://developer.paypal.com/home/"