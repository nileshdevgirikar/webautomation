from base.BasePage import BasePage
import Utilities.custom_logger as cl
import logging
from base.TestParams import TestParams
from inputTestData import inputAccountCashManagementTest
from Utilities.util import Util
from pages.reports.Template import Template
from Utilities.teststatus import TestStatus


class Reports(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.template = Template(self.driver)
        self.status = TestStatus(self.driver)

    btnNewTemplate = "//*[text()[normalize-space() = '{0}']]"
    templateAccessFilter = "(//div[@class='btn btn-link dropdown dropdown-toggle']//span)[1]"
    templateTypeFilter = "(//div[@class='btn btn-link dropdown dropdown-toggle']//span)[2]"
    templateAccessFilterValue = "//div[@class='dropdown-menu show']//div[text()[normalize-space()='{0}']]"
    reportsTable = "//div[@class='scrollable-content']/table"
    selectCreatedTemplateInList = "//div[@class='scrollable-content']/table//tbody//tr//td[text()[normalize-space() = '{0}']]"
    searchTemplateName = "//*[text()[normalize-space() = '{0}']]"

    selectCreatedTemplateInList = "//div[@class='scrollable-content']/table//tbody//tr//td[text()[normalize-space()='{0}']]"
    # selectReadioBtnOfTemplate = "//div[@class='scrollable-content']/table//tbody//tr//td[text()[normalize-space() = '{0}']]//following-sibling::td//span[text()[normalize-space() = 'Select']]"
    selectReadioBtnOfTemplate = "//*[text()[normalize-space() = '{0}']]//following-sibling::td//span[text()[normalize-space() = 'Select']]"
    selectScheduleOnReportSetting = "//label[@class='custom-control-label'][text()[normalize-space() = '{0}']]"
    searchAccountBox = "//div[@class='d-inline-block w-100 dropdown']//input"
    searchAccountInList = "//div[@class='scrollable-content']//*[text()[normalize-space()='({0})']]"
    tableScroll = "//div[@class='ps__thumb-y']"
    confirmationBtnLabel = "//button[@class='btn btn-primary ng-star-inserted button-margin']//span"

    def clickOnButton(self, buttonText):
        try:
            self.waitForElement(self.btnNewTemplate, 2)
            self.executeJavaScript(self.btnNewTemplate.format(buttonText), locatorType="xpath")
            self.wait_for_page_load(3)
        except Exception as e:
            self.log.error("Unable to click on button :: ")

    def setAccessFilter(self, templateinfo, count):
        try:
            self.wait_for_page_load(3)
            self.elementClick(self.templateAccessFilter, locatorType="xpath")
            self.elementClick(self.templateAccessFilterValue.format(templateinfo.loc[count]['Access']),
                              locatorType="xpath")
            self.elementClick(self.templateTypeFilter, locatorType="xpath")
            self.elementClick(self.templateAccessFilterValue.format(templateinfo.loc[count]['Report Type']),
                              locatorType="xpath")
        except Exception as e:
            self.log.error("Unable to click on button :: ")

    def clickonViewToVerifyDetails(self, text):
        try:
            self.elementClick(self.searchTemplateName.format(text), locatorType="xpath")
            self.log.info("Successfully click on View button " + self.labelsOnUI['lbl_templateName'])
        except Exception as e:
            self.log.info("Error while navigating to" + self.labelsOnUI['lbl_templateName'])

    def clickonSelectRadioButton(self, text):
        try:
            self.elementClick(self.selectReadioBtnOfTemplate.format(text), locatorType="xpath")
            self.log.info("Successfully click on Select Schedule button::")
        except Exception as e:
            self.log.info("Error while selecting::" + "clickonSelectRadioButton")

    def selectSchedule(self, text):
        try:
            self.elementClick(self.selectScheduleOnReportSetting.format(text), locatorType="xpath")
            self.log.info("Successfully click on Select Radio button::")
        except Exception as e:
            self.log.info("Error while selecting::" + "clickonSelectRadioButton")

    def selectFrequency(self, text):
        try:
            Flag = self.iselementSelected(self.selectScheduleOnReportSetting.format(text), locatorType="xpath")
            if Flag == False:
                self.elementClick(self.selectScheduleOnReportSetting.format(text), locatorType="xpath")
                self.log.info("Successfully click on Select Radio button::")
            else:
                self.log.info("Frequency Radio button is already selected::")
        except Exception as e:
            self.log.info("Error while selecting::" + "clickonSelectRadioButton")

    def setAccountName(self, text):
        try:
            self.sendKeys(text, self.searchAccountBox, locatorType="xpath")
            self.elementClick(self.selectReadioBtnOfTemplate.format(text), locatorType="xpath")
            self.elementClick(self.searchAccountInList.format(text), locatorType="xpath")
            self.log.info("Successfully click on Select Radio button::")
        except Exception as e:
            self.log.info("Error while selecting::" + "clickonSelectRadioButton")

    def searchTemplateInList(self, text, locator=None):
        try:
            self.wait_for_page_load(3)
            findFlag = False
            if locator == None:
                while not findFlag:
                    findFlag = self.isElementDisplayed(self.searchTemplateName.format(text),
                                                       locatorType="xpath")
                    # findFlag = self.isElementPresent(self.searchTemplateName.format('03APRPKTRAN'),
                    #                                  locatorType="xpath")
                    if findFlag:
                        break
                        # self.elementClick(self.searchTemplateName.format('03APRPKTRAN'), locatorType="xpath")
                        # self.elementClick(self.searchTemplateName.format(templateinfo.loc[count]['Template Name']),
                        #                   locatorType="xpath")
                    else:
                        self.webScroll('down')
                        # self.elementScroll(self.tableScroll,'down')
            else:
                findFlag = self.elementScroll(self.tableScroll, self.searchTemplateName.format(text))
            return findFlag
        except Exception as e:
            self.log.error("Unable to click on button :: ")

    def create_search_verifyTemplate(self, templateinfo):
        count = len(templateinfo)
        result = False
        try:
            for i in range(count):
                self.clickOnButton(self.labelsOnUI['btnNewTemplate'])
                self.wait_for_page_load(3)
                self.template.createReportTemplate(templateinfo, i)
                self.setAccessFilter(templateinfo, i)
                if self.searchTemplateInList(templateinfo[self.labelsOnUI['lbl_templateName']][i]):
                    self.clickonViewToVerifyDetails(templateinfo[self.labelsOnUI['lbl_templateName']][i])
                    result = self.template.verifyReportDetails(templateinfo, i)
                    self.template.clickOnCloseButton()
                    self.log.info("Template is created successfully ::")
                else:
                    self.log.info("Template is not found in search list ::")
        except Exception as e:
            self.log.error("Unable to create Template ::")
        return result

    def create_search_verifySchedule(self, templateinfo):
        count = len(templateinfo)
        result = False
        try:
            for i in range(count):
                self.clickOnButton(self.labelsOnUI['btnNewReport'])
                self.wait_for_page_load(2)
                self.setAccessFilter(templateinfo, i)
                if self.searchTemplateInList(templateinfo[self.labelsOnUI['lbl_templateName']][i], self.tableScroll):
                    self.clickonSelectRadioButton(templateinfo[self.labelsOnUI['lbl_templateName']][i])
                    self.webScroll('down')
                    self.clickOnButton(self.labelsOnUI['nextButton'])
                    self.setAccountName("112312312321")
                    self.selectSchedule(templateinfo[self.labelsOnUI['lbl_selectSchedule']][i])
                    self.clickOnButton(self.labelsOnUI['nextButton'])
                    self.selectFrequency(templateinfo[self.labelsOnUI['lbl_frequency']][i])
                    self.clickOnButton(self.labelsOnUI['finishButton'])
                    result = self.is_text_present(self.labelsOnUI['confirmationMessageForSchedulesReport'])
                    self.status.mark(result, "Incorrect match")
                    self.clickOnButton(self.labelsOnUI['btnGoToSchedulesReports'])
                    result = self.searchTemplateInList(templateinfo[self.labelsOnUI['lbl_templateName']][i])
                    self.status.markFinal("create_search_verifySchedule", result, "Verification is Successful")
                    self.log.info("Schedule is created successfully :: ")
                else:
                    self.log.info("Schedule is not found:: ")
        except Exception as e:
            self.log.error("Unable to create Schedule :: ")
        return result

    def is_text_present(self, text):
        return str(text) in self.driver.page_source
