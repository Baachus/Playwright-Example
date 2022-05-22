from paypal_model import PayPal
import pytest

@pytest.mark.skip(reason="something to look into.")
def test_help_link(page):
    """Navigates to the developer page and verifies the URL."""
    obj = PayPal(page)
    obj.navigate()

    page.click(obj.developer_header)
    
    assert page.url == "https://developer.paypal.com/home/"