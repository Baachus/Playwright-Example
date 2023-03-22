class Bing:
    def __init__(self, page):
        self.page = page

        self.bing_url = "https://rewards.bing.com"

        self.sign_in_icon = "#raf-signin-link-id"
        self.email_input = "input[name='loginfmt']"
        self.email_next_btn = "#idSIButton9"

        self.password_input = "input[name='passwd']"
        self.password_next_btn = "#idSIButton9"
        self.confirm_btn = "input[id='idSIButton9']"
        self.signed_in = "a[class='redirect_link additional_info']"
        
        self.activity_card = "div[class='c-card-content']"
        self.plus_icon = "span.mee-icon.mee-icon-AddMedium"
        
        self.poll_icon = ":nth-match(:text('Daily poll'), 1)"
        self.not_signed_in = ":nth-match(:text('Sign in'), 1)"
        self.first_poll_answer = "#btoption0"

    def navigate(self):
        self.page.goto(self.bing_url)