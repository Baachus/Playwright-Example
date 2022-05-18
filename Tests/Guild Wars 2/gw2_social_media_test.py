import pytest

@pytest.mark.skip(reason="This test is instable and context ruins other tests "
                        +"need to research more.")
def test_verify_social_media_links(context, page, url='https://guildjen.com/'):
    """
    This test verifies the social media links on the right hand side 
    of the home page.
    """
    page.goto(url)
    with context.expect_page() as new_page_info:
        page.click("img[title='Youtube']")  #opens in a new tab
    new_page = new_page_info.value

    new_page.wait_for_load_state()
    assert new_page.url.__contains__('https://www.youtube.com/guildjen')
    new_page.close
    
    page.goto(url)
    with context.expect_page() as new_page_info:
        page.click("img[title='Twitter']")  #opens in a new tab
    new_page = new_page_info.value

    new_page.wait_for_load_state()
    assert new_page.url.__contains__('https://twitter.com/guildjenn')
    new_page.close
    
    page.goto(url)
    with context.expect_page() as new_page_info:
        page.click("img[title='Discord']")  #opens in a new tab
    new_page = new_page_info.value

    new_page.wait_for_load_state()
    assert new_page.url.__contains__('https://discord.com/invite/8NZNRvC')
    new_page.close
    
    page.goto(url)
    with context.expect_page() as new_page_info:
        page.click("img[title='Facebook']")  #opens in a new tab
    new_page = new_page_info.value

    new_page.wait_for_load_state()
    assert new_page.url.__contains__('https://www.facebook.com/guildjen')
    new_page.close
    
    page.goto(url)
    with context.expect_page() as new_page_info:
        page.click("img[title='Instagram']")  #opens in a new tab
    new_page = new_page_info.value

    new_page.wait_for_load_state()
    assert new_page.url.__contains__('https://www.instagram.com/')
    assert new_page.url.__contains__('guildjen')
    new_page.close
    
    page.goto(url)
    with context.expect_page() as new_page_info:
        page.click("img[title='Steam']")  #opens in a new tab
    new_page = new_page_info.value

    new_page.wait_for_load_state()
    assert new_page.url.__contains__('https://steamcommunity.com/groups/guildjen')
    new_page.close

@pytest.mark.skip(reason="This test is instable and context ruins other tests "
                        +"need to research more.")
def test_support_social_media_links(context, page):
    """This test verifies the social media links on the support page"""
    url = "https://guildjen.com/support/"
    test_verify_social_media_links(context, page, url)