from base.BasePage import BasePage
import Utilities.custom_logger as cl
import logging
from base.TestParams import TestParams
from inputTestData import inputAccountCashManagementTest
from Utilities.util import Util
from datetime import date


class Transactions(BasePage):
    log = cl.customLogger( logging.DEBUG )

    def __init__(self, driver):
        super().__init__( driver )
        self.driver = driver

    progressBar = "//div[@class='simple-notification success has-icon ng-trigger ng-trigger-enterLeave'] | //div[@class='simple-notification success ng-trigger ng-trigger-enterLeave']"
    lnkTransactions = "//a/span[text()='{0}']"
    rows_Trn = "//table//tr"
    cell_TrnAmt = "//table//tr[{0}]/td[8]"
    cell_TrnDate = "//table//tr[{0}]/td[1]"
    cell_AcctName = "//table//tr[{0}]/td[2]"
    cell_Category = "//table//tr[{0}]/td[3]"
    cell_TransactionType = "//table//tr[{0}]/td[4]"
    cell_ValueDate = "//table//tr[{0}]/td[7]"
    lnkView = "//table//tr['{0}']/td[9]//a[text()[normalize-space()='{0}']] | //table//tr[1]/td[8]//a[text()[normalize-space()='View']]"
    lnkMove = "//table//tr['{0}']/td[9]//a[text()[normalize-space()='{0}']]"
    lnkViewRow = "//table//tr['{0}']/td[8]//a[text()[normalize-space()='View']]"
    lnkExport = "//button/span"

    cell_CategoryPain = "//table//tr['{0}']/td[2]"
    cell_ValueDatePain = "//table//tr['{0}'/td[6]"
    cell_TrnAmtPain = "//table//tr['{0}']/td[7]"
    txtTargetAccount = "//label[ text()[normalize-space()='{0}']]/../descendant::input"
    ddlTargetAccount = "//span[text()[normalize-space()='{0}']]"
    txtDynamicLocator = "//*[text()[normalize-space()='{0}']]"
    lblMovedToFromAccount = "//*[text()[normalize-space()='{0}']]/following-sibling::td"
    lblExceptionTranAmountOnWidget = "//*[@class='text-right text-danger ng-star-inserted']/strong"
    reportDataTable = "//table[contains(@class, 'table-clickable-rows')]"
    reportOption = "//div[text()='%{0}']"
    linksOnTransactionRecord = "//table//tr//td[9]//a[text()[normalize-space()='{0}']]"

    # Icons
    iconFilter = "//a[@class='btn btn-circle btn-circle-sm ml-2 mr-2 btn-outline-primary']"

    # TextBoxes
    txtValueFromDate = "//input[@id='valueFromDate']"
    txtValueToDate = "//input[@id='valueToDate']"

    # Buttons
    btnApplyFilter = "//button[@class='btn btn-sm btn-primary']//span[contains(text(),'%s')]"


    def navigateToTransactions(self):
        try:
            self.waitForElement( self.lnkTransactions)
            self.elementClick( self.lnkTransactions.format( self.navigationMap['lnkTransactions']),
                               locatorType="xpath" )
            self.log.info( "Successfully navigated to " + self.navigationMap['lnkTransactions'] )
        except:
            self.log.info( "Error while navigating to" + self.navigationMap['lnkTransactions'])

    def verifyTransationsOnUI(self, input, transactionAccount):
        result = False
        cntCreditTrn = 0
        cntDebitTrn = 0
        exceptionRow = 0
        trnRowsFromTestData = 0
        value = ""
        amount = 0.00
        try:
            trnRowsOnUI = self.getElementList(self.rows_Trn).size()
            trnRowsFromTestData= input.get('ntry_Credit') + input.get('ntry_Debit') + 1

            if (trnRowsOnUI -1) != trnRowsFromTestData:
                self.log.info("Credit/Debit Transaction not posted::")
            else:
                today = str(date.today())
                for i in trnRowsOnUI:
                    value = self.getText(self.cell_TrnDate.format(i))
                    if today == value:
                        amount = amount + float(self.getText(self.cell_TrnAmt.format(i)[3:]))
        except:
            self.log.info( "Error while navigating to" + self.navigationMap['lnkTransactions'])