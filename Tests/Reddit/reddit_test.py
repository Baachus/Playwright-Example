from reddit_model import Reddit

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

    #page.pause()
