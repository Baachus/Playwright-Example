import os
from the_internet_model import The_Internet

def test_upload_file(page):
    """
    This test navigates to a website which accepts uploading a file.
    It then uploads a sample file and verifies it uploads successfully.
    """
    dirname = os.path.dirname(__file__)
    filePath = os.path.join(dirname, '..\\..\\Sample Files\\recipe.txt')

    obj = The_Internet(page)
    obj.navigate_to_upload()

    page.set_input_files(obj.file_upload, filePath)
    page.click(obj.submit_file)
    assert page.inner_text(obj.uploaded_file) == "recipe.txt"

def test_javascript_alerts(page):
    """
    This test verifies the handling of Javacsript alerts.  It sets the 
    dialog to auto accept any dialog opened.
    """
    obj = The_Internet(page)
    obj.navigate_to_javascipt_alerts()
    
    page.on("dialog", lambda dialog: dialog.accept())

    page.click(obj.js_alert_button)
    assert page.inner_text(obj.result_label) == "You successfully clicked an alert"
    page.click(obj.js_confirm_button)
    assert page.inner_text(obj.result_label) == "You clicked: Ok"
    page.click(obj.js_prompt_button)
    assert page.inner_text(obj.result_label) == "You entered:"