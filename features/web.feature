#Move feature folder under tests for this to execute - removed due to issues with multiple browsers running as pytest-bdd can only utilize one browser
#Move bdd_test.py to Tests folder at the same level as the features folder also
@web @duckduckgo
Feature: DuckDuckGo Web Browsing
  As a web surfer,
  I want to find information online,
  So I can learn new things and get tasks done.

  Scenario: Basic DuckDuckGo Search
    Given the DuckDuckGo home page is displayed
    When the user searches for "panda"
    Then results are shown for "panda"
    
  Scenario: Basic DuckDuckGo Search for tests
    Given the DuckDuckGo home page is displayed
    When the user searches for "tests"
    Then results are shown for "tests"
    
  Scenario: Basic DuckDuckGo Search for automation
    Given the DuckDuckGo home page is displayed
    When the user searches for "automation"
    Then results are shown for "automation"