import os
import pytest

from enum import auto
from typing import Generator
from playwright.sync_api import Playwright, Page, APIRequestContext, expect

#Test fixture to setup requets
@pytest.fixture(scope="session")
    #Execute before tests
def api_request_context(
    playwright: Playwright,
) -> Generator[APIRequestContext, None, None]:
    headers = {
    }
    request_context = playwright.request.new_context(
        base_url="https://catfact.ninja", extra_http_headers=headers,
    )
    yield request_context
    #After Tests
    request_context.dispose()

# Author - Robert Chapin
# Date Created - 5/11/2022
# This test calls the api of catfact.ninja and retrievse a single fact 
# and verifies its length is less than max length sent in
def test_verify_max_length_cat_fact(api_request_context: APIRequestContext) -> None: 
    catResponse = api_request_context.get(f"/fact", params={"max_length":"100"})
    assert catResponse.ok
    catResponseJson = catResponse.json()
    assert catResponseJson["length"] > 0 and catResponseJson["length"] < 101

# Author - Robert Chapin
# Date Created - 5/11/2022
# This test calls the api of catfact.ninja and retrievse all cat facts 
# and verifies the response comes back ok
def test_all_cat_facts(api_request_context: APIRequestContext) -> None:
    catResponse = api_request_context.get(f'/facts')
    assert catResponse.ok