import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/baba/PycharmProjects/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
action = ActionChains(driver)
#action.click_and_hold()
#action.double_click()
#action.context_click()
#action.drag_and_drop()
action.move_to_element(driver.find_element(By.XPATH, "//button[@id ='mousehover']")).perform()
#action.context_click(driver.find_element(By.XPATH, "//button[@id ='mousehover']")).perform()
action.click(driver.find_element(By.LINK_TEXT,"Top")).perform()
