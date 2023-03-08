import pytest

from faker import Faker
from bing_model import Bing

def test_activities(page):
    """
    This test attempts to click on each activity for Bing rewards.
    """
    obj = Bing(page)
    obj.navigate()
    login_bing(page, obj)

    for card in page.query_selector_all(obj.plus_icon): #TODO: Update activity cards to be more speicific
        with page.context.expect_page() as tab:
            try:
                card.click()
            except:
                print("Unable to click on card")
        new_tab = tab.value
        new_tab.close()

def test_poll(page):
    """
    This test attempts to click on each poll for Bing rewards.
    """
    obj = Bing(page)
    obj.navigate()
    login_bing(page, obj)

    with page.expect_popup() as popup_info:
        page.click(obj.poll_icon)
    page1 = popup_info.value
    
    if(page1.locator(obj.not_signed_in).is_visible()):
        page1.locator(obj.not_signed_in).click()
    page1.click(obj.first_poll_answer)

def test_bing_search(page):
    """
    This test does a search on Bing for rewards.
    """
    obj = Bing(page)
    obj.navigate()
    login_bing(page, obj)

    search_text = []

    fake=Faker()
    for i in range(50):
        search_text.append(fake.word())
    
    page.goto("https://www.bing.com")
    page.wait_for_timeout(10000) # TODO: Update this to remove wait_for_timeout
    if(page.locator("#id_s").is_visible()):
        page.click("#id_s")
    
    for search in search_text:
        page.goto("https://www.bing.com")
        if(page.locator("#id_s").is_visible()):
            page.click("#id_s")
        page.fill("#sb_form_q", search)
        page.keyboard.press("Enter")
        page.wait_for_timeout(1000)

def login_bing(page, obj):
    if(page.locator(obj.sign_in_icon).is_visible()):
        page.click(obj.sign_in_icon)
    page.wait_for_selector(obj.email_input)
    page.fill(obj.email_input, "bc.robert@gmail.com")   #TODO: Update to parameterize username
    page.get_by_role("button", name="Next").click()

    page.wait_for_timeout(1000) # TODO: Update this to remove wait_for_timeout
    page.fill(obj.password_input, "SFs8Xiz62u5W")   #TODO: Update to remove password
    page.get_by_role("button", name="Sign in").click()

    page.wait_for_timeout(1000) # TODO: Update this to remove wait_for_timeout
    page.get_by_role("button", name="Yes").click()
    page.wait_for_url("https://rewards.bing.com/")

    assert page.inner_text(obj.signed_in)=="Robert Chapin "
