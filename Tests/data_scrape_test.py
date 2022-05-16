import pytest
#pandas is used for data frames
import pandas as pd
#requets used for direct requests to the pages
import requests

#Soup used for parsing data retrieved from requests
from bs4 import BeautifulSoup

#mark to skip test unless absolutely wanting to run it takes a while
@pytest.mark.skip(reason="This test takes a long time only run if needed.")
# Author - Robert Chapin
# Date Created - 5/11/2022
# This test navigates to the whiskey exchange website then scrapes all 
# single malt scotch whiskies available and gets their name, price, 
# description, star review, and number of user reviews.  It stores this
# data in a panda data frame for ease of use.
def test_data_scrape():
    baseUrl = 'https://www.thewhiskyexchange.com'

    # utilizes a defaulted user agent so the website doesn't block to 
    # many requests from python.  More can be found -
    # https://developers.whatismybrowser.com/useragents/explore/software_type_specific/web-browser/2
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/"
            +"537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
    }

    #array used to store all the links that were scrapped
    productlinks = []
    #array to store all the whiskey information
    whiskeylist = []

    #Retrieve the number of pages
    r = requests.get('https://www.thewhiskyexchange.com/c/40/single-malt-'
                    +'scotch-whisky?pg=1')
    soup = BeautifulSoup(r.content, 'html.parser')
    numOfPages = int(
        soup.find('nav', class_='paging js-paging')['data-totalpages'].strip()
        )

    # loop through all pages and get all the product links and store
    # them in the array productlinks
    for x in range(1,numOfPages):
        r = requests.get(f'https://www.thewhiskyexchange.com/c/40/single-'
                        +'malt-scotch-whisky?pg={x}')
        soup = BeautifulSoup(r.content, 'html.parser')
        productlist = soup.find_all('li', class_='product-grid__item')

        for item in productlist:
            for link in item.find_all('a', href=True):
                productlinks.append(baseUrl + link['href'])

    #loop through all links in product link and get all whiskey information    
    for link in productlinks:
        r = requests.get(link, headers=headers)
        soup = BeautifulSoup(r.content, 'html.parser')

        #Retrieve Names
        try:
            name = soup.find('h1', 
                class_='product-main__name').text.strip()
        except:
            name = soup.find('p', 
                class_='whiskylabels-intro__classification').text.strip()

        #Retrieve Prices
        try:
            price = soup.find('p', 
                class_='product-action__price').text.strip()
        except:
            price = soup.find('p', 
                class_='whiskylabels-intro__price').text.strip()
        
        #Retrieve descriptions
        try:
            description = soup.find('div',
                class_='product-main__description').text.strip()
        except:
            description = soup.find('p', 
                class_='whiskylabels-content__copy').text.strip()

        #Retrieve star ratings
        try:
            starRating = soup.find('span', 
                class_='star-rating').text.strip()
        except:
            starRating = "no rating"

        #Retrieve number of reviews
        try:
            numOfReviews = soup.find('span', 
                class_='review-overview__count').text.strip()
        except:
            numOfReviews = "no reviews"

        #store whiskey information in a whiskey object
        whiskey = {
            'Name':name,
            'Price':price,
            'Star Rating':starRating,
            'Number of Reviews':numOfReviews,
            'Description':description,
            }
        whiskeylist.append(whiskey)

    # store all information on the whiskeylist array into a data frame 
    # for easier maniuplation later
    df = pd.DataFrame(whiskeylist)
    print(df)