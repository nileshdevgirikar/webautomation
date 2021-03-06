import pytest
from base.WebDriverFactory import WebDriverFactory

@pytest.yield_fixture( scope="class" )
def SetUp():
    print( "Running method level setUp" )
    yield
    print( "Running method level tearDown" )

@pytest.yield_fixture()
def oneTimeSetUp(request, browser):
    print("Running method level setUp")

    global driver
    wdf = WebDriverFactory( browser )
    driver = wdf.getWebDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.close()
    print("Running method level tearDown")

def pytest_addoption(parser):
    parser.addoption( "--browser" )
    parser.addoption( "--osType", help="Type of operating system" )

@pytest.fixture( scope="session" )
def browser(request):
    return request.config.getoption( "--browser" )

@pytest.fixture( scope="session" )
def osType(request):
    return request.config.getoption( "--osType" )
