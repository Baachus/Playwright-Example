# To run tests use pytest in terminal or 
# pytest -n (Number of parallel tests)
def test_click(page):
    """
    First Test Created
    This test navigates to the default page and clicks the button link
    and navigates back
    """
    page.goto("/")
    page.click("text=Click")
    page.click("#badButton")
    
def test_xPath(page):
    """This test navigates to a page by utilizing the xpath"""
    page.goto("/")
    page.click("//*[@id='overview']/div/div[2]/div[4]/h3/a")

def test_load_delay(page):
    """
    This test navigates to the load delay link which takes 15 seconds
    to load and returns.
    """
    page.goto("/")
    page.click("text=Load Delay") 
    page.click(".btn") 

def test_client_side_delay(page):
    """
    This test navigates to the client side delay link which takes 15 
    seconds to load and verifies client data is loaded after the delay.
    """
    page.goto("/clientdelay")
    page.click(".btn-primary")
    assert page.inner_text(".bg-success")=="Data calculated on the client side."

def test_text_input(page):
    """
    This test enters value into a text field and verifies a button
    is updated with that text.
    """
    page.goto("/textinput")
    page.fill("#newButtonName", "Test Name")
    page.click("#updatingButton")
    assert page.inner_text("#updatingButton") == "Test Name"

def test_scroll_bars(page):
    """This test selects a button hidden by scroll bars."""
    page.goto("/scrollbars")
    page.click("#hidingButton")

def test_login_fail(page):
    """
    This test attempts to log into a page but fails and verifies 
    a warning appears.
    """
    page.goto("/sampleapp")
    page.fill('//input[@placeholder="User Name"]', 'Baachus')
    page.click("#login")
    assert page.inner_text("#loginstatus") == "Invalid username/password"

def test_login_logout(page):
    """This test logs into a website and logs back out."""
    #login
    page.goto("/sampleapp")
    page.fill('//input[@placeholder="User Name"]', 'Baachus')
    page.fill('//input[@name="Password"]', "pwd")
    page.click("#login")
    assert page.inner_text("#loginstatus") == "Welcome, Baachus!"

    #logout
    page.click("#login")
    assert page.inner_text("#loginstatus") == "User logged out."

def test_non_breaking_space(page):
    """
    This test can click a link which has a non-breaking space inside it
    between My and Button.
    """
    page.goto("/nbsp")
    page.click("text=My Button")

def test_progress_bar(page):
    """
    This test starts a progress bar and attempts to stop at 75% 
    loaded.  It expects to hit it within 10 seconds but if it goes 
    over it will fail.
    """
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