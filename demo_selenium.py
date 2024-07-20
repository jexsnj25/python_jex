import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


service_obj = Service("/Users/baba/PycharmProjects/chromedriver")
driver = webdriver.Chrome(service=service_obj)

# driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")

time.sleep(2)
