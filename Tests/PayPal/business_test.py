import pytest
from paypal_model import PayPal

@pytest.mark.skip(reason="Hover feature a bit instable.")
def test_verify_business_links(page):
    """
    This test verifies all links in the business tab of paypal.
    It will click on the link than navigate back.
    """
    obj = PayPal(page)

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

    obj.navigate()

    for links in linksOnBusiness:
        obj.click_link_business(page, links)

    # Special cases for Enterpirse and More since its text appears multiple 
    # times on home page.
    page.hover(obj.business_header)
    page.click(obj.enterprise_link)
    page.go_back()

    page.hover(obj.business_header)
    page.click(obj.more_link)
    page.go_back()