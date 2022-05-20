class The_Internet:
    def __init__(self, page):
        self.page = page

        self.the_internet_url = "https://the-internet.herokuapp.com"

        self.file_upload = "#file-upload"
        self.submit_file = "#file-submit"
        self.uploaded_file = "#uploaded-files"
        self.js_alert_button = "text='Click for JS Alert'"
        self.js_confirm_button = "text='Click for JS Confirm'"
        self.js_prompt_button = "text='Click for JS Prompt'"
        self.result_label = "#result"
    
    def navigate_to_upload(self):
        self.page.goto(self.the_internet_url+"/upload")

    def navigate_to_javascipt_alerts(self):
        self.page.goto(self.the_internet_url+"/javascript_alerts")