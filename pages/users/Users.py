from Utilities.util import Util
from base.BasePage import BasePage
import Utilities.custom_logger as cl
import logging
from Utilities.teststatus import TestStatus


class Users( BasePage ):
    log = cl.customLogger( logging.DEBUG )

    def __init__(self, driver):
        super().__init__( driver )
        self.driver = driver
        self.status = TestStatus( self.driver )

    progressBar = "//div[@class='simple-notification success ng-trigger ng-trigger-enterLeave']"
    txtUserId = "//input[@id='ID']"
    txtNumberOfVotes = "//input[@id='votes']"
    txtFirstName = "//input[@id='firstName']"
    txtLastName = "//input[@id='lastName']"
    txtEmailId = "//input[@id='email']"
    txtPhone = "//input[@id='phone']"
    txtPassword = "//input[@id='password1']"
    txtRepeatPassword = "//input[@id='password2']"
    txtSearchUser = "//th/div/div/input"

    # Select boxes
    ddlProfile = "//select[@formcontrolname='roleId']"
    ddlStatusfilter = "//span[@class='ml-2']/../following-sibling::div/div[text()='{0}']"
    ddlFilter = "//span[@class='ml-2']"

    # ddlProfile = "#select[@id='profile']"
    # Button
    btnAddUser = "//button[contains(.,'{0}')]"

    btnAddSaveUser = "//div [@class='modal-footer']/div/following-sibling::div/button[contains(.,'{0}')]"
    btnSaveUser = "//div[@class='text-right ml-auto']/button"

    btnBankUser = "//span[contains(.,'Bank Users')]", "Bank User Button"
    btnAddMainUser = "#button[@class='btn btn-primary']", "Add Main User"
    # rdoUserStatus = "#label[contains(@class,'custom-control custom-radio')]/span[text()='%s']"
    rdoUserStatus = "//label[contains(@class,'custom-control-label')][(text()='%s')]", "User Status Radio Button"

    # links
    Lnksetup = "//span[contains(.,'Setup')]", "Setup Link"
    LnkViewEditDelete = "//td/following-sibling::td/span/a[contains(.,'{0}')]"
    LnkHiddenDelete = "//td[contains(.,' 970D')]/following-sibling::td/span[@style='visibility: hidden;']/a[contains(.,'Delete')]", "Delete Hidden Link"
    lnkResetPassWord = "//h5[contains(.,'%s')]/..", "Reset Password Link"
    lnkBankUserStatusFilter = "//span[contains(text(),'%s')]", "Bank User Staus Filter Link"
    lblAddUser = "//h3[contains(.,'Add user')]", "Add User Label"
    lnkUserProfile = "//div#li[@class='nav-item d-none d-md-flex dropdown']/a/app-icon", "user Profile Link"
    actionList = "#div[@class='list-group']/a[text()[normalize-space() = '%s']]", "Action List on Account OvewView Page"
    # dates
    ActiveFromDate = "#input[@id='fromDate' and @placeholder='YYYY-MM-DD']", "Active From Date"
    ActiveToDate = "#input[@id='toDate' and @placeholder='YYYY-MM-DD']", "Active To Date"
    lnkiconActiveFromDate = "(#*[name()='svg' and @class='icon icon-calendar'])[1]", "Active From DateCalender Icon"
    lnkiconActiveToDate = "(#*[name()='svg' and @class='icon icon-calendar'])[2]", "Active To DateCalender Icon"
    # msg
    msg = "#div[contains(text(),'%s')]"
    # lable
    lblMandatory = "#label[@class='required'][contains(text(),'%s')]", "Mandatory Label"
    lblOptional = "#label[contains(.,'%s')]", "Optional Label"
    lblUserDetails = "//label[contains(.,'{0}')]/following-sibling::p"
    lblAccessRights = "//tbody/tr[@class='ng-star-inserted']/td[{0}]"
    lblStatus = "//label[contains(.,'{0}')]/../p/strong"
    strGenericTableXpath = "#td[contains(.,'%s')]#ancestor::tr#td[count(#*[normalize-space(text())='%s']#ancestor-or-self::th/preceding-sibling::th)+1]"
    # strUserName="#div#strong[contains(.,'%s')]"
    strUserName = "#div#strong", "UserName"
    # strUserName="#div[contains(@class,'px-4 pt-2 pb-3 text-force-wrap')]"

    # other
    msgValidation = "#label[contains(.,'%s')]/../div"
    tblBankStatus = "#tbody[contains(@class,'ng-tns-c')]/tr[%s]/td[4]", "Bank Status in Table"
    tblBankStatusRows = "#tbody[contains(@class,'ng-tns-c')]/tr", "Bank Status rows in Table"
    tblCustStatus = "#tbody[@class='ng-tns-c14-6 ng-star-inserted']/tr/td[5]", "Customer Status in Table"
    tblCustStatusRows = "#tbody[@class='ng-tns-c14-6 ng-star-inserted']", "Customer Status rows in Table"

    btnDeleteCustomer = "#a[contains(text(),'%s')]/button", "Delete Customer Button"
    btnDeleteConfirm = "#div/button[contains(.,'%s')]", "Delete Confirm Button"
    btnCancelConfirm = "#div/a[contains(.,'%s')]", "Cancel Confirm Button"
    msgDeleteConfirm = "#div/p[contains(text(),'%s')]", "Delete Confirm Message"
    titleCustomerNameConfirm = "#div/h4[contains(text(),'%s')]", "Title Customer Name Confirm"
    adminTitle = "#a[contains(.,'Admin')]", "Admin Title"
    selectBankRoleID = "#select[@formcontrolname='roleId']", "Select Bank Role ID"
    txtRolesAllValue = "#select[@formcontrolname='roleId']/option", "Bank Role ID Values"
    btnChangelog = "#button[text()[normalize-space()='%s']]", "Changelog Button"
    btnEdit = "#button[@id='editButton1']", "Edit Button"
    strParentCustName = "#div/strong[contains(text(), '%s')]/parent::div/following-sibling::small[contains(text(),'%s')]", "Parent Customer Name"
    usersTitle = "#span[contains(.,'users')]", "Users Title"
    lblUserId = "#tbody[contains(@class,'ng-tns-c')]/tr/td[contains(.,'%s')]", "Users id"

    util = Util()

    def createUsers(self, usersABO):
        newusersABO = ''
        try:
            self.clickOnAddUserButton();
            newusersABO = self.fillUsersDetails( usersABO )
            self.clickOnAddOrSaveButton()
            # self.verifyMessage("UserSuccessCreateMessage", "User is successfully Created",
            #                " Not able to Create user. Success message not displayed.")
        except Exception as e:
            self.log.error( "Error occurred while creating user ::" )
        return newusersABO

    def clickOnAddUserButton(self):
        try:
            self.waitForElement( self.btnAddUser, 4 )
            self.elementClick( self.btnAddUser.format( self.navigationMap.get( 'AddUser' ) ),
                               locatorType="xpath" )
        except Exception as e:
            self.log.error( "Error occurred while click on the Add user button::" )

    def fillUsersDetails(self, usersABO):
        try:
            # UserID = usersABO.get('User ID') + Util.get_unique_number(5)
            self.wait_for_page_load( 2 )
            self.sendKeys( usersABO.get( 'UserId' ), self.txtUserId, locatorType="xpath" )
            self.sendKeys( usersABO.get( 'firstName' ), self.txtFirstName, locatorType="xpath" )
            self.sendKeys( usersABO.get( 'lastName' ), self.txtLastName, locatorType="xpath" )
            self.sendKeys( usersABO.get( 'email' ), self.txtEmailId, locatorType="xpath" )
            self.sendKeys( usersABO.get( 'phone' ), self.txtPhone, locatorType="xpath" )
            self.selectvaluefromDropdown( usersABO.get( 'profile' ), self.ddlProfile, locatorType="xpath" )
            self.sendKeys( usersABO.get( 'Password' ), self.txtPassword, locatorType="xpath" )
            self.sendKeys( usersABO.get( 'repeatPassword' ), self.txtRepeatPassword, locatorType="xpath" )
        except Exception as e:
            self.log.error( "Exception occurred while entering User's Details::" )
        return usersABO

    def clickOnAddOrSaveButton(self):
        try:
            # self.waitForElement(self.ddlAccountType )
            self.elementClick( self.btnAddSaveUser.format( self.navigationMap['AddUser'] ),
                               locatorType="xpath" )
        except Exception as e:
            self.log.error( "Error occurred while click on the Add user button of Add user screen::" )

    def searchUser(self, usersABO):
        try:
            self.wait_for_page_load( 7 )
            self.sendKeysAndEnter( usersABO.get( 'UserId' ), self.txtSearchUser, locatorType="xpath" )
        except Exception as e:
            self.log.error( "Exception occurred while doing search users ::" )

    def clickOnViewUser(self, usersABO):
        try:
            self.waitForElement( self.LnkViewEditDelete )
            self.elementClick( self.LnkViewEditDelete.format( self.navigationMap.get( 'View' ) ),
                               locatorType="xpath" )
        except Exception as e:
            self.log.error( "Exception occurred in clickOnViewUser ::" )

    def verifyUserDetails(self, usersABO):
        try:
            self.clickOnViewUser( self )
            actualText = self.getText( self.lblUserDetails.format( self.navigationMap.get( 'UserID' ) ),
                                       locatorType="xpath" )
            result = self.util.verifyTextMatch( actualText, usersABO.get( 'UserId' ) )
            self.status.mark( result, "Title Verified" )
            # assert result == True
            actualText = self.getText( self.lblUserDetails.format( self.navigationMap.get( 'FirstName' ) ),
                                       locatorType="xpath" )
            result = self.util.verifyTextMatch( actualText, usersABO.get( 'firstName' ) )
            self.status.mark( result, "Title Verified" )
            # assert result == True
            actualText = self.getText( self.lblUserDetails.format( self.navigationMap.get( 'LastName' ) ),
                                       locatorType="xpath" )
            result = self.util.verifyTextMatch( actualText, usersABO.get( 'lastName' ) )
            self.status.mark( result, "Title Verified" )
            # assert result == True
            actualText = self.getText( self.lblUserDetails.format( self.navigationMap.get( 'Email' ) ),
                                       locatorType="xpath" )
            result = self.util.verifyTextMatch( actualText, usersABO.get( 'email' ) )
            self.status.mark( result, "Title Verified" )
            # assert result == True
            actualText = self.getText( self.lblUserDetails.format( self.navigationMap.get( 'Phone' ) ),
                                       locatorType="xpath" )
            result = self.util.verifyTextMatch( actualText, usersABO.get( 'phone' ) )
            # assert result == True
            actualText = self.getText( self.lblStatus.format( self.navigationMap.get( 'UserStatus' ) ),
                                       locatorType="xpath" )
            result = self.util.verifyTextMatch( actualText, usersABO.get( 'userStatus' ) )
            # assert result == True
            actualText = self.getText( self.lblAccessRights.format( self.navigationMap.get( 'BankId' ) ),
                                       locatorType="xpath" )
            result = self.util.verifyTextMatch( actualText, usersABO.get( 'BANKID' ) )
            # assert result == True
            actualText = self.getText( self.lblAccessRights.format( self.navigationMap.get( 'Profile' ) ),
                                       locatorType="xpath" )
            result = self.util.verifyTextMatch( actualText, usersABO.get( 'profile' ) )
            # assert result == False
            self.status.markFinal( "verifyUserDetails", result, "Verification is Successful" )
        except Exception as e:
            assert True == False
            self.log.error( "Exception occurred while verifying user details ::" )
        return result
