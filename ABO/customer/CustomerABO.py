class CustomerABO():
    customerCategory = ''
    customerType = ''
    Name = ''
    CustomerId = '0'

    def __init__(self, driver):
        self.bankId = "VAHI"
        self.custStatus = "Draft"
        self.clientAccount = "false"
        self.clientsAllowed = "true"
        self.custId = "0"
        # self.bankId = EnvVars.BANKID;
        self.corporateName = "AutoCustomer"
        self.custStatusWebService = "A"
        self.custTaxStatus = "G"
        self.custType = "C"
        self.customerCategory = "M"
        # self.customerIdLength = 9L;
        # self.contactInformation = ContactInformationABO();
        # self.nameCust = new NameABO();
        # self.customerReferences = new CustomerReferenceABO[]
        self.subCustAccessFlag = "false"
        self.subCustomerAllowed = "false"
        self.withHoldingTaxApplicable = "false"

    def getCustomerCategory(self):
        return self.customerCategory

    def setCustomerCategory(self, customerCategory):
        customerCategory = customerCategory

    def getCustomertype(self):
        return self.customerCategory

    def setCustomertype(self, customerType):
        customerType = customerType

    def getName(self):
        return self.Name

    def setName(self, Name):
        Name = Name

    def getPreferredName(self):
        return self.PreferredName

    def setPreferredName(self, PreferredName):
        PreferredName = PreferredName

    def getCustomerId(self):
        return self.CustomerId

    def setCustomerId(self, CustomerId):
        CustomerId = CustomerId

    def getSectorClassfication(self):
        return self.SectorClassfication

    def setSectorClassfication(self, SectorClassfication):
        SectorClassfication = SectorClassfication

    def getMarketSegment(self):
        return self.SectorClassfication

    def setMarketSegment(self, marketSegment):
        marketSegment = marketSegment
