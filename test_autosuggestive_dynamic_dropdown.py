import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def test_e2e():
 #service_obj = Service("/Users/baba/PycharmProjects/chromedriver")
 #driver = webdriver.Chrome(service=service_obj)
 options = webdriver.ChromeOptions()
 driver = webdriver.Chrome(options=options)


 driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
 driver.find_element(By.ID, "autosuggest").send_keys("uni")
 time.sleep(2)
 countries = driver.find_elements(By.XPATH, "//li[@class = 'ui-menu-item']/a")
 for country in countries:
    if country.text == "United Kingdom (UK)":
        country.click()
        break
 print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))
 assert driver.find_element(By.ID, "autosuggest").get_attribute("value").__contains__("UK")
 time.sleep(2)
