from reddit_model import Reddit

def test_nuke(page):
    """
    downvote all comments on a post
    """
    name_to_nuke = "Ok_Television4571"

    reddit_login(page)
    page.goto("https://old.reddit.com/user/"+name_to_nuke)

    buttons = page.query_selector_all("div[class*='down']")
    
    for button in buttons:
        if button.get_attribute("aria-label") == "downvote":
            button.click()


def test_reddit(page):
    """
    This test 
    """
    obj = Reddit(page)

    #basic navigation to site and search
    page.goto(obj.reddit_url)

    page.fill(obj.search_bar, 'SquaredCircle')
    page.click(obj.squaredcircle_search_label)
    
    page_fully_loaded = page.get_by_text("About Community")
    page_fully_loaded.wait_for()

    assert page.inner_text(obj.squaredcircle_title)=="r/SquaredCircle"

    #commented out but when included stops the test at this point to view page
    #page.pause()

def reddit_login(page):
    """
    login to reddit
    """
    page.goto("https://old.reddit.com/login")
    page.fill("input[id='user_login']", "Baachus")
    page.fill("input[id='passwd_login']", "RPdiYC863BP9.")  #added to password to make invalid
    page.click("button[type='submit'][tabindex='3']")