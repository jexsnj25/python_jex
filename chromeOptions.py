import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions
chrome_options.add_argument("--kiosk")
#service_obj = Service("/Users/baba/PycharmProjects/chromedriver")
driver = webdriver.Chrome(executable_path ="/Users/baba/PycharmProjects/chromedriver", options=chrome_options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")