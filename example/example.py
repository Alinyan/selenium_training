# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Ie()
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("http://www.google.com")
    driver.close()

