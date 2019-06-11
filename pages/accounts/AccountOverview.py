from base.BasePage import BasePage
import Utilities.custom_logger as cl
import logging
from base.TestParams import TestParams
from Utilities.teststatus import TestStatus
from pages.accounts.Accounts import Accounts
import time


class AccountOverview(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    lblAccountDetails = "//dt[contains(.,'{0}')]/following-sibling::dd"
    lblAccountDetailsTopOverview = "//small[contains(.,'{0}')]/.."
    lblAccountButtons = "//*[contains(.,'{0}')]"
    addRootAccountHeading = "//*[contains(.,'{0}')]"
    addRootAccountButton = "//a[text()[normalize-space() = 'Add root account']]"
    Overviewpage = "//div[@class='split-container']/div"
    btnBlockAccount = "//button[@class='btn btn-circle btn-circle-sm btn-outline-danger ml-auto']"
    btnCloseAccount = "//button[@class='btn btn-circle btn-circle-sm btn-outline-danger ml-auto']"
    lblInActiontab = "//*[text()[normalize-space() = '{0}']]"

    # Block Account Pop Elements
    rdoAll = "//h3[contains(text(),'{0}')]/parent::div/following-sibling::div/descendant::div/div/label/preceding-sibling::input"
    lblRdoAll = "//h3[contains(text(),'{0}')]/parent::div/following-sibling::div/descendant::div/div/label"
    lblRdoDescAll = "//h3[contains(text(),'{0}')]/parent::div/following-sibling::div/descendant::div/div/label/p/small"
    btnCancel = "//button[text()[normalize-space() = '{0}']]"
    btnSaveBlockingChanges = "//button[text()[normalize-space() = '{0}']]"
    btnActionAccount = "//a[text()[normalize-space() = '{0}']]"
    notBlockedRadio = "//label[@for='notBlockedRadio']"
    blockedRadio = "//label[@for='blockedRadio']"
    blockedCreditRadio = "//label[@for='blockedCreditRadio']"
    blockedDebitRadio = "//label[@for='blockedDebitRadio']"

    # Close Account Pop Elements
    btnCloseAccountonPopUp = "//button[@class='btn btn-lg btn-success']"

    # Delete Account Pop Elements
    btnDeleteOnPopUp = "//button[@class='btn btn-danger ng-star-inserted']"

    # Account SetUp Helper
    lblAccountSetupHelper = "//div[@class='card-title' and text()='Account Setup Helper']"
    iconAccountSetUpHelperButtons = "//a[contains(.,'{0}')]/button"
    btnAccountSetUpHelper = "//button[contains(.,'{0}')]"

    # links
    lnkEditDetails = "//span[contains(text(),'{0}')]/.."
    lnkChangeLog = "//span[text()[normalize-space()='{0}']]/.."
    lnkBalanceDetails = "//span[text()[normalize-space()='{0}']]/.."

    # Other
    balanace = "//div[contains(text(),'{0}')]/../following-sibling::div//div[@class='ng-star-inserted']"
    lblAvailableAmount = "//div[text()='{0}']/../following-sibling::div//h4"
    accountName = "//div[@class='level-item hidden-overflow bg-selected']//span[text()[normalize-space()='{0}']]"

    def clickOnOptionsInActionTab(self, targetAction):
        try:
            self.waitForElement(self.lblInActiontab.format(targetAction), locatorType="xpath")
            self.executeJavaScript(self.lblInActiontab.format(targetAction), locatorType="xpath")
            self.log.info("Successfully able to click on::" + targetAction + "::link")
        except Exception as e:
            self.log.error("Unable to click on::" + targetAction + "::link")

    def verifyAccountBlockedBasedOnInput(self, accountTargetStatus):
        try:
            self.wait_for_page_load(2)
            self.elementClick(accountTargetStatus, locatorType="xpath")
            self.log.info("Successfully able to click on Block radio button::")
            self.executeJavaScript(self.btnSaveBlockingChanges.format(self.labelsOnUI['btnSaveBlockAccountPopUp']),
                                   locatorType="xpath")
            self.log.info("Successfully able to click on Save blocking changes button::")
            blockText = self.getText(accountTargetStatus, locatorType="xpath").split('\n')

            if 'Blocked' or 'Blocked For Credit' or 'Blocked For Debit' == blockText[0]:
                return self.verifyMessageOnProgressBar(self.labelsOnUI['msgAccountBlockedSuccessfully'])
            else:
                return self.verifyMessageOnProgressBar(self.labelsOnUI['msgAccountUnblockedSuccessfully'])
        except Exception as e:
            self.log.error("Unable to click on Block radio button::")
            return False

    def verifyClosedAccountFunctionality(self):
        try:
            self.wait_for_page_load(2)
            self.elementClick(self.btnCloseAccountonPopUp, locatorType="xpath")
            return self.verifyMessageOnProgressBar(self.labelsOnUI['msgClosedAccount'])
        except Exception as e:
            self.log.error("Unable to click on Block radio button::")
            return False

    def verifyDeleteAccountFunctionality(self):
        try:
            # self.wait_for_page_load(2)
            self.waitForElement(self.btnDeleteOnPopUp, locatorType="xpath")
            self.elementClick(self.btnDeleteOnPopUp, locatorType="xpath")
            return self.verifyMessageOnProgressBar(self.labelsOnUI['msgDeleteAccount'])
        except Exception as e:
            self.log.error("Unable to click on Block radio button::")
            return False
