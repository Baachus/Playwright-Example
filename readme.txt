This project is a sample automation framework utilizing pytest for test automation.  It utilizes Playwright for front end testing, but also has the capabilities of 
middle and backend testing if needed.  It is being utilized for testing out test automation in python and its capabilities.

To run the tests in a terminal just run "pytest", this can be modified or changed in your pytest.ini file for any extra cli limitations you want on these.
    *useful change is "pytest -k 'test name'" to run a specific test by itself

This project utilizes Python 3.10  (choco install python3 --pre)

The Gherkin extension is installed in visual studio code for ease of reading feature files for BDD test cases.
The Python extension is installed in visual studio code for coding in python within visual studio code.

update syspaths are added on m-paths.pth (this is under the sandbox-env->lib->site-packages)

To upgrade packages run - (pip-review --local --auto)

pip List in Sandbox Environment (pip list):
    Package               Version
    --------------------- -----------
    ansi2html             1.7.0
    atomicwrites          1.4.0
    attrs                 21.4.0
    beautifulsoup4        4.11.1
    bs4                   0.0.1
    certifi               2022.5.18.1
    cffi                  1.15.0
    chardet               4.0.0
    charset-normalizer    2.0.12
    colorama              0.4.4
    docutils              0.18.1
    execnet               1.9.0
    Faker                 13.11.1
    glob2                 0.7
    greenlet              1.1.2
    htmlmin               0.1.12
    idna                  3.3
    iniconfig             1.1.1
    Jinja2                3.1.2
    Mako                  1.2.0
    MarkupSafe            2.1.1
    numpy                 1.22.4
    packaging             21.3
    pandas                1.4.2
    parse                 1.19.0
    parse-type            0.6.0
    Pillow                9.1.1
    pip                   22.1.1
    pip-review            1.1.1
    playwright            1.22.0
    pluggy                1.0.0
    plyvel-win32          1.3.0
    py                    1.11.0
    pycparser             2.21
    pyee                  9.0.4
    pymssql               2.2.5
    pyodbc                4.0.32
    pyodc                 1.1.2
    pyparsing             3.0.9
    pytest                7.1.2
    pytest-base-url       2.0.0
    pytest-bdd            5.0.0
    pytest-forked         1.4.0
    pytest-playwright     0.3.0
    pytest-reporter       0.5.2
    pytest-reporter-html1 0.8.2
    pytest-slack          2.3.1
    pytest-xdist          2.5.0
    python-dateutil       2.8.2
    python-slugify        6.1.2
    pytz                  2022.1
    requests              2.27.1
    setuptools            62.3.2
    six                   1.16.0
    soupsieve             2.3.2.post1
    text-unidecode        1.3
    tomli                 2.0.1
    typing_extensions     4.2.0
    urllib3               1.26.9
    websockets            10.3