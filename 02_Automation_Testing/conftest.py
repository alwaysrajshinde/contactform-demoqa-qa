import json, pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope='session')
def config():
    with open('config/config.json') as f:
        return json.load(f)

@pytest.fixture
def driver(config):
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1366,768')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(config['implicit_wait'])
    driver.get(config['base_url'])
    yield driver
    driver.quit()
