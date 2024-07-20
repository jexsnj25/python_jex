import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("/Users/baba/PycharmProjects/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(5)
driver.find_element(By.XPATH, "//input[@placeholder='Search for Vegetables and Fruits']").send_keys("ber")

results = driver.find_elements(By.XPATH, "//div[@class ='product']")
print(len(results))
assert len(results) > 0
for result in results:
    # Chaning the webelements
    result.find_element(By.XPATH, "div/button[text()='ADD TO CART']").click()
driver.find_element(By.XPATH, "//a[@class ='cart-icon']").click()
driver.find_element(By.XPATH, "//button[text() = 'PROCEED TO CHECKOUT']").click()

# sum of the total
prices = driver.find_elements(By.XPATH, "//tr/td[5]/p")
Total = 0
for price in prices:
    Total = Total + int(price.text)
Total_amount = int(driver.find_element(By.XPATH, "//span[@class ='totAmt']").text)
assert Total == Total_amount
print(Total)
print(driver.find_element(By.XPATH, "//span[@class ='totAmt']").text)

driver.find_element(By.XPATH, "//input[@class ='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH, "//button[text()='Apply']").click()
# explcit wait till the condition is met
# https://stackoverflow.com/questions/38038920/visibilityofelementlocated-vs-presenceofelementlocated
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//span[@class='promoInfo']")))

print(driver.find_element(By.XPATH, "//span[@class='promoInfo']").text)
