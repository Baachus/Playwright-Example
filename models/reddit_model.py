class Reddit:
    def __init__(self, page):
        self.page = page

        self.reddit_url = "https://www.reddit.com"
        self.search_bar = "#header-search-bar"
        self.squaredcircle_search_label = "[aria-label='r/SquaredCircle']"
        self.squaredcircle_title = "h1"