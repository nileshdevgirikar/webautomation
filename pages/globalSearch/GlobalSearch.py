from base.BasePage import BasePage
import Utilities.custom_logger as cl
import logging
from Utilities.teststatus import TestStatus


class GlobalSearch(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.status = TestStatus(self.driver)

    lnk_globalSearch = "//div[@class='dropdown ng-star-inserted']"
    # globalSearch_list = "//div[@class='dropdown-menu show']/a[contains(.,'{0}')]"
    globalSearch_list = "//div[@class='dropdown-menu show']/div/a[contains(.,'{0}')]"
    searchTextBox = "//div[@class='input-group']/input"
    lnk_search = "//button[@class='btn btn-link px-3']"
    LblcustDetails = "//dt[contains(text(),'{0}')]/following-sibling::dd"
    LblcustDetails_Category = "//div[@class='col']/div/span[2]"
    LblAccountdetails = "//dt[contains(text(),'{0}')]"
    searchWaterMark = ".//input[@placeholder='{0}']"
    lnk_openAccount = ".//div[@class='row']/div[@class='col']"
    lnk_openCustomer = "//div[@class='card card-clickable mb-3 ng-star-inserted']/div[@class='card-body']"
    lnk_header = "//div[@class='header']"
    lnk_searchHeader = "//div[contains(text(),'{0}')]"
    lnk_defaultglobalSearch = "//*[@id='navbarSupportedContent']/div"
    lnk_recentSearchList = "//div[@class='row']/div[@class='column-two']//span[contains(text(),'{0}')]"
    lnk_recentSearchList_1 = "//div[@class='row']/div[@class='column-two']"
    btn_Search = "//button[@class='btn dropdown-color dropdown-toggle']"
    optionInGlobalSearchDropDown = "//div[@class='dropdown-menu show']/div/a[text()[normalize-space()='{0}']]"

    def searchAccountOrCustomerAndClick(self, targetString, searchString=None):
        try:
            if searchString != None:
                self.selectGlobalSearchType(searchString)
            self.addValueToSearch(targetString)
            self.clickOnSearchBtn()
            self.OpenSearchedResults()
            self.log.info("Successfully able to search string::")
        except Exception as e:
            self.log.error("Not abel to search:: ")

    def selectGlobalSearchType(self, searchString):
        try:
            self.wait_for_page_load(3)
            self.elementClick(self.lnk_globalSearch, locatorType="xpath")
            self.executeJavaScript(self.globalSearch_list.format(searchString), locatorType="xpath")
            self.log.info("Successfully able to search ::" + searchString)
        except Exception as e:
            self.log.error("Not abel to search:: " + searchString)

    def addValueToSearch(self, targetString):
        try:
            self.sendKeys(targetString, self.searchTextBox, locatorType="xpath")
            self.log.info("Successfully able to set text in search box ::")
        except Exception as e:
            self.log.error("Unable to set text in search box:: ")

    def clickOnSearchBtn(self):
        try:
            # self.wait_for_page_load(2)
            self.waitForElement(self.lnk_search, locatorType="xpath", timeout=2)
            self.executeJavaScript(self.lnk_search, locatorType="xpath")
            self.log.info("Successfully click on  search button::")
        except Exception as e:
            self.log.error("Not abel to click on search button::")

    def OpenSearchedResults(self):
        try:
            self.waitForElement(self.lnk_openAccount, locatorType="xpath", timeout=5, pollFrequency=1)
            self.elementClick(self.lnk_openAccount, locatorType="xpath")
            self.log.info("Successfully able to search ::")
        except Exception as e:
            self.log.error("Not abel to search:: ")
