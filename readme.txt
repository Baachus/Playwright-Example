This project is a sample automation framework utilizing pytest for test automation.  It utilizes Playwright for front end testing, but also has the capabilities of 
middle and backend testing if needed.  It is being utilized for testing out test automation in python and its capabilities.

To run the tests in a terminal just run "pytest", this can be modified or changed in your pytest.ini file for any extra cli limitations you want on these.
    *useful change is "pytest -k 'test name'" to run a specific test by itself

This project utilizes Python 3.10  (choco install python3 --pre)

The Gherkin extension is installed in visual studio code for ease of reading feature files for BDD test cases.
The Python extension is installed in visual studio code for coding in python within visual studio code.

update syspaths are added on m-paths.pth (this is under the sandbox-env->lib->site-packages)
    (may be hidden in vs code under preferences->Files->Exclude)
    
To upgrade packages run - (pip-review --local --auto)

pip List in Sandbox Environment (pip list)

Allure is installed for reporting and bin is located in Environment Variable path.  To generate report after run type "allure serve Reports/"