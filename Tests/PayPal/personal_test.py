import pytest
from paypal_model import PayPal

@pytest.mark.skip(reason="Hover feature a bit instable.")
def test_verify_personal_links(page):
    """
    This test verifies all links in the personal tab of paypal.
    It will click on the link than navigate back.
    """
    obj = PayPal(page)

    linksOnPersonal = [
        "Shop and Buy",
        "Deals and Cash Back",
        "Pay with Rewards",
        "Pay with QR Codes",
        "Checkout with Crypto",
        "PayPal Credit and Cards",
        "Send and Receive",
        "Send Money",
        "Request Money",
        "Start Selling",
        "Donate and Raise Funds",
        "Manage Your Money",
        "Set up Direct Deposit",
        "Deposit Checks",
        "Add Cash",
        "Savings and Goals",
        "Buy and Sell Crypto",
        "Pay Bills",
    ]

    obj.navigate()

    for links in linksOnPersonal:
        obj.click_link_personal(page, links)

    # Special cases for Buy Now, Pay Later since its text appears multiple
    # times on home page.
    page.hover(obj.personal_header)
    page.click(obj.buy_now_pay_later)
    page.go_back()
