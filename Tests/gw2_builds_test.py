import pandas as pd
import pytest

def test_retrieve_all_builds(page):
    
    names = {"PvP Builds": "a[data-id='12412']>img", 
            "WvW Builds": "a[data-id='12416']>img", 
            "Raid Builds": "a[data-id='22312']>img", 
            "Open World Builds": "a[data-id='23070']>img", 
            "Strike Mission Builds": "a[data-id='23146']>img", 
            "Fractal Builds": "a[data-id='23329']>img"}

    df = pd.DataFrame()

    for spot in names:
        page.goto('https://guildjen.com/builds/')
        page.click(names[spot])
        assert page.inner_text(".entry-title")==spot
        
        temp = get_Builds(page, pd.DataFrame(), spot)
        df = pd.concat([df, temp])

    print(df)

# Method to generate builds based upon links on the page - returns a data frame
def get_Builds(page, df, title):
    buildLinks = page.eval_on_selector_all("a[href$='-build/']", "elements => elements.map(element => element.href)")
    buildNames = page.eval_on_selector_all("a[href$='-build/']", "elements => elements.map(element => element.text)")
    
    if(len(buildLinks)!=len(buildNames)):
        pytest.fail("Links and names does not match.")

    finalBuilds = []

    for builds in range(len(buildLinks)):
        build = {
            "Type": title,
            "Name": buildNames[builds],
            "Link": buildLinks[builds]
        }
        finalBuilds.append(build)

    return pd.DataFrame(finalBuilds)