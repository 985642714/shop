import time
from selenium import webdriver

abc = "123456"
print(abc)

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
time.sleep(2)
driver.quit()
