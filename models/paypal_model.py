class PayPal:
    def __init__(self, page):
        self.page = page

        self.paypal_url = "https://www.paypal.com"

        self.business_header = "#header-for-business"
        self.personal_header = "#header-personal"
        self.developer_header = "text=Developer"

        self.enterprise_link = "a[href$='enterprise']"
        self.more_link = "a[href='#']"
        self.buy_now_pay_later = "li>a[href$='buy-now-pay-later']"

    def navigate(self):
        self.page.goto(self.paypal_url)

    def click_link_business(self, page, linkName):
        page.hover(self.business_header)
        page.click(f"text={linkName}")
        page.go_back()

    def click_link_personal(self, page, linkName):
        page.hover(self.personal_header)
        page.click(f"text={linkName}")
        page.go_back()