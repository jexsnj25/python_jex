import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/baba/PycharmProjects/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.XPATH, "//input[@name ='enter-name']").send_keys("Jeck")
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
time.sleep(2)
assert "Jeck" in alertText
alert.accept()
# alert.dismiss()
