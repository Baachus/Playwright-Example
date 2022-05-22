class GuildWars2:
    def __init__(self, page):
        self.page = page

        self.gw2_url = "https://guildjen.com"

        self.page_title = ".entry-title"
        self.build_links = "a[href$='-build/']"

        #build links
        self.pvp_builds = "a[data-id='12412']>img"
        self.wvw_builds = "a[data-id='12416']>img"
        self.raid_builds = "a[data-id='22312']>img"
        self.open_world_builds = "a[data-id='23070']>img"
        self.strike_builds ="a[data-id='23146']>img"
        self.fractal_builds = "a[data-id='23329']>img"

        #social media links
        self.youtube_link = "img[title='Youtube']"
        self.twitter_link = "img[title='Twitter']"
        self.discord_link = "img[title='Discord']"
        self.facebook_link = "img[title='Facebook']"
        self.instagram_link = "img[title='Instagram']"
        self.steam_link = "img[title='Steam']"

    def navigate(self):
        self.page.goto(self.gw2_url)
    def navigate_builds(self):
        self.page.goto(self.gw2_url+"/builds/")