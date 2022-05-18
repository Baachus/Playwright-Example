import os
import pytest

from enum import auto
from typing import Generator
from playwright.sync_api import Playwright, Page, APIRequestContext, expect

@pytest.fixture(scope="session")
def api_request_context(
    playwright: Playwright,
) -> Generator[APIRequestContext, None, None]:
    """
    This method generates an api request context.  It sets the header
    information, request contexts, and disposes of the request
    """
    #Before Tests
    headers = {
    }
    request_context = playwright.request.new_context(
        base_url="https://catfact.ninja", extra_http_headers=headers,
    )
    yield request_context
    #After Tests
    request_context.dispose()

def test_verify_max_length_cat_fact(api_request_context: APIRequestContext) -> None: 
    """
    This test calls the api of catfact.ninja and retrieves a single fact
    and verifies its length is less than the max length sent in.
    """
    cat_response = api_request_context.get(f"/fact", params={"max_length":"100"})
    assert cat_response.ok
    cat_response_json = cat_response.json()
    assert cat_response_json["length"] > 0 and cat_response_json["length"] < 101

def test_all_cat_facts(api_request_context: APIRequestContext) -> None:
    """
    This test calls the api of catfact.ninja and retrieves all cat facts
    and verifies the response comes back ok.
    """
    cat_response = api_request_context.get(f'/facts')
    assert cat_response.ok