class TlkIo:
    def __init__(self, page):
        self.page = page

        self.tlkio_url = "https://tlk.io"
        self.channel_selection = "id=chat_permalink"
        self.channel_join = "id=join_button"

        #joined channel
        self.channel_header = "id=channel"
        self.message_body = "id=message_body"
        self.user_count = "id=user-counter"
        self.users = "id=online-participants"