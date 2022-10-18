class Intercept:
    def __init__(self, page):
        self.page = page

        self.etsy_url = "https://etsy.com"
        self.search_input = "id=global-enhancements-search-query"

    def navigate(self):
        self.page.goto(self.etsy_url)