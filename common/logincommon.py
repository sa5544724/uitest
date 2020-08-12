from selenium import webdriver
from selenium.webdriver.common.by import By
#driver初始化
def set_driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(url='http://60.205.168.160:8000')
    return driver
#登录
def get_login(driver,usename,password):
    driver.find_element(By.XPATH, '//input[@placeholder="请输入邮箱"]').send_keys(usename)
    driver.find_element(By.XPATH, '//input[@placeholder="请输入密码"]').send_keys(password)
    driver.find_element(By.XPATH, '//span[text()="登录"]').click()