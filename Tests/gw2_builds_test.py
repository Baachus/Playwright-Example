import pandas as pd
import pytest

def test_retrieve_all_builds(page):
    
    #PvP Builds
    page.goto('https://guildjen.com/builds/')
    page.click("a[data-id='12412']>img")
    assert page.inner_text(".entry-title")=="PvP Builds"

    df = get_Builds(page, pd.DataFrame(), "PvP Builds")

    #WvW Builds
    page.goto('https://guildjen.com/builds/')
    page.click("a[data-id='12416']>img")
    assert page.inner_text(".entry-title")=="WvW Builds"

    df = get_Builds(page, df, "WvW Builds")

    #Raid Builds
    page.goto('https://guildjen.com/builds/')
    page.click("a[data-id='22312']>img")
    assert page.inner_text(".entry-title")=="Raid Builds"

    df = get_Builds(page, df, "Raid Builds")

    #World PvE Builds
    page.goto('https://guildjen.com/builds/')
    page.click("a[data-id='23070']>img")
    assert page.inner_text(".entry-title")=="Open World Builds"

    df = get_Builds(page, df, "Open World Builds")

    #Strike Mission Builds
    page.goto('https://guildjen.com/builds/')
    page.click("a[data-id='23146']>img")
    assert page.inner_text(".entry-title")=="Strike Mission Builds"

    df = get_Builds(page, df, "Strike Mission Builds")

    #Fractal Builds
    page.goto('https://guildjen.com/builds/')
    page.click("a[data-id='23329']>img")    
    assert page.inner_text(".entry-title")=="Fractal Builds"

    df = get_Builds(page, df, "Fractal Builds")
    
    #Print out Data Frame
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

    newdf = pd.DataFrame(finalBuilds)
    return pd.concat([df, newdf])