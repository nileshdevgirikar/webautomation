from base.BasePage import BasePage
import Utilities.custom_logger as cl
import logging
from base.TestParams import TestParams
from inputTestData import inputAccountCashManagementTest
from Utilities.util import Util
from pages.reports.Template import Template


class Reports(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.template = Template(self.driver)

    btnNewTemplate = "//span[text()[normalize-space() = '{0}']]/.."
    templateAccessFilter = "(//div[@class='btn btn-link dropdown dropdown-toggle']//span)[1]"
    templateTypeFilter = "(//div[@class='btn btn-link dropdown dropdown-toggle']//span)[2]"
    templateAccessFilterValue = "//div[@class='dropdown-menu show']//div[text()[normalize-space()='{0}']]"
    reportsTable = "//div[@class='scrollable-content']/table"
    selectCreatedTemplateInList = "//div[@class='scrollable-content']/table//tbody//tr//td[text()[normalize-space()='{0}']]"
    searchTemplateName = "//*[text()[normalize-space() = '{0}']]"


    def clickOnButton(self):
        try:
            self.waitForElement(self.btnNewTemplate, 4)
            self.executeJavaScript(self.btnNewTemplate.format(self.labelsOnUI['btnNewTemplate']),
                                   locatorType="xpath")
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

    def searchDetailsInList(self, templateinfo, count):
        try:
            self.wait_for_page_load(3)
            findFlag = False
            while not findFlag:
                findFlag = self.isElementPresent(
                    self.searchTemplateName.format(templateinfo.loc[count]['Template Name']),
                    locatorType="xpath")
                # findFlag = self.isElementPresent(self.searchTemplateName.format('03APRPKTRAN'),
                #                                  locatorType="xpath")
                if findFlag:
                    # self.elementClick(self.searchTemplateName.format('03APRPKTRAN'), locatorType="xpath")
                    self.elementClick(self.searchTemplateName.format(templateinfo.loc[count]['Template Name']),
                                      locatorType="xpath")
                else:
                    self.webScroll('down')
        except Exception as e:
            self.log.error("Unable to click on button :: ")

    def create_search_verifyReport(self, templateinfo):
        count = len(templateinfo)
        try:
            for i in range(count):
                self.clickOnButton()
                self.wait_for_page_load(3)
                self.template.createReportTemplate(templateinfo, i)
                self.setAccessFilter(templateinfo, i)
                self.searchDetailsInList(templateinfo, i)
                self.template.verifyReportDetails(templateinfo, i)
                self.template.clickOnCloseButton()
        except Exception as e:
            self.log.error("Unable to click on button :: ")
