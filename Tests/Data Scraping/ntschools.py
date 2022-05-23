import scrapy

class School_Spider(scrapy.Spider):
    """
    Data scraping of a school directory.  It searches each school and 
    identifies their name, telephone, email, address, and postal code.
    This also utilizes scrapy as a scraping tool and must be run in CLI
    with the command 'scrapy runspider ntschools.py -o all_schools.csv'
    which will run scrapy and put all outputs into a CSV file called
    all_schools.csv.
    """
    #start_urls sets the base url to start with to get the cookie.
    name="all"
    start_urls = ["https://directory.ntschools.net/#/schools"] 

    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,hi;q=0.8,lb;q=0.7",
        "Referer": "https://directory.ntschools.net/",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "+
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+
                "79.0.3945.130 Safari/537.36",
        "X-Requested-With": "Fetch",
    }

    def parse(self, response):
        """Sends a request with the base URL"""
        yield scrapy.Request(
            url="https://directory.ntschools.net/api/System/GetAllSchools",
            callback=self.parse_all_schools,
            headers=self.headers
        )

    def parse_all_schools(self, response):
        """Parses the url for all schools."""
        data = response.json()

        for i,school in enumerate(data):
            school_code = school["itSchoolCode"]
            yield scrapy.Request(
                f"https://directory.ntschools.net/api/System/GetSchool?"+
                    "itSchoolCode={school_code}",
                callback=self.parse_school,
                headers=self.headers,
                # Many schools have the same code, but listed more than once
                dont_filter=True 
            )

    def parse_school(self, response):
        """Parses the specific request for a specific school."""
        data = response.json() 
        yield {
            "Name" : data["name"],
            "Telephone Number" : data["telephoneNumber"],
            "E-Mail" : data["mail"],
            "Physical Address" : data["physicalAddress"]["displayAddress"],
            "Postal Address" : data["postalAddress"]["displayAddress"],
        }