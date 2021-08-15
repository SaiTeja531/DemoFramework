import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture(scope="class")
def setup(request):
    browser = request.config.getoption("browser")
    # Opening web browser
    if browser == "firefox":
        driver = webdriver.Firefox()
        driver.maximize_window()
    elif browser == "chrome":
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.maximize_window()
    elif browser == "edge":
        driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
        driver.maximize_window()

    driver.get("http://tutorialsninja.com/demo/")
    wait = WebDriverWait(driver, 10)
    actions = ActionChains(driver)
    request.cls.driver = driver
    request.cls.wait = wait
    request.cls.actions = actions
    # closing browser
    yield
    driver.close()
