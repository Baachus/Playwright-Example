This project is a sample automation framework utilizing pytest for test automation.  It utilizes Playwright for front end testing, but also has the capabilities of 
middle and backend testing if needed.  It is being utilized for testing out test automation in python and its capabilities.

To run the tests in a terminal just run "pytest", this can be modified or changed in your pytest.ini file for any extra cli limitations you want on these.
    *useful change is "pytest -k 'test name'" to run a specific test by itself

To have this run you must install the following items utilizing Pip or your favorite install:
    pytest (testing framework) - pip install pytest
    playwright (web driver) - pip install pytest-playwright
    faker (generator of random fake data) - pip install Faker
    Beautiful Soup (html parser) - pip install beautifulsoup4
    Pandas (Data framework for storing data) - pip install pandas
    Pyodc (odb connections for database manipulation) - pip install pyodc
    Pytest Assertions (assertions for test verifications) - pip install pytest-assertions
    Pytest Concurrent (multiple threads running at the same time) - pip install pytest-concurrent