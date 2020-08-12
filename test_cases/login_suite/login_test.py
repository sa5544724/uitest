import time
from selenium import webdriver
import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common import logincommon
class LuChengLoginTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=logincommon.set_driver()
    def tearDown(self) -> None:
        self.driver.quit()

    def test_Login01(self):
        '''输入正确的邮箱和密码，点击登录按钮'''
        logincommon.get_login(self.driver,'lcsuoadmin','lcsuo123456')
        a=self.driver.find_element_by_xpath('//a[text()="首页"]').text
        self.assertEqual('首页',a,'登录失败')
        # self.assertTrue(EC.text_to_be_present_in_element((By.XPATH,'//a[text()="首页"]'),'首页111'))

    def test_Login02(self):
        '''邮箱不填，填入密码，点击登录按钮'''
        logincommon.get_login(self.driver,'','lcsuo123456')
        time.sleep(2)
        a = self.driver.find_element_by_xpath('//div[contains(text(),"请输入邮箱")]').text
        self.assertEqual('请输入邮箱',a,'邮箱不填，没有给出报错信息')

    def test_Login03(self):
        '''密码不填，填入邮箱，点击登录按钮'''
        logincommon.get_login(self.driver, 'lcsuoadmin', '')
        time.sleep(2)
        a = self.driver.find_element(By.XPATH,'//div[contains(text(),"请输入密码")]').text
        self.assertEqual('请输入密码',a,'密码不填，没有给出报错信息')
    #
    def test_Login04(self):
        '''登录成功后退出登录'''
        logincommon.get_login(self.driver, 'lcsuoadmin', 'lcsuo123456')
        self.driver.find_element(By.XPATH,'//span[contains(text(),"退出")]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div[4]/div/div[3]/span/button[1]/span').click()
        a = self.driver.find_element(By.XPATH,'//a[contains(text(),"忘记密码")]').text
        self.assertEqual('忘记密码',a,'退出登录操作失败')
    def test_05(self):
        '''点击忘记密码，跳转至密码重置页'''
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/form/div[3]/div/a').click()
        time.sleep(2)
        a = self.driver.find_element(By.XPATH,'//span[contains(text(),"直接登录")]').text
        self.assertEqual('直接登录',a,'跳转至密码重置页失败')

if __name__ =='__main__':
    unittest.main(verbosity=2)




