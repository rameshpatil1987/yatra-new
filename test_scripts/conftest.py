import allure
import pytest
from allure_commons.types import AttachmentType
from pyjavaproperties import Properties
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions
@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="failed_tests", attachment_type=AttachmentType.PNG)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope="class")
def setup(request):
    global driver
    pfile = Properties()
    try:
        pfile.load(open("config.properties"))
    except:
        pfile.load(open("../config.properties"))
    url = pfile['url']
    browser = pfile['browser']
    use_grid=pfile['use_grid']
    grid_url=pfile['grid_url']
    if use_grid == "no":
        if browser == 'chrome':
            driver = webdriver.Chrome()
            print("Launched chrome browser in local system")
        else:
            driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
            print("Launched firefox browser in local system")
    else:
        if browser == "chrome":
            browser_options=ChromeOptions()
            print("Launched chrome browser in remote system")
        else:
            browser_options=FirefoxOptions()
            print("Launched firefox browser in remote system")
        driver=webdriver.Remote(grid_url,options=browser_options)
    driver.maximize_window()
    driver.get(url)
    request.cls.driver=driver
    yield
    driver.close()
