from bs4 import BeautifulSoup

# Author - Robert Chapin
# Date Created - 5/11/2022
# This test utilizes beautiful soup to parse information from a page 
# and get all h2 links on the page categoriezed with class pull-right
def test_open_cart_find_total_orders(page):
    #utilizes a url different than default page
    page.goto("https://demo.opencart.com/admin")
    page.fill("#input-username", "demo")
    page.fill("#input-password", "demo")
    page.click("button[type=submit]")
    page.is_visible("div.tile-body")
    html = page.inner_html("#content")
    soup = BeautifulSoup(html, 'html.parser')
    total_orders = soup.find('h2', {'class':'pull-right'}).text
    print(f'total orders = {total_orders}')