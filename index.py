import time

from selenium import webdriver


def testcase():
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')
    driver.find_element_by_id('kw').send_keys('123')
    time.sleep(2)
    driver.quit()
