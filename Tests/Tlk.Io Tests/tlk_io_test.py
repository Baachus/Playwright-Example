from tlkio_model import TlkIo

def test_tlk_io(page):
    """
    This test 
    """
    obj = TlkIo(page)

    #basic navigation to site and search
    page.goto(obj.tlkio_url)

    #navigate to the chat channel and verify you are in the right one
    page.fill(obj.channel_selection, 'Testing_Automation')
    page.locator(obj.channel_join).click()  
    page.wait_for_load_state("networkidle"); # This waits for the "networkidle" this page loads oddly
    
    assert page.inner_text(obj.channel_header)=="testing_automation"

