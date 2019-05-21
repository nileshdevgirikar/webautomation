from base.BasePage import BasePage
import Utilities.custom_logger as cl
import logging
from base.TestParams import TestParams
from inputTestData import inputAccountCashManagementTest
from Utilities.util import Util
from datetime import date


class Template(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

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
    lnkButtons = "//tr//td[text()[normalize-space() = '%s']]/following-sibling::td//span//a[text()[normalize-space() = '%s']]"
    lnkMsg = "//div[contains(text(),'%s')]"

    # button
    btnButton = "//button[@class='btn btn-danger ng-star-inserted']"
    lbltemplateViewDetailsPage = "//div[@class='modal-body']//label[text()[normalize-space() = '%s']]/following-sibling::p"
    btnClose = "//button[@class='btn btn-lg btn-secondary']"
    iconCross = "//button[@class='close']", "Cross Icon"
    templateNameInTableList = "//div[@class='scrollable-content']/table//tbody//tr//td[1]"
    transactionTypeAll = "//select[@formcontrolname='transactionType']//option[@value='%s']"
    deletePopUpTitle = "//div[@class='modal-header align-items-start']//h3['%s'] | //div[@class='modal-header align-items-start']//p['%s']"
    msgOnDeletePopUp = "//div[@class='modal-body pb-3']//div[text()[normalize-space()='%s']]"
    titleOfEditPopUp = "//div[@class='modal-header']//h3[@class='modal-title'][text()[normalize-space()='Edit Report Template']] | //div[@class='modal-header']//p[text()[normalize-space()='%s']]"
    closeIconOnSelectedCurrency = "//a[@class='close'] | //span[@class='ng-clear-wrapper ng-star-inserted']"
    btnCancelOnDeleteTemplatePopup = "//button[text()[normalize-space()='%s']]"

    # Check box
    chkBoxIncludeCurrencyAccounts = "//input[@id='includeCurrency']/following-sibling::label"
    amtRangeError = "//div[@for='amount']"
    cancelButtonOnEditTemplatePopUp = "//button[@class='btn btn-lg btn-secondary']"
    enterNumberOfDaysTextBox = "//input[@formcontrolname='periodInDays']"

    def navigateToTemplate(self):
        try:
            self.waitForElement(self.lnktemplate)
            self.elementClick(self.lnktemplate.format(self.navigationMap['Template']),
                              locatorType="xpath")
            self.log.info("Successfully navigated to " + self.navigationMap['Template'])
        except:
            self.log.info("Error while navigating to" + self.navigationMap['Template'])

    def createReportTemplate(self, templateinfo):
        try:
            for i in range(len(templateinfo)):
                self.fill_template_details(templateinfo, i)
                self.selectOptionalFields(templateinfo, i)
                self.clickOnSaveButton()
            self.log.info("Successfully create report template::")
        except:
            self.log.info("Error while creating report template::")

    def fill_template_details(self, templateinfo, i):
        try:
            ReportType = templateinfo.loc[i].get('Report Type')

            flag = self.iselementSelected(self.templateType.format(ReportType), locatorType="xpath")
            if flag == False:
                self.elementClick(self.templateType.format(ReportType), locatorType="xpath")

            templateinfo['Template Name'][i] = templateinfo['Template Name'][i] + Util.get_unique_number(14)
            self.sendKeys(templateinfo['Template Name'][i], self.templateName, locatorType="xpath")

            access = templateinfo.loc[i].get('Access')
            self.elementClick(self.templateAccess.format(access), locatorType="xpath")

            self.selectCurrency(templateinfo, i)

            if ReportType == 'Balance':
                self.selectvaluefromDropdown(templateinfo['View'][i], self.ddlView, locatorType="xpath")
                self.elementClick(self.chkBoxIncludeCurrencyAccounts, locatorType="xpath")
            else:
                self.setFromAndToAmount(templateinfo, i)
                self.selectvaluefromDropdown(templateinfo['Account type'][i], self.templateAccountType,
                                             locatorType="xpath")
                self.selectvaluefromDropdown(templateinfo['Transaction Type'][i],
                                             self.templateTranscationType, locatorType="xpath")

            self.elementClick(self.templatePeriod.format(templateinfo['Period'][i]),
                              locatorType="xpath")
            self.log.info("Successfully filled template details::")
        except:
            self.log.info("Error occured while filling template details::")

    def selectCurrency(self, templateinfo, i):
        try:
            self.elementClick(self.ddlTemplateCurrencyBox, locatorType="xpath")
            # self.selectvaluefromDropdown(currency, self.ddlTemplateCurrency, locatorType="xpath")
            self.sendKeys(templateinfo['Currencies'][i], self.ddlTemplateCurrencyBox, locatorType="xpath")
            self.elementClick(self.ddlTemplateCurrency, locatorType="xpath")
            self.log.info("Successfully select currency details::")
        except:
            self.log.info("Error in while selecting currency::")

    def setFromAndToAmount(self, templateinfo, i):
        try:
            amount = templateinfo['Amount Range'][i].split("|")
            self.sendKeys(amount[0], self.templateFromAmountRange, locatorType="xpath")
            self.sendKeys(amount[1], self.templateToAmountRange, locatorType="xpath")
            self.log.info("Successfully filled amount details::")
        except:
            self.log.info("Error while entering amount::")

    def selectOptionalFields(self, templateinfo, i):
        try:
            Optionalfields = templateinfo['Optional fields'][i].split("|")
            for count in range(len(Optionalfields)):
                self.elementClick(self.templateOptionalFields.format(Optionalfields[count]),
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
