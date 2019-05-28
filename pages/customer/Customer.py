from Utilities.util import Util
import Utilities.custom_logger as cl
import logging
from pages.customer.RootCustomer import RootCustomer
import time
from inputTestData import inputCustomerTest
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

class Customer( RootCustomer ):
    log = cl.customLogger( logging.DEBUG )

    def __init__(self, driver):
        super().__init__( driver )
        self.driver = driver

    # Locators
    companyTitle = "//h4[contains(.,'{0}')]"
    accountTitle = "//h4[contains(.,'{0}')]"
    lblMandatory = "//label[@class='required'][contains(text(),'{0}')]"
    lbl_tblheader = "//th[contains(text(),'{0})]"

    # radiobuttons
    rdoSubEntity = "//input[@id='subEntityRadio']"
    rdoClient = "//input[@id='clientRadio']"
    rdoLblSubEntity = "//label[@for='subEntityRadio']"
    rdoLblClient = "//label[@for='clientRadio']"
    rdoCustomerCategory = "//input[@type='radio']/ancestor::label[contains(.,'{0}')]"
    rdoCorporate = "//input[@id='corporateRadio']"
    rdoIndividual = "//input[@id='individualRadio']"
    rdoLblCorporate = "//label[@for='corporateRadio']"
    rdoLblIndividual = "//label[@for='individualRadio']"

    # textbox
    txtBankId = "//select[@id='bankId']"
    txtName = "//input[@formcontrolname='firstName']"
    txtlastName = "//input[@formcontrolname='lastName']"
    txtPreferredName = "//input[@formcontrolname='companyName']"
    txtCustomerId = "//input[@id='customerIdentity']"
    txtAddressLine1 = "//input[@id='addressLine1']"
    txtAddressLine2 = "//input[@id='addressLine2']"
    txtAddressLine3 = "//input[@id='addressLine3']"
    txtAddressLine4 = "//input[@id='addressLine4']"
    txtPostalCode = "//input[@id='postalCode']"
    txtParentCustomer = "//span[@class='ng-arrow-zone']"
    txtParentCustomerAllValue = "//div[contains(@class,'ng-select-dropdown-outer bottom')]//div/span"
    txtParentCustomerVlue = "//div[contains(@class,'ng-select-dropdown-outer bottom')]//div/span[contains(text(),'{0}')]"
    txtReferenceNo = "//input[@id='customerReference']"
    txtContactValue = "//input[@id='contactPhoneNumber']"
    txtContactDescription = "//input[@id='contactDescription']"
    txtOptionalReference = "(//select[@formcontrolname='customerRefType']/ancestor::td/following-sibling::td/input[@id='customerReference'])[%d]"
    txtOptionalReferenceNumber = "//select[@formcontrolname='customerRefType']/ancestor::td/following-sibling::td/input[@id='customerReference']"
    txtManRefNumber = "(//th[text()[normalize-space()='%s']]/following::label[@class='required ng-star-inserted']/ancestor::td/following-sibling::td/input[@id='customerReference'])[%d]"
    txtcustomerReference = "//input[@id='customerReference']"

    # dropdown
    ddlSectorClassification = "//select[@id='institutionalSectorCode']"
    ddlMarketSegment = "//select[@id='marketSegmentCode']"
    ddlCountry = "//select[@id='country']"
    ddlContactType = "//select[@id='contactType']"
    ddlRefType = "//select[@formcontrolname='customerRefType']"
    ddlOpRefType = "(//select[@formcontrolname='customerRefType'])[%d]"
    ddlOptionalRefType = "//select[@formcontrolname='customerRefType']"

    # ddlManRefType = "//select[@formcontrolname='customerRefType'][(@disabled)]"
    ddlManRefType = "//tr[@class='ng-untouched ng-pristine ng-invalid ng-star-inserted']"

    # Button
    btnClose = "//button[@class='close']"
    btnAddCustomer = "//app-icon[@iconname='plus']/ancestor::button[@class='btn btn-lg btn-success'][contains(.,'{0}')]"

    # btnCancel = "//a[@class='btn btn-lg btn-secondary']"
    btnCancel = "//button[@class='btn btn-lg btn-secondary']"
    btnSave = "//button[contains(.,'%s')]"
    btnAddRef = "//span[contains(.,'{0}')]"
    btnSaveChanges = "//button[@class='btn btn-lg btn-success']"

    # Checkbox
    chkClientsAllowed = "//input[@id='subCustomerAllowedCheckbox']"
    chkClientsAllowedLabel = "//label[@for='subCustomerAllowedCheckbox']"

    # msg
    msg = "//div[contains(text(),'{0}')]"
    label = "//label[text()='{0}']"
    lblValue = "//label[contains(text(),'%s')]/following-sibling::p"
    deleteIcon = "//fieldset[@formarrayname='customerReferences']/table[@class='table table-sm']" \
                 "//tr[%s]//td[@class='actions ng-star-inserted']/a"
    deleteIconForOptRef = "//select[@formcontrolname='customerRefType']" \
                          "/following::td[@class='actions ng-star-inserted']/a"
    deleteIconAsPerOptRef = "(//select[@formcontrolname='customerRefType']" \
                            "/following::td[@class='actions ng-star-inserted'])[%d]/a"

    numberOfDeleteIcons = "//table[@class='table table-sm']" \
                          "//tbody//tr[@class='ng-untouched ng-pristine ng-valid ng-star-inserted']//td//a"
    # lblDatils = "//div[@class='data-list data-list-row data-list-row-align-right mt-2']//dl//dt[contains(.,'%s')]/..")
    lblRootCustomerName = "//a[@title='%s']"

    # other
    rootCustomerIsSelected = "//li[@class='level-0 has-children selected ng-star-inserted']"

    lnkCustomerName = "//span[contains(text(),'{0}')]"
    addChildCustomer = "//span[text()='{0}']/following-sibling::" \
                       "div[@class='level-item-actions ng-star-inserted']//app-icon[@iconclass='icon-sm']"

    btnSendForActivation = "//button[@class='btn btn-primary']"
    chkboxChooseBranchForApproval = "//label/div/strong[text()='{0}']"
    btnSend = "//button[@class='btn btn-lg btn-success']"

    def FillRootCustomer(self):
        root = inputCustomerTest.rootCustomer
        for datafields in root:

            if root[datafields] == 'Click':
                self.elementClick( locator=self.datafields, locatorType="xpath" )

    def clickOnParentCustomerToAddChild(self, parent):
        try:
            self.elementClick( self.lnkCustomerName.format( parent ),
                               locatorType="xpath" )
            self.elementClick( self.addChildCustomer.format( parent ),
                               locatorType="xpath" )
        except Exception as e:
            self.log.error("Error occurred while click on AddChild button. :: ")

    def fill_customer_information(self, root):
        try:
            self.select_customer_category(root['Customer catergory'])
            self.select_customer_type(root['Customer type'])
            self.setName(root['Name'], root['PreferredName'])
            self.set_customer_id(root['Customer Id'])
            self.select_sector_classification(root['Sector classification'])
            self.select_Market_Segment(root['Market Segment'])
            # if str( root['Customer category'] ) == str( self.labelsOnUI['lbl_CustCategory_SubEntity'] ):
            #     self.decide_Whether_Clients_Allowed( root['Clients allowed'] )
            self.fill_address_details(root)
            self.fill_contact_details(root)
            self.fill_customer_references(root)
        except Exception as e:
            self.log.error("Error occurred while filling customer information. :: ")

    def createCustomerHierarchy(self, company, keyvalue):
        if type( company ) is dict:
            for key, value in company.items():
                fill = inputCustomerTest.rootCustomer
                fill['Name'] = str( key )
                self.fill_customer_information( fill )
                self.clickOnAddCustomerButton()
                time.sleep( 5 )
                keyvalue = key
                self.clickOnParentCustomerToAddChild( key )
                self.createCustomerHierarchy( value, keyvalue )
        elif type( company ) is str:
            fill = inputCustomerTest.rootCustomer
            fill['Name'] = str( company )
            self.fill_customer_information( fill )
            self.clickOnAddCustomerButton()
            time.sleep( 5 )
        elif type( company ) is list:
            for item in company:
                print( keyvalue )
                self.clickOnParentCustomerToAddChild( keyvalue )
                self.createCustomerHierarchy( item, keyvalue )

    def fill_address_details(self, address):
        try:
            self.sendKeys(address['Line 1'], self.txtAddressLine1, locatorType="xpath")
            self.sendKeys(address['Line 2'], self.txtAddressLine2, locatorType="xpath")
            self.sendKeys(address['Line 3'], self.txtAddressLine3, locatorType="xpath")
            self.sendKeys(address['Line 4'], self.txtAddressLine4, locatorType="xpath")
            self.sendKeys(address['Postal code'], self.txtPostalCode, locatorType="xpath")
            self.selectvaluefromDropdown(address['Country'], self.ddlCountry, locatorType="xpath")
        except Exception as e:
            self.log.error("Error occurred while filling address details. :: ")

    def fill_contact_details(self, contactDetails):
        try:
            self.selectvaluefromDropdown(contactDetails['Type'], self.ddlContactType, locatorType="xpath")
            self.sendKeys( contactDetails['Value'], self.txtContactValue, locatorType="xpath" )
            self.sendKeys( contactDetails['Description'], self.txtContactDescription, locatorType="xpath" )
        except Exception as e:
            self.log.error( "Error occurred while filling contact details. :: " )

    def fill_customer_references(self, customerReferences):
        try:
            self.add_Mandatory_References( customerReferences )
            # self.add_Optional_References( customerReferences )
        except Exception as e:
            self.log.error( "Problem occurred while adding customer references. :: " )

    def add_Mandatory_References(self, customerReferences):
        try:
            References = customerReferences['Reference type']
            self.selectvaluefromDropdown(References, self.ddlOptionalRefType, locatorType="xpath")
            ReferencesNumber = customerReferences['Reference number'] + Util.get_unique_number(5)
            self.sendKeys(ReferencesNumber, self.txtcustomerReference, locatorType="xpath")
        except Exception as e:
            self.log.error( "Problem occurred while adding Mandatory references. :: " )

    def add_Optional_References(self, customerReferences):
        try:
            References = customerReferences['Reference type']
            # for key in References:
            #     self.elementClick( self.btnAddRef.format( self.labelsOnUI['btn_AddAnotherReference'] ),
            #                        locatorType="xpath" )
            #     self.selectvaluefromDropdown( key, self.ddlOptionalRefType, locatorType="xpath" )
            #     references_number = References.get( key ) + Util.get_unique_number( 8 )
            #     self.sendKeys( references_number, self.txtOptionalReferenceNumber, locatorType="xpath" )
            self.elementClick(self.btnAddRef.format(self.labelsOnUI['btn_AddAnotherReference']),
                              locatorType="xpath")
            self.selectvaluefromDropdown(References, self.ddlOptionalRefType, locatorType="xpath")
            # references_number = customerReferences['Reference number'] + Util.get_unique_number( 8 )
            # self.sendKeys( references_number, self.txtOptionalReferenceNumber, locatorType="xpath" )
        except Exception as e:
            self.log.error( "Problem occurred while adding Optional references. :: " )

    def select_customer_category(self, customerCategory):
        try:
            new = self.labelsOnUI['lbl_CustCategory_SubEntity']
            if str(customerCategory) == str(self.labelsOnUI['lbl_CustCategory_SubEntity']):
                self.elementClick( self.rdoSubEntity, locatorType="xpath" )
            else:
                self.elementClick( self.rdoClient, locatorType="xpath" )
        except Exception as e:
            x = str( e.with_traceback() )
            self.log.error( "Error occurred while selecting the customer category :: " + customerCategory )

    def select_customer_type(self, custType):
        try:
            if custType == self.labelsOnUI['lbl_CustCategory_SubEntity']:
                self.elementClick( self.rdoCorporate, locatorType="xpath" )
            else:
                self.elementClick( self.rdoIndividual, locatorType="xpath" )
        except:
            self.log.error( "Error occurred while selecting the customer category :: " + custType )

    def setName(self, Name, PreferredName):
        try:
            self.sendKeys(Name, self.txtName, locatorType="xpath")
            self.sendKeys(PreferredName, self.txtPreferredName, locatorType="xpath")
        except Exception as e:
            self.log.error( "Error occurred while seting the Name :: " + Name )

    def set_customer_id(self, customerId):
        try:
            self.strCustomerId = customerId + Util.get_unique_number( 10 )
            self.sendKeys( self.strCustomerId, self.txtCustomerId, locatorType="xpath" )
        except Exception as e:
            self.log.error( "Error occurred while seting the CustomerId :: " + self.strCustomerId )

    def select_sector_classification(self, sector_classification):
        try:
            self.selectvaluefromDropdown( sector_classification, self.ddlSectorClassification, locatorType="xpath" )

        except Exception as e:
            self.log.error( "Error occurred while seting the Sector Classification :: " + sector_classification )

    def select_Market_Segment(self, market_segment):
        try:
            self.selectvaluefromDropdown( market_segment, self.ddlMarketSegment, locatorType="xpath" )
        except Exception as e:
            self.log.error( "Error occurred while seting the Market Segment :: " + market_segment )

    def decide_Whether_Clients_Allowed(self, subCustomerAllowed):
        try:
            if subCustomerAllowed == 'True':
                self.log.info( "Making client allowed checkbox enabled :: " )
            else:
                self.elementClick(self.chkClientsAllowedLabel, locatorType="xpath" )
                self.log.info( "Making client allowed checkbox disabled :: " )
        except Exception as e:
            self.log.error("Error occurred while setting the Market Segment :: ")

    def clickOnAddCustomerButton(self, ):
        try:
            self.elementClick(self.btnAddCustomer.format(self.labelsOnUI['btn_Add_Customer']),
                              locatorType="xpath")
        except Exception as e:
            self.log.error( "Error occurred while filling address details. :: " )

    def activateCustomer(self, companyName):
        try:
            self.waitForElement( self.btnSendForActivation )
            self.elementClick( self.btnSendForActivation, locatorType="xpath" )
            self.waitForElement( self.chkboxChooseBranchForApproval )
            self.elementClick( self.chkboxChooseBranchForApproval.format( companyName ),
                               locatorType="xpath" )
            self.elementClick( self.btnSend, locatorType="xpath" )
        except Exception as e:
            self.log.error( "Error occurred while filling address details. :: " )
