import time

abc = "123456"
print(abc)
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
time.sleep(2)
driver.quit()