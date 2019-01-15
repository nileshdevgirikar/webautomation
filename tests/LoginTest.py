from selenium import webdriver
import unittest
from pages.common.LoginPage import LoginPage
from pages.common.HomePage import HomePage
import time

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
        cls.lp = LoginPage(cls.driver)


    def test_login_valid(self):
        driver = self.driver
        driver.get("http://10.254.187.172:9081/vam-ui/#/")

        #lp = LoginPage(driver)
        self.lp.login("banksup", "Password@123")

        time.sleep(5)

        hp = HomePage(driver)
        hp.verifyTextonHomepage()
        hp.clickUserDropdown()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()






