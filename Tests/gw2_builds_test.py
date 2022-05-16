import pandas as pd
import pytest as pt

def test_retrieve_all_builds(page):
    """
    This test navigates to guildjen and retrieves all builds for the 6
    areas of guild wars 2.  It then stores this data in a data frame
    for later use.
    """
    # Dictionary of types of builds and the image link to click on the 
    # homepage
    names = {
        "PvP Builds": "a[data-id='12412']>img", 
        "WvW Builds": "a[data-id='12416']>img", 
        "Raid Builds": "a[data-id='22312']>img", 
        "Open World Builds": "a[data-id='23070']>img", 
        "Strike Mission Builds": "a[data-id='23146']>img", 
        "Fractal Builds": "a[data-id='23329']>img",
        }

    #Data frame to store all information
    final_df = pd.DataFrame()

    #loop through all keys in the dictionary
    for spot in names:
        page.goto('https://guildjen.com/builds/')
        page.click(names[spot])
        assert page.inner_text(".entry-title")==spot
        
        temp = get_Builds(page, spot)
        df = pd.concat([final_df, temp])

    print(final_df)

def get_Builds(page, title):
    """
    Method retrieves all names and links for the build and places the
    title that is sent in.  It takes this data and forms a data frame.

    returns - DataFrame of the data.
    """
    buildLinks = page.eval_on_selector_all("a[href$='-build/']", 
        "elements => elements.map(element => element.href)")
        
    buildNames = page.eval_on_selector_all("a[href$='-build/']", 
        "elements => elements.map(element => element.text)")
    
    # Number of links and names should match if not something is wrong 
    # and the test will fail
    if(len(buildLinks)!=len(buildNames)):
        pt.fail("Links and names does not match.")

    final_builds = []

    for builds in range(len(buildLinks)):
        build = {
            "Type": title,
            "Name": buildNames[builds],
            "Link": buildLinks[builds],
        }
        final_builds.append(build)

    return pd.DataFrame(final_builds)