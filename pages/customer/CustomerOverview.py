from Utilities.util import Util
import Utilities.custom_logger as cl
import logging
from pages.customer.Company import Company
from pages.customer.RootCustomer import RootCustomer
from Utilities.teststatus import TestStatus


class CustomerOverview(Company):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.status = TestStatus(self.driver)

    LblcustDetails = "//dt[contains(text(),'{0}')]/following-sibling::dd"
    LblAds = "//div[contains(text(),'{0}')]/../following-sibling::div/div/div", "LblAds"
    # LblAddress = "//div[contains(text(),'Address')]/../following-sibling::div/div/div"
    LblAddress = "//div[contains(text(),'{0}')]"
    LblAddCountry = "//div[contains(text(),'{0}')]/../following-sibling::div/div/strong"
    LblContacts = "//div[contains(text(),'{0}')]/../following-sibling::div/div/dl/dd"
    # LblActiveUsers = "//div[contains(text(),'{0}')]/../following-sibling::div/h2/a/strong"
    LblActiveUsers = "//div[contains(text(),'{0}')]/..//following-sibling::div"
    LblActions_Adduser = "//div[contains(text(),'Actions')]/../following-sibling::div/div/a"
    LblActions_CloseCustomer = "//div[contains(text(),'Actions')]/../following-sibling::div/div/app-customer-action", "Close Customer Label"
    LnkActions_CloseCustomer = "//a[text()[normalize-space()='{0}']]"
    LnkActions_DeleteCustomer = "//a[text()[normalize-space()='{0}']]"
    lnkCustomerName = "//span[contains(text(),'{0}')]"

    btnDeleteCustomer = "//a[contains(text(),'{0}')]/button"
    btnDeleteConfirm = "//div/button[contains(.,'{0}')]"
    btnCancelConfirm = "//button[contains(.,'{0}')]"
    msgDeleteConfirm = "//div/p[contains(text(),'{0}')]"
    titleCustomerNameConfirm = "//div/h4[contains(text(),'{0}')]"
    chkClientsAllowed = "//input[@id='subCustomerAllowedCheckbox']"

    btnCloseCustomer = "//a[contains(text(),'{0}')]/button"
    btnCloseConfirm = "//div/button[contains(.,'{0}')]"
    msgCloseConfirm = "//div/p[contains(text(),'{0}')]"

    lblEditDetails = "//span[contains(text(),'{0}')]"

    lnkParentCustomer = "//dt[text()[normalize-space()='{0}']]/following-sibling::dd/a"
    lnkChangeLog = "//a[text()[normalize-space()='{0}']]"
    userTab = "//ul[@class='nav nav-pills']//li//a//span[contains(text(),'{0}')]"
    userTable = "//div[@class='scrollable-content']//table//tbody"
    userRecordsInTable = "//div[@class='alert alert-info mt-1'][text()[normalize-space() = '{0}']]"
    changeLogLink = "//span[text()[normalize-space()='{0}']]"
    lnkAddIcon = "//div[@class='level-item-actions ng-star-inserted']//a", "Add icon displaying on root customer name "
    actionListItem = "//div[@class='list-group']//a[text()[normalize-space()='{0}']]", "Action List item "
    customerCloseMsgOnPopup = "//h3[@class='modal-title title-wrap'][contains(text(),'{0}')]", "Customer close message displaying on pop up "
    closeButton = "//button[@class='btn btn-danger ng-star-inserted']", "Close button "
    closeCustomer = "//a[contains(text(), 'Close Customer')]//Button", "Close Customer Button"
    cancelCustomer = "//button[@type='{0}']", "Cancel Customer Button"
    customerCloseMsg = "//*[text()[normalize-space() = '{0}']]"
    confirmCloseMsg = "//p[@class='ng-star-inserted']", "Button"
    phoneNumber = "//div[@class='data-list']//dl//dd"

    def clickOnEditCustomerLink(self):
        try:
            self.elementClick(self.lnkCustomerName.format(self.labelsOnUI['Lnk_Editdetails']),
                              locatorType="xpath")
            self.log.error("Successfully clicked on :: " + self.labelsOnUI['Lnk_Editdetails'])
        except Exception as e:
            self.log.error("Error occurred while click on:: " + self.labelsOnUI['Lnk_Editdetails'])

    def verifyCustomerDetails(self, customerDetails):
        result = False
        try:
            self.wait_for_page_load(3)
            result = self.verifyBasicCustomerDetails(customerDetails)
            self.status.mark(result, "Incorrect match")
            result = self.verifyReferenceValues(customerDetails)
            self.status.mark(result, "Incorrect match")
            # result = self.verifyAddressDetails(customerDetails)
            # self.status.mark(result, "Incorrect match")
            # result = self.verifyContactDetails(customerDetails)
            # self.status.mark(result, "Incorrect match")
            self.log.info("Successfully filled Optional fields details::")
        except:
            self.log.info("Error while filling Optional fields details::")
        return result

    def verifyBasicCustomerDetails(self, customerDetails):
        result = False
        try:
            self.status.mark(self.verify(self.LblcustDetails.format(self.labelsOnUI['Lbl_Category']),
                                         customerDetails[self.labelsOnUI['lbl_Customer_category']][0]),
                             "Incorrect match")

            self.status.mark(self.verify(self.LblcustDetails.format(self.labelsOnUI['Lbl_BankID']),
                                         customerDetails[self.labelsOnUI['Lbl_BankID']][0]), "Incorrect match")

            self.status.mark(self.verify(self.LblcustDetails.format(self.labelsOnUI['Lbl_CustomerID']),
                                         customerDetails[self.labelsOnUI['Lbl_CustomerID']][0]), "Incorrect match")

            self.status.mark(self.verify(self.LblcustDetails.format(self.labelsOnUI['Lbl_Name']),
                                         customerDetails[self.labelsOnUI['Lbl_Name']][0]), "Incorrect match")

            self.status.mark(self.verify(self.LblcustDetails.format(self.labelsOnUI['Lbl_PreferredName']),
                                         customerDetails[self.labelsOnUI['Lbl_PreferredName']][0]), "Incorrect match")

            self.status.mark(self.verify(self.LblcustDetails.format(self.labelsOnUI['Lbl_ClientsAllowed']),
                                         customerDetails[self.labelsOnUI['Lbl_ClientsAllowed']][0]), "Incorrect match")

            self.status.mark(self.verify(self.LblcustDetails.format(self.labelsOnUI['Lbl_MarketSegment']),
                                         customerDetails[self.labelsOnUI['Lbl_MarketSegment']][0]), "Incorrect match")

            self.status.mark(self.verify(self.LblcustDetails.format(self.labelsOnUI['Lbl_SectorClassification']),
                                         customerDetails[self.labelsOnUI['Lbl_SectorClassification']][0]),
                             "Incorrect match")

            result = self.status.markFinal("verifyBasicCustomerDetails", result, "Verification is Successful")

            self.log.info("Successfully filled Optional fields details::")
        except:
            self.log.info("Error while filling Optional fields details::")
        return result

    def verifyReferenceValues(self, customerDetails):
        result = False
        try:
            self.status.mark(self.verify(self.LblcustDetails.format(self.labelsOnUI['Lbl_ReferenceNumbers']),
                                         customerDetails[self.labelsOnUI['lbl_Reference_Number']][0]),
                             "Incorrect match")
            self.log.info("Successfully filled Optional fields details::")
        except:
            self.log.info("Error while filling Optional fields details::")
        return result

    def verifyAddressDetails(self, customerDetails):
        result = False
        try:
            self.status.mark(self.verify(self.LblAddress.format(self.labelsOnUI['lbl_Line1']),
                                         customerDetails[self.labelsOnUI['lbl_Line1']][0]), "Incorrect match")
            self.status.mark(self.verify(self.LblAddress.format(self.labelsOnUI['lbl_Line2']),
                                         customerDetails[self.labelsOnUI['lbl_Line2']][0]), "Incorrect match")
            self.status.mark(self.verify(self.LblAddress.format(self.labelsOnUI['lbl_Line3']),
                                         customerDetails[self.labelsOnUI['lbl_Line3']][0]), "Incorrect match")
            self.status.mark(self.verify(self.LblAddress.format(self.labelsOnUI['lbl_Line4']),
                                         customerDetails[self.labelsOnUI['lbl_Line4']][0]), "Incorrect match")
            self.status.mark(self.verify(self.LblAddress.format(self.labelsOnUI['lbl_PostalCode']),
                                         customerDetails[self.labelsOnUI['lbl_PostalCode']][0]), "Incorrect match")
            self.status.mark(self.verify(self.LblAddress.format(self.labelsOnUI['lbl_Country']),
                                         customerDetails[self.labelsOnUI['lbl_Country']][0]), "Incorrect match")
            self.log.info("Successfully filled Optional fields details::")
        except:
            self.log.info("Error while filling Optional fields details::")
        return result

    def verifyContactDetails(self, customerDetails):
        result = False
        try:
            self.status.mark(self.verify(self.LblcustDetails.format(self.labelsOnUI['Lbl_Category']),
                                         customerDetails[self.labelsOnUI['lbl_Customer_category']][0]),
                             "Incorrect match")
            self.log.info("Successfully filled Optional fields details::")
        except:
            self.log.info("Error while filling Optional fields details::")
        return result
