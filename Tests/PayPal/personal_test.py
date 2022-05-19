import pytest

@pytest.mark.skip(reason="Hover feature a bit instable.")
def test_verify_personal_links(page):
    """
    This test verifies all links in the personal tab of paypal.
    It will click on the link than navigate back.
    """
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

    page.goto('https://www.paypal.com')

    for links in linksOnPersonal:
        page.hover("#header-personal")
        page.click(f"text={links}")
        page.go_back()

        
    # Special cases for Buy Now, Pay Later since its text appears multiple
    # times on home page.
    page.hover("#header-personal")
    page.click("li>a[href$='buy-now-pay-later']")
    page.go_back()