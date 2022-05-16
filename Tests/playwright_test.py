# To run tests use pytest in terminal or 
# pytest -n (Number of parallel tests)
import os

# Author - Robert Chapin
# Date Created - 5/11/2022
# First test created by playwright, it navigates to default page and 
# clicks button link than navigates back
def test_click(page):
    page.goto("/")
    page.click("text=Click")
    page.click("#badButton")
    
# Author - Robert Chapin
# Date Created - 5/11/2022
# This test navigates to a page by utilizing the xpath
def test_xPath(page):
    page.goto("/")
    page.click("//*[@id='overview']/div/div[2]/div[4]/h3/a")

# Author - Robert Chapin
# Date Created - 5/11/2022
# This test navigates to the load delay link which takes 15seconds to 
# load and returns
def test_load_delay(page):
    page.goto("/")
    page.click("text=Load Delay") 
    page.click(".btn") 

# Author - Robert Chapin
# Date Created - 5/11/2022
# This test navigates to the client side delay link which takes 15
# seconds to load and verifies client data is loaded after the delay
def test_client_side_delay(page):
    page.goto("/clientdelay")
    page.click(".btn-primary")
    assert page.inner_text(".bg-success")=="Data calculated on the client side."

# Author - Robert Chapin
# Date Created - 5/11/2022
# This test enters value into a text field and verifies a button is 
# updated with that text
def test_text_input(page):
    page.goto("/textinput")
    page.fill("#newButtonName", "Test Name")
    page.click("#updatingButton")
    assert page.inner_text("#updatingButton") == "Test Name"

# Author - Robert Chapin
# Date Created - 5/11/2022
# This test selects a button hidden by scroll bars
def test_scroll_bars(page):
    page.goto("/scrollbars")
    page.click("#hidingButton")

# Author - Robert Chapin
# Date Created - 5/11/2022
# This test attempts to log into a page but fails and verifies warning 
# appears
def test_login_fail(page):
    page.goto("/sampleapp")
    page.fill('//input[@placeholder="User Name"]', 'Baachus')
    page.click("#login")
    assert page.inner_text("#loginstatus") == "Invalid username/password"

# Author - Robert Chapin
# Date Created - 5/11/2022
# This test logs into a website and logs back out
def test_login_logout(page):
    #login
    page.goto("/sampleapp")
    page.fill('//input[@placeholder="User Name"]', 'Baachus')
    page.fill('//input[@name="Password"]', "pwd")
    page.click("#login")
    assert page.inner_text("#loginstatus") == "Welcome, Baachus!"

    #logout
    page.click("#login")
    assert page.inner_text("#loginstatus") == "User logged out."

# Author - Robert Chapin
# Date Created - 5/11/2022
# This test can click a link which has a non-breaking space inside it 
# between My and Button
def test_non_breaking_space(page):
    page.goto("/nbsp")
    page.click("text=My Button")

# Author - Robert Chapin
# Date Created - 5/11/2022
# This test starts a progress bar and attempts to stop at 75% loaded.  
# It expects to hit it within 10 seconds but if it goes over it will 
# fail.
def test_progress_bar(page):
    page.goto("/progressbar")
    page.click('#startButton')
    page.inner_text("#progressBar[aria-valuenow='75']")
    page.click('#stopButton')
    result = page.inner_text("#result")
    resultLength = int(result[len(result)-1])
    if (resultLength>10 or resultLength<0):
        print(f'Result length when stopped was over or under 75% by '
            + '{str(resultLength)}%')
    assert all(["Result: " in result, resultLength>=0, resultLength<=10])
    

