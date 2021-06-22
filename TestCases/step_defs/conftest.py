import os
import random
import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    dir_path = os.path.dirname(os.path.abspath(__file__)) + "\..\.."
    driver_path = dir_path + "\Drivers\chromedriver.exe"
    print(driver_path)
    b = webdriver.Chrome(driver_path)
    b.implicitly_wait(20)
    b.maximize_window()
    yield b
    b.quit()


@pytest.fixture
def project_name():
    return str(random.random()) + "project"
