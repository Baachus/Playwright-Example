# from playwright.sync_api import sync_playwright

# def run(playwright):
#     # create a chromium browser instance
#     chromium = playwright.chromium
#     browser = chromium.launch()

#     # create two isolated browser contexts
#     user_context = browser.new_context()
#     admin_context = browser.new_context()

#     # create pages and interact with contexts independently
#     page = user_context.page
#     page.goto("/clientdelay")
#     page.click(".btn-primary")
#     assert page.inner_text(".bg-success")=="Data calculated on the client side."


# async def test_browser_channels(browser):
#     with sync_playwright() as playwright:
#         run(playwright)
        