# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
#
# chrome_options = webdriver.ChromeOptions()
# # NO browser will be opened, execution will happen without opening the browser
# chrome_options.add_argument('--headless')
# # will handle certification error , advance option - proceed anyway
# chrome_options.add_argument('--ignore-certificate-errors')
#
# service_obj = Service("/Users/rahulshetty/documents/chromedriver")
# driver = webdriver.Chrome(service=service_obj, options=chrome_options)
# driver.implicitly_wait(2)
#
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
# driver.get_screenshot_as_file("screen.png")

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
#
# # Define the path to the ChromeDriver executable
# #chrome_driver_path = "/Users/rahulshetty/documents/chromedriver"
#
# # Set up Chrome service
# service = Service("/Users/rahulshetty/documents/chromedriver")
#
# # Define Chrome options
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--ignore-certificate-errors')
# 
# # Create WebDriver instance
# driver = webdriver.Chrome(service=service, options=chrome_options)


