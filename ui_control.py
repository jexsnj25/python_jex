import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/baba/PycharmProjects/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkbox = driver.find_elements(By.XPATH,"//input[@type ='checkbox']")

for chk in checkbox:
    if chk.get_attribute("value") == "option2":
        chk.click()
        assert chk.is_selected()
        break

radiobuttons = driver.find_elements_by_name("radioButton")
radiobuttons[2].click()
assert radiobuttons[2].is_selected()


assert driver.find_element_by_id("displayed-text").is_displayed()
driver.find_element_by_id("hide-textbox").click()
assert not driver.find_element_by_id("displayed-text").is_displayed()




# Passing value to xpath
# value = driver.find_element(By.XPATH, "//input[@value ='option2']").get_attribute("value")
# driver.find_element(By.XPATH, "//input[@value ='"+value+"']").click()


time.sleep(2)
