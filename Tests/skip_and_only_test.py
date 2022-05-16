import pytest

# Author - Robert Chapin
# Date Created - 5/11/2022
# This test clicks a button on the default page but will be skipped by 
# firefox
@pytest.mark.skip_browser("firefox")
def test_skip_on_firefox(page):
    page.goto("/")
    page.click("text=Click")
    page.click("#badButton")

# Author - Robert Chapin
# Date Created - 5/11/2022
# This test clicks a button on the default page but will be skipped by 
# all browsers but chromium
@pytest.mark.only_browser("chromium")
def test_only_run_on_chrome(page):
    page.goto("/")
    page.click("text=Click")
    page.click("#badButton")