import unittest
import pytest
from pages.common.LoginPage import LoginPage
from pages.common.HomePage import HomePage
from resources.config import ApplicationConfig
import time


@pytest.mark.usefixtures( "oneTimeSetUp", "SetUp" )
class LoginTest(unittest.TestCase):

    @pytest.fixture( autouse=True )
    def classSetup(self, oneTimeSetUp):
        self.login = LoginPage( self.driver )
        self.home = HomePage( self.driver )

    @pytest.mark.Smoke
    def test_login_valid(self):
        self.login.loginToApplication( ApplicationConfig.get( 'UserId' ), ApplicationConfig.get( 'Password' ) )
        self.home.verifyWelcomeMessage( ApplicationConfig.get( 'UserId' ) )
        self.home.userLogout()

    @pytest.mark.Regression
    def test_login_invalid(self):
        self.login.loginToApplication( 'banksup', 'Tieto@123' )
        # self.home.verifyWelcomeMessage('banksup1')
