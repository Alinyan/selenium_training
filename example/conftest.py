import pytest
import os.path
import json
from fixture.application import Application

fixture = None
conf = None

def load_config(file):
    global conf
    if conf is None:
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), file)) as json_file:
            conf = json.load(json_file)
    return conf

@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    web_conf = load_config(request.config.getoption("--config"))['web']
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, web_conf=web_conf)
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def exit():
        fixture.destroy()
    request.addfinalizer(exit)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--config", action="store", default="config.json")






