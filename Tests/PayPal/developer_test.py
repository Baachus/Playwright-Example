from paypal_model import PayPal
def test_help_link(page):
    """Navigates to the developer page and verifies the URL."""
    obj = PayPal(page)
    obj.navigate()

    page.click(obj.developer_header)
    
    assert page.url == "https://developer.paypal.com/home/"