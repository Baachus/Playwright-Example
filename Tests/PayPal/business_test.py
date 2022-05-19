import pytest

@pytest.mark.skip(reason="Hover feature a bit instable.")
def test_verify_business_links(page):
    """
    This test verifies all links in the business tab of paypal.
    It will click on the link than navigate back.
    """
    linksOnBusiness = [
        "Small-to-Medium Business",
        "Getting Started",
        "All Solution",
        "Accept Payments",
        "Make Payments",
        "Manage Risk",
        "Accelerate Growth",
        "Streamline Operations",
        "PayPal for Enterprise",
        "Platform and Capabilities",
        "Simplify Payment Operations",
        "Fraud Protection",
        "Global Payment Processing",
        "Payment Methods",
        "Product Spotlight",
        "Fundraising",
        "Marketplace and Platforms",
    ]

    page.goto('https://www.paypal.com')

    for links in linksOnBusiness:
        page.hover("#header-for-business")
        page.click(f"text={links}")
        page.go_back()

    # Special cases for Enterpirse and More since its text appears multiple 
    # times on home page.
    page.hover("#header-for-business")
    page.click("a[href$='enterprise']")
    page.go_back()

    page.hover("#header-for-business")
    page.click("a[href='#']")
    page.go_back()