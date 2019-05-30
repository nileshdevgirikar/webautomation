from base.BasePage import BasePage
import Utilities.custom_logger as cl
import logging
from base.TestParams import TestParams
from inputTestData import inputAccountCashManagementTest
from Utilities.util import Util
from datetime import date
from Utilities.teststatus import TestStatus


class Template(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.status = TestStatus(self.driver)

    lnktemplate = "//span[contains(text(),'{0}')]"
    templateName = "//div[@class='form-group col-6 pl-0']//input[@formcontrolname='name']"
    templateAccess = "//div[@class='custom-controls-inline']//label[@class='custom-control-label'][contains(text(),'{0}')]"
    # templateType = "//div[@class='col-6 form-group custom-control custom-radio custom-radio-accent ng-star-inserted']//label[@class='form-control custom-control-label'][contains(text(),'{0}')]"
    templateType = "//label[@class='form-control custom-control-label'][contains(text(),'{0}')]"

    ddlTemplateCurrencyBox = "//input[@role='combobox']"
    templateFromAmountRange = "//input[@formcontrolname='fromAmount']"
    templateToAmountRange = "//input[@formcontrolname='toAmount']"

    inpCurrency = "//input[@class='form-control ui-select-search']"
    ddlTemplateCurrency = "//div[@class='ng-option ng-star-inserted'] | //li[@class='ng-star-inserted']"
    templateAmountRange = "//div[@class='row']//input[@formcontrolname='%s']"
    templateAccountType = "//select[@formcontrolname='accountType']"
    templateTranscationType = "//select[@formcontrolname='transactionType']"
    templatePeriod = "//input[@formcontrolname='period']/following-sibling::label[text()[normalize-space() = '{0}']]"
    templateOptionalFields = "//label[@class='custom-control-label'][text()[normalize-space() = '{0}']]"
    templateSave = "//button[@class='btn btn-lg btn-success']"
    ddlView = "//select[@formcontrolname='reportView']"

    # link
    lnkButtons = "//tr//td[text()[normalize-space() = '{0}']]/following-sibling::td//span//a[text()[normalize-space() = '{0}']]"
    lnkMsg = "//div[contains(text(),'{0}')]"

    # button
    btnButton = "//button[@class='btn btn-danger ng-star-inserted']"
    lbltemplateViewDetailsPage = "//div[@class='modal-body']//label[text()[normalize-space() = '{0}']]/following-sibling::p"
    btnClose = "//button[@class='btn btn-lg btn-secondary']"
    iconCross = "//button[@class='close']", "Cross Icon"
    templateNameInTableList = "//div[@class='scrollable-content']/table//tbody//tr//td[1]"
    transactionTypeAll = "//select[@formcontrolname='transactionType']//option[@value='{0}']"
    deletePopUpTitle = "//div[@class='modal-header align-items-start']//h3['{0}] | //div[@class='modal-header align-items-start']//p['{0}']"
    msgOnDeletePopUp = "//div[@class='modal-body pb-3']//div[text()[normalize-space()='{0}']]"
    titleOfEditPopUp = "//div[@class='modal-header']//h3[@class='modal-title'][text()[normalize-space()='Edit Report Template']] | //div[@class='modal-header']//p[text()[normalize-space()='%s']]"
    closeIconOnSelectedCurrency = "//a[@class='close'] | //span[@class='ng-clear-wrapper ng-star-inserted']"
    btnCancelOnDeleteTemplatePopup = "//button[text()[normalize-space()='{0}']]"

    # Check box
    chkBoxIncludeCurrencyAccounts = "//input[@id='includeCurrency']/following-sibling::label"
    amtRangeError = "//div[@for='amount']"
    cancelButtonOnEditTemplatePopUp = "//button[@class='btn btn-lg btn-secondary']"
    enterNumberOfDaysTextBox = "//input[@formcontrolname='periodInDays']"

    def navigateToTemplate(self):
        try:
            self.waitForElement(self.lnktemplate)
            self.elementClick(self.lnktemplate.format(self.labelsOnUI['Template']),
                              locatorType="xpath")
            self.log.info("Successfully navigated to " + self.labelsOnUI['Template'])
        except:
            self.log.info("Error while navigating to" + self.labelsOnUI['Template'])

    def navigateToSchedule(self):
        try:
            self.waitForElement(self.lnktemplate)
            # self.elementClick(self.lnktemplate.format(self.labelsOnUI['schedulesReportMenu']),
            #                   locatorType="xpath")
            self.executeJavaScript(self.lnktemplate.format(self.labelsOnUI['schedulesReportMenu']),
                                   locatorType="xpath")
            self.log.info("Successfully navigated to " + self.labelsOnUI['schedulesReportMenu'])
        except:
            self.log.info("Error while navigating to" + self.labelsOnUI['schedulesReportMenu'])

    def clickOnCloseButton(self):
        try:
            self.executeJavaScript(self.btnClose, locatorType="xpath")
        except Exception as e:
            self.log.error("Unable to click on button :: ")

    def createReportTemplate(self, templateinfo, i):
        try:
            self.fill_template_details(templateinfo, i)
            self.selectOptionalFields(templateinfo, i)
            self.clickOnSaveButton()
            self.log.info("Successfully create report template::")
        except:
            self.log.info("Error while creating report template::")

    def fill_template_details(self, templateinfo, i):
        try:
            ReportType = templateinfo.loc[i].get(self.labelsOnUI.get('lbl_templateReportType'))

            flag = self.iselementSelected(self.templateType.format(ReportType), locatorType="xpath")
            if flag == False:
                self.elementClick(self.templateType.format(ReportType), locatorType="xpath")

            templateinfo[self.labelsOnUI['lbl_templateName']][i] = templateinfo[self.labelsOnUI['lbl_templateName']][i] \
                                                                   + Util.get_unique_number(14)
            self.sendKeys(templateinfo[self.labelsOnUI.get('lbl_templateName')][i],
                          self.templateName, locatorType="xpath")

            access = templateinfo.loc[i].get(self.labelsOnUI.get('lbl_templateAccess'))
            self.elementClick(self.templateAccess.format(access), locatorType="xpath")

            self.selectCurrency(templateinfo, i)

            if ReportType == 'Balance':
                self.selectvaluefromDropdown(templateinfo[self.labelsOnUI['lbl_templateView']][i],
                                             self.ddlView, locatorType="xpath")
                self.elementClick(self.chkBoxIncludeCurrencyAccounts, locatorType="xpath")
            else:
                self.setFromAndToAmount(templateinfo, i)
                self.selectvaluefromDropdown(templateinfo[self.labelsOnUI['lbl_templateAccountType']][i],
                                             self.templateAccountType, locatorType="xpath")
                self.selectvaluefromDropdown(templateinfo[self.labelsOnUI['lbl_templateTransactionType']][i],
                                             self.templateTranscationType, locatorType="xpath")

            self.elementClick(self.templatePeriod.format(templateinfo[self.labelsOnUI['lbl_templatePeriod']][i]),
                              locatorType="xpath")
            self.log.info("Successfully filled template details::")
        except:
            self.log.info("Error occured while filling template details::")

    def selectCurrency(self, templateinfo, i):
        try:
            self.elementClick(self.ddlTemplateCurrencyBox, locatorType="xpath")
            self.sendKeys(templateinfo[self.labelsOnUI['lbl_templateCurrency']][i],
                          self.ddlTemplateCurrencyBox, locatorType="xpath")
            self.elementClick(self.ddlTemplateCurrency, locatorType="xpath")
            self.log.info("Successfully select currency details::")
        except:
            self.log.info("Error in while selecting currency::")

    def setFromAndToAmount(self, templateinfo, i):
        try:
            amount = templateinfo[self.labelsOnUI['lbl_templateAmountRange']][i].split(" - ")
            self.sendKeys(amount[0], self.templateFromAmountRange, locatorType="xpath")
            self.sendKeys(amount[1], self.templateToAmountRange, locatorType="xpath")
            self.log.info("Successfully filled amount details::")
        except:
            self.log.info("Error while entering amount::")

    def selectOptionalFields(self, templateinfo, i):
        try:
            optionalfields = templateinfo[self.labelsOnUI['lbl_optionalFields']][i].split("|")
            for count in range(len(optionalfields)):
                self.elementClick(self.templateOptionalFields.format(optionalfields[count]),
                                  locatorType="xpath")
            self.log.info("Successfully filled Optional fields details::")
        except:
            self.log.info("Error while filling Optional fields details::")

    def clickOnSaveButton(self):
        try:
            self.elementClick(self.templateSave, locatorType="xpath")
            # isElementDisplayed(lnkMsg.format(VAMConstants.getCaption("MessageTemplateUpdatedSuccessfully")));
            self.log.info("Successfully clicked on Save button::")
        except:
            self.log.info("Error while clicking on Save button::")

    def verify(self, lbltemplateViewDetailsPage, expectedResult):
        result = False
        try:
            actualText = self.getText(lbltemplateViewDetailsPage, locatorType="xpath")
            result = self.util.verifyTextMatch(actualText, expectedResult)
            self.log.info("Successfully verify detail of::" + expectedResult)
        except:
            self.log.info("Error in verifying detail of::" + expectedResult)
        return result

    def verifyReportDetails(self, templateinfo, i):
        result = False
        try:
            self.wait_for_page_load(3)
            Optionalfields = templateinfo[self.labelsOnUI['lbl_optionalFields']][i].split("|")

            result = self.verify(self.lbltemplateViewDetailsPage.format(self.labelsOnUI['lbl_templateName']),
                                 templateinfo[self.labelsOnUI['lbl_templateName']][i])
            self.status.mark(result, "Incorrect match")

            if templateinfo[self.labelsOnUI.get('lbl_templateCurrency')][i] == 'Select All':
                result = self.verify(self.lbltemplateViewDetailsPage.format(self.labelsOnUI['lbl_templateCurrency']),
                                     'XXX')
            else:
                result = self.verify(
                    self.lbltemplateViewDetailsPage.format(self.labelsOnUI.get('lbl_templateCurrency')),
                    templateinfo[self.labelsOnUI['lbl_templateCurrency']][i])
            self.status.mark(result, "Incorrect match")

            result = self.verify(self.lbltemplateViewDetailsPage.format(self.labelsOnUI.get('lbl_templateReportType')),
                                 templateinfo[self.labelsOnUI['lbl_templateReportType']][i])
            self.status.mark(result, "Incorrect match")

            result = self.verify(self.lbltemplateViewDetailsPage.format(self.labelsOnUI['lbl_templatePrivacy']),
                                 templateinfo[self.labelsOnUI['lbl_templateAccess']][i])
            self.status.mark(result, "Incorrect match")

            result = self.verify(self.lbltemplateViewDetailsPage.format(self.labelsOnUI['lbl_templateTransactionType']),
                                 templateinfo[self.labelsOnUI['lbl_templateTransactionType']][i])
            self.status.mark(result, "Incorrect match")

            result = self.verify(self.lbltemplateViewDetailsPage.format(self.labelsOnUI['lbl_templatePeriod']),
                                 templateinfo[self.labelsOnUI['lbl_templatePeriod']][i])
            self.status.mark(result, "Incorrect match")

            result = self.verify(self.lbltemplateViewDetailsPage.format(self.labelsOnUI['lbl_templateAmountRange']),
                                 templateinfo[self.labelsOnUI['lbl_templateAmountRange']][i])
            self.status.mark(result, "Incorrect match")

            result = self.verifyOptionFields(templateinfo, i)
            self.status.mark(result, "Incorrect match")
            self.log.info("Successfully filled Optional fields details::")
        except:
            self.log.info("Error while filling Optional fields details::")
        return result

    def verifyOptionFields(self, templateinfo, i):
        result = False
        try:
            optionalFieldValues = self.getText(self.lbltemplateViewDetailsPage.
                                               format(self.labelsOnUI['lbl_optionalFields1']),
                                               locatorType="xpath")
            actualListOfOptionalFieldsOnUI = optionalFieldValues.split(",")
            actualListOfOptionalFieldsOnUI = [items.strip() for items in actualListOfOptionalFieldsOnUI]
            expectedListOfOptionalfields = templateinfo[self.labelsOnUI['lbl_optionalFields']][i].split("|")
            actualListOfOptionalFieldsOnUI.sort()
            expectedListOfOptionalfields.sort()
            if actualListOfOptionalFieldsOnUI == expectedListOfOptionalfields:
                result = True
            else:
                result = False
            self.log.info("Successfully verify Optional fields details ::")
        except:
            self.log.info("Error in verifying Optional fields details::")
        return result
