#encoding:utf8

import unittest
from selenium import webdriver
from time import sleep



class login(unittest.TestCase):
    def setUp(self):
        #启动浏览器IE
        self.driver=webdriver.Ie()
        ie=self.driver
        #进入登陆界面
        ie.get('http://127.0.0.1/zentaopms/www/user-login.html')
        sleep(5)
        
    def test_login_success(self):
        ie=self.driver
        #定位登陆界面中的账号、密码输入框元素
        element1=ie.find_element_by_css_selector('input#account')
        element2=ie.find_element_by_css_selector('input[name="password"]')
        #分别在两个输入框中输入账号、密码
        element1.send_keys('admin')
        element2.send_keys('123456')
        sleep(5)
        #定位登陆界面中的登陆按钮，并点击按钮
        ie.find_element_by_css_selector('button#submit').click()
        sleep(5)

        #当前用例结果校验
        try:
            ie.find_element_by_partial_link_text('我的地盘')
            result=True
        except:
            result=False

        self.assertTrue(result,'登陆不成功')
        
    def test_login_password_wrong(self):
        ie=self.driver
        #定位登陆界面中的账号、密码输入框元素
        element1=ie.find_element_by_css_selector('input#account')
        element2=ie.find_element_by_css_selector('input[name="password"]')
        #分别在两个输入框中输入账号、密码
        element1.send_keys('admin1')
        element2.send_keys('123')
        sleep(5)
        #定位登陆界面中的登陆按钮，并点击按钮
        ie.find_element_by_css_selector('button#submit').click()
        sleep(5)

        #当前用例结果校验
        alert=ie.switch_to_alert()
        self.assertEqual(alert.text,'登录失败，请检查您的用户名或密码是否填写正确。','结果不正确')
 
        
        
    def tearDown(self):
        ie=self.driver
        sleep(10)
        ie.quit()

