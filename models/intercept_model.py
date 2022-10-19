class Intercept:
    def __init__(self, page):
        self.page = page

        self.etsy_url = "https://etsy.com"
        self.danube_url = "http://danube-webshop.herokuapp.com/"
        self.search_input = "id=global-enhancements-search-query"

    def navigate(self):
        self.page.goto(self.etsy_url)

    def navigate_to_danube(self):
        self.page.goto(self.danube_url)