from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("/Users/orue/code/python-code/raw/chromedriver")


def get_driver(url: str):
    # Set Options for browsing
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_argument("disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url=url)

    return driver
