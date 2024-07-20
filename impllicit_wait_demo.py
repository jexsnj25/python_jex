import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/baba/PycharmProjects/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(5)  # Implicit wait will have max time out of 5 seconds for any element to load
driver.find_element(By.XPATH, "//input[@placeholder='Search for Vegetables and Fruits']").send_keys("ber")

results = driver.find_elements(By.XPATH, "//div[@class ='product']")
print(len(results))
assert len(results) > 0
for result in results:
    # Chaning the webelements
    result.find_element(By.XPATH, "div/button[text()='ADD TO CART']").click()
driver.find_element(By.XPATH, "//a[@class ='cart-icon']").click()
driver.find_element(By.XPATH, "//button[text() = 'PROCEED TO CHECKOUT']").click()

driver.find_element(By.XPATH, "//input[@class ='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH, "//button[text()='Apply']").click()

print(driver.find_element(By.XPATH, "//span[@class='promoInfo']").text)
