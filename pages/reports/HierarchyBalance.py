from base.BasePage import BasePage
import Utilities.custom_logger as cl
import logging
from base.TestParams import TestParams
from inputTestData import inputAccountCashManagementTest
from Utilities.util import Util
from pages.reports.Template import Template
from Utilities.teststatus import TestStatus


class HierarchyBalance(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.status = TestStatus(self.driver)

    Overview_AvailableAmount = ""
    Overview_BookedBalance = ""
    Overview_ValueDated = ""
    Overview_OrdinaryOD = "Null"
    Overview_AditionalOD = "Null"
    Overview_IntraDayOD = "Null"
    Overview_BlockedAmount = "Null"
    Overview_TotalOD = "Null"

    label = "//label[contains(.,'{0}')]"
    blockHeading = "//div[@class='card-title'][contains(.,'{0}')]"
    blockValue = "//div[@class='card-title'][contains(.,'{0}')]/parent::div//h4"
    overViewLimitValues = "//dt[text()='{0}']/following::dd"
    overViewBalances = "//div[@class='card-title'][contains(.,'{0}')]/parent::div/following::div//h4"
    txtSelectCurrency = "//input[@placeholder='Select currencies...']"
    txtSelectCurrencyDropdown = "//strong[text()='{0}']"
    tblSubsidiaryAccounts = "//table/tbody/tr"
    txtCurrencyCell = "//table/tbody/tr[{0}]/td[8]"
    iconClose = "//a[@class='close' and text()='×']"
    lbl_NoAccountPresent = "//div[contains(@class,'alert')]"
    lnk_AccountName = "//a[@id='dropdownBasic1']/em"
    lbl_AccountDetails = "//div[text()='{0}']/following-sibling::div"
    lbl_AccountType = "//div[text()='Type']/..//div//span/following-sibling::span"
    btn_HierarchyBalance = "//button[@class='btn btn-circle btn-circle-sm btn-outline-success ml-auto']"
    lnk_AccountTabs = "//span[text()='{0}']/parent::a"
    # public static final ElementSelector txt_AccountSearch = "//input[@id='typeahead-template']"
    txt_AccountSearch = "//input[contains(@placeholder,'Search Accounts...')]"
    # public static final ElementSelector txt_AccountAutoSuggestion = "//button[contains(@class,'dropdown-item')]"
    txt_AccountAutoSuggestion = "//div[contains(@class,'dropdown-item')]"
    chkbox_IncludeCurrencyAccounts = "//input[@id='currencyAccountsCheckbox']"
    lbl_tblAccountName = "//table/tbody/tr[{0}]/td[1]"
    lbl_tblAccountNumber = "//table/tbody/tr[{0}]/td[2]"
    lbl_tblOwner = "//table/tbody/tr[{0}]/td[3]"
    lbl_tblAccountType = "//table/tbody/tr[{0}]/td[7]"
    btn_GoToPreviousLevel = "//button[text()[normalize-space()='Go to previous level']]"
    labelHierarchyBalance = "//li[@class='d-inline-block nav-item ng-star-inserted']"

    def verifyDefaultHierarchyBalances(self):
        try:
            # To check the Headings
            self.status.mark(self.isElementDisplayed(self.label.format(self.labelsOnUI['HB_TotalBalances']),
                                                     locatorType="xpath"), "Incorrect match")
            self.status.mark(self.isElementDisplayed(self.blockHeading.format(self.labelsOnUI['HB_AvailableBalances']),
                                                     locatorType="xpath"), "Incorrect match")
            self.status.mark(self.isElementDisplayed(self.blockHeading.format(self.labelsOnUI['HB_ValueDatedBalances']),
                                                     locatorType="xpath"), "Incorrect match")
            self.status.mark(self.isElementDisplayed(self.blockHeading.format(self.labelsOnUI['HB_BookedBalances']),
                                                     locatorType="xpath"), "Incorrect match")
            self.status.mark(self.isElementDisplayed(self.blockHeading.format(self.labelsOnUI['HB_TotalODLimit']),
                                                     locatorType="xpath"), "Incorrect match")
            self.status.mark(self.isElementDisplayed(self.blockHeading.format(self.labelsOnUI['HB_TotalBlockedAmount']),
                                                     locatorType="xpath"), "Incorrect match")
            self.status.markFinal("verifyDefaultHierarchyBalances",
                                  self.isElementDisplayed(self.blockHeading.format(self.labelsOnUI['HB_IntraDayLimit']),
                                                          locatorType="xpath"), "Verification is Successful")
            self.log.info("Successfully capture the values on Hierarchy Balance :: ")
        except Exception as e:
            self.log.error("Unable to capture the values on Hierarchy Balance:: ")

    def captureOviewPageBalanceValues(self):
        try:
            self.Overview_AvailableAmount = self.getText(
                self.overViewBalances.format(self.labelsOnUI['OV_AvailableAmount']),
                locatorType="xpath")
            self.Overview_BookedBalance = self.getText(self.overViewBalances.format(self.labelsOnUI['OV_BookedAmount']),
                                                       locatorType="xpath")
            self.Overview_ValueDated = self.getText(self.overViewBalances.format(self.labelsOnUI['OV_ValueDated']),
                                                    locatorType="xpath")
            self.log.error("Successfully capture the values on Hierarchy Balance :: ")
        except Exception as e:
            self.log.error("Unable to capture the values on Hierarchy Balance:: ")
