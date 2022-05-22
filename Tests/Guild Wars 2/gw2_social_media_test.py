import pytest
from gw2_model import GuildWars2

@pytest.mark.skip(reason="does stuff.")
def test_verify_social_media_links(context, page):
    """
    This test verifies the social media links on the right hand side 
    of the home page.
    """
    obj = GuildWars2(page)
    obj.navigate()

    with context.expect_page() as new_page_info:
        page.click(obj.youtube_link)  #opens in a new tab
    new_page = new_page_info.value

    new_page.wait_for_load_state()
    assert new_page.url.__contains__('https://www.youtube.com/guildjen')
    new_page.close
    
    obj.navigate()
    with context.expect_page() as new_page_info:
        page.click(obj.twitter_link)  #opens in a new tab
    new_page = new_page_info.value

    new_page.wait_for_load_state()
    assert new_page.url.__contains__('https://twitter.com/guildjenn')
    new_page.close
    
    obj.navigate()
    with context.expect_page() as new_page_info:
        page.click(obj.discord_link)  #opens in a new tab
    new_page = new_page_info.value

    new_page.wait_for_load_state()
    assert new_page.url.__contains__('https://discord.com/invite/8NZNRvC')
    new_page.close
    
    obj.navigate()
    with context.expect_page() as new_page_info:
        page.click(obj.facebook_link)  #opens in a new tab
    new_page = new_page_info.value

    new_page.wait_for_load_state()
    assert new_page.url.__contains__('https://www.facebook.com/guildjen')
    new_page.close
        
    obj.navigate()
    with context.expect_page() as new_page_info:
        page.click(obj.instagram_link)  #opens in a new tab
    new_page = new_page_info.value

    new_page.wait_for_load_state()
    assert new_page.url.__contains__('https://www.instagram.com/')
    assert new_page.url.__contains__('guildjen')
    new_page.close
        
    obj.navigate()
    with context.expect_page() as new_page_info:
        page.click(obj.steam_link)  #opens in a new tab
    new_page = new_page_info.value

    new_page.wait_for_load_state()
    assert new_page.url.__contains__('https://steamcommunity.com/groups/guildjen')
    new_page.close