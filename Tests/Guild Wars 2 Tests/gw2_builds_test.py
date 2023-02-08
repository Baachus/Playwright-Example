import pandas as pd
import pytest as pt
from gw2_model import GuildWars2

def test_retrieve_all_builds(page):
    """
    This test navigates to guildjen and retrieves all builds for the 6
    areas of guild wars 2.  It then stores this data in a data frame
    for later use.
    """
    # Dictionary of types of builds and the image link to click on the 
    # homepage
    obj = GuildWars2(page)

    names = {
        "PvP Builds": obj.pvp_builds, 
        "WvW Builds": obj.wvw_builds, 
        "Raid Builds": obj.raid_builds, 
        "Open World Builds": obj.open_world_builds, 
        "Strike Mission Builds": obj.strike_builds, 
        "Fractal Builds": obj.fractal_builds,
        }

    #Data frame to store all information
    final_df = pd.DataFrame()

    #loop through all keys in the dictionary
    for spot in names:
        obj.navigate_builds()
        page.click(names[spot])
        assert page.inner_text(obj.page_title)==spot

        temp = get_Builds(page, spot)
        final_df = pd.concat([final_df, temp])

    print(final_df)

def get_Builds(page, title):
    """
    Method retrieves all names and links for the build and places the
    title that is sent in.  It takes this data and forms a data frame.

    returns - DataFrame of the data.
    """
    obj = GuildWars2(page)
    buildLinks = page.eval_on_selector_all(obj.build_links,
        "elements => elements.map(element => element.href)")
        
    buildNames = page.eval_on_selector_all(obj.build_links, 
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