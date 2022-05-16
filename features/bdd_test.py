import pytest 
from pytest_bdd import scenarios, given, when, then, parsers
 
# Constants
DUCKDUCKGO_HOME = 'https://duckduckgo.com/'

# Scenarios
#scenarios('../Tests/features/web.feature')

# Given Steps
@given('the DuckDuckGo home page is displayed')
def ddg_home(page):
    page.goto(DUCKDUCKGO_HOME)
 
# When Steps
@when(parsers.parse('the user searches for "{phrase}"'))
def search_phrase(page, phrase):
    page.fill("#search_form_input_homepage", phrase)
    page.press("#search_form_input_homepage", 'Enter')
 
# Then Steps
@then(parsers.parse('results are shown for "{phrase}"'))
def search_results(page, phrase):
    # Check search phrase
    assert page.locator('#search_form_input').get_attribute('value') == phrase
    print(phrase)