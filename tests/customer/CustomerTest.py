from selenium import webdriver
import unittest
from pages.common.LoginPage import LoginPage
from pages.common.HomePage import HomePage
from pages.customer.Customer import Customer
from pages.customer.RootCustomer import RootCustomer
import time

class CustomerTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        #cls.driver = webdriver.Ie(executable_path="../drivers/IEDriverServer.exe")
        #cls.driver = webdriver.Firefox( executable_path="../drivers/geckodriver_64bit.exe" )
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
        cls.lp = LoginPage(cls.driver)
        cls.rc = RootCustomer(cls.driver)
        cls.hp = HomePage(cls.driver)
        cls.ct = Customer(cls.driver)

    # def test_Navigation(self):
    #     driver = self.driver
    #     driver.get("http://10.254.187.172:9081/vam-ui/#/")
    #     #lp = LoginPage(driver)
    #     self.lp.login("banksup", "Password@123")
    #     self.hp.verifyWelcomeMessage()
    #     time.sleep(5)
    #     self.hp.navigateToRootCustomers()
    #     self.rc.verifyTextonRootCustomer()
    #     #self.sleep(5)

    def test_CreateRootCustomer(self):
        driver = self.driver
        driver.get("http://10.254.187.172:9081/vam-ui/#/")
        self.lp.login("banksup", "Password@123")
        self.hp.verifyWelcomeMessage()
        time.sleep(5)
        self.hp.navigateToRootCustomers()
        self.rc.clickOnAddRootCustomerButton()
        time.sleep( 5 )
        self.ct.fill_customer_information()


    #@classmethod
    #def tearDownClass(cls):
        #cls.driver.close()
