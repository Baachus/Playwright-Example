import pandas as pd
import pytest as pt
from intercept_model import Intercept

def test_intercept_request(page):
    """
    This test
    """
    obj = Intercept(page)

    obj.click(Intercept.search_input)
