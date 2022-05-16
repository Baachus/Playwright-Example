import pytest 
from pytest_bdd import scenarios, given, when, then, parsers
 
# Constants
DUCKDUCKGO_HOMEPAGE = 'https://duckduckgo.com/'

# Scenarios - commented out so none will run
#scenarios('../Tests/features/web.feature')

# Given Steps
@given('the DuckDuckGo home page is displayed')
def ddg_home(page):
    """This method navigates to the duckduckgo website"""
    page.goto(DUCKDUCKGO_HOMEPAGE)
 
# When Steps
@when(parsers.parse('the user searches for "{phrase}"'))
def search_phrase(page, phrase):
    """This method fills in a phrase and presses the enter button"""
    page.fill("#search_form_input_homepage", phrase)
    page.press("#search_form_input_homepage", 'Enter')
 
# Then Steps
@then(parsers.parse('results are shown for "{phrase}"'))
def search_results(page, phrase):
    """
    This method verifies the search field is set to the phrase sent in
    """
    # Check search phrase
    assert page.locator('#search_form_input').get_attribute('value') == phrase
    print(phrase)