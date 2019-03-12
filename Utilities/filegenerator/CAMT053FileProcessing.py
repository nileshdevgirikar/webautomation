from Utilities.util import Util
from Utilities.filegenerator.CAMT053InputData import CAMT053InputData
from Utilities.filegenerator.CAMT053Tags import CAMT053Tags
from datetime import date
from datetime import datetime
from xml.dom import minidom
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as etree


class CAMT053FileProcessing():
    outputFileFullName = ""
    paramFilePath = ""
    custID = ""
    path = ""
    multiple = False
    Bal_Ccy = ""
    random = ""
    # ftpUtils = FTPTransferImpl()
    xpath_prtryCode = "(//Prtry/Cd)[{0}]"
    xpath_RealAcctId = "//Stmt//Acct/Id//Othr/Id"
    xpath_DbtrAcct = "(//UltmtDbtr//Othr/Id)[{0}]"
    xpath_CdtrAcct = "(//UltmtCdtr//Othr/Id)[{0}]"
    xpath_SubFmlyCd = "(//Fmly/SubFmlyCd)[{0}]"

    iBANFlag = True
    doc = minidom.Document()

    def generateCAMT053(self):
        iBANFlag = ""
        outputFileName = "AutoCAMT053" + Util.get_unique_number(5)
        random = "MSG-" + date.today().isoformat()

        CAMT053InputData.Random = random + "-" + Util.get_unique_number(5)
        CAMT053InputData.date = datetime.today().isoformat()
        CAMT053InputData.Dt = date.today().isoformat()

        Root = self.initiateXML()
        # tree = ElementTree(Root)
        BkToCstmrStmt = Element(CAMT053Tags.BkToCstmrStmtTag)
        Root.append(BkToCstmrStmt)

        self.createGrpHdr(BkToCstmrStmt)
        self.createStmt(BkToCstmrStmt)

        print(etree.tostring(Root))

    def initiateXML(self):
        rootElement = Element("Document")
        tree = ElementTree(rootElement)
        rootElement.set("xmlns", "urn:iso:std:iso:20022:tech:xsd:camt.053.001.02")
        rootElement.set("xmlns:xsd", "http://www.w3.org/2000/xmlns/")
        rootElement.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        return rootElement

    def createGrpHdr(self, BkToCstmrStmt):

        # GrpHdr
        grpHdr = Element(CAMT053Tags.GrpHdrTag)
        BkToCstmrStmt.append(grpHdr)
        msgID = Element(CAMT053Tags.MsgIdTag)
        msgID.text = CAMT053InputData.Random
        grpHdr.append(msgID)
        CreDtTm = Element(CAMT053Tags.CreDtTmTag)
        grpHdr.append(CreDtTm)

        # MsgRcpt
        MsgRcpt = Element(CAMT053Tags.MsgRcptTag)
        grpHdr.append(MsgRcpt)
        nmt = Element(CAMT053Tags.NmTag)
        nmt.text = CAMT053InputData.nm
        MsgRcpt.append(nmt)

        # PstlAdr
        PstlAdr = Element(CAMT053Tags.PstlAdrTag)
        MsgRcpt.append(PstlAdr)

        StrtNm = Element(CAMT053Tags.StrtNmTag)
        StrtNm.text = CAMT053InputData.StrtNm
        PstlAdr.append(StrtNm)

        BldgNb = Element(CAMT053Tags.BldgNbTag)
        BldgNb.text = CAMT053InputData.BldgNb
        PstlAdr.append(BldgNb)

        PstCd = Element(CAMT053Tags.PstCdTag)
        PstCd.text = CAMT053InputData.PstCd
        PstlAdr.append(PstCd)

        TwnNm = Element(CAMT053Tags.TwnNmTag)
        TwnNm.text = CAMT053InputData.TwnNm
        PstlAdr.append(TwnNm)

        Ctry = Element(CAMT053Tags.CtryTag)
        Ctry.text = CAMT053InputData.Ctry
        PstlAdr.append(Ctry)

        AdrLine = Element(CAMT053Tags.AdrLineTag)
        AdrLine.text = CAMT053InputData.AdrLine
        PstlAdr.append(AdrLine)

        # ID
        Id1 = Element(CAMT053Tags.IdTag)
        MsgRcpt.append(Id1)

        OrgId = Element(CAMT053Tags.OrgIdTag)
        Id1.append(OrgId)

        BICOrBEI = Element(CAMT053Tags.BICOrBEITag)
        BICOrBEI.text = CAMT053InputData.BICOrBEI
        OrgId.append(BICOrBEI)

        Othr = Element(CAMT053Tags.OthrTag)
        OrgId.append(Othr)

        Id2 = Element(CAMT053Tags.IdTag)
        Id2.text = CAMT053InputData.GrpHdr_Other_ID
        Othr.append(Id2)

        # MsgPgntn
        MsgPgntn = Element(CAMT053Tags.MsgPgntnTag)
        grpHdr.append(MsgPgntn)

        PgNb = Element(CAMT053Tags.PgNbTag)
        PgNb.text = CAMT053InputData.PgNb
        MsgPgntn.append(PgNb)

        LastPgInd = Element(CAMT053Tags.LastPgIndTag)
        LastPgInd.text = CAMT053InputData.LastPgInd
        MsgPgntn.append(LastPgInd)
        # return BkToCstmrStmt

    def createStmt(self, BkToCstmrStmt):

        Stmt = Element(CAMT053Tags.StmtTag)
        BkToCstmrStmt.append(Stmt)

        # Stmt
        Id = Element(CAMT053Tags.IdTag)
        Id.text = CAMT053InputData.Random
        Stmt.append(Id)

        ElctrncSeqNb = Element(CAMT053Tags.ElctrncSeqNbTag)
        ElctrncSeqNb.text = CAMT053InputData.ElctrncSeqNb
        Stmt.append(ElctrncSeqNb)

        CreDtTm = Element(CAMT053Tags.CreDtTmTag)
        CreDtTm.text = CAMT053InputData.date
        Stmt.append(CreDtTm)

        self.createAccount(Stmt)
        self.createBalanceCredit(Stmt)
        self.createTxsSummry(Stmt)
        self.createNtry(Stmt)
        # return BkToCstmrStmt

    def createAccount(self, Stmt):
        # Acct
        Acct = Element(CAMT053Tags.AcctTag)
        Stmt.append(Acct)

        Id = Element(CAMT053Tags.IdTag)
        Acct.append(Id)

        Othr = Element(CAMT053Tags.OthrTag)
        Id.append(Othr)

        Id2 = Element(CAMT053Tags.IdTag)
        Id2.text = CAMT053InputData.Acct_ID
        Othr.append(Id2)

        Ccy = Element(CAMT053Tags.CcyTag)
        Ccy.text = CAMT053InputData.Ccy
        Acct.append(Ccy)

        Svcr = Element(CAMT053Tags.SvcrTag)
        Acct.append(Svcr)

        FinInstnId = Element(CAMT053Tags.FinInstnIdTag)
        Svcr.append(FinInstnId)

        BIC = Element(CAMT053Tags.BICTag)
        BIC.text = CAMT053InputData.BIC
        FinInstnId.append(BIC)

    def createBalanceCredit(self, Stmt):
        Bal_Cd = ""
        Amount = ""

        Bal = Element(CAMT053Tags.BalTag)
        Stmt.append(Bal)

        Tp = Element(CAMT053Tags.TpTag)
        Bal.append(Tp)

        CdOrPrtry = Element(CAMT053Tags.CdOrPrtryTag)
        Tp.append(CdOrPrtry)

        Cd = Element(CAMT053Tags.CdTag)
        Cd.text = Bal_Cd
        CdOrPrtry.append(Cd)

        Amt = Element(CAMT053Tags.AmtTag)
        Amt.text = Amount
        Bal.append(Amt)

        # set attribute to Amt
        Attr = Element(CAMT053Tags.CcyTag)
        Attr.set(CAMT053Tags.CcyTag, "NOK")

        CdtDbtInd = Element(CAMT053Tags.CdtDbtIndTag)
        CdtDbtInd.text = "CRDT"
        Bal.append(CdtDbtInd)

        Dt1 = Element(CAMT053Tags.DtTag)
        Bal.append(Dt1)

        Dt2 = Element(CAMT053Tags.DtTag)
        Dt2.text = CAMT053InputData.Dt
        Dt1.append(Dt2)

    def createTxsSummry(self, Stmt):
        if CAMT053InputData.TxsSummry == "Yes":
            # TxsSummry
            TxsSummry = Element(CAMT053Tags.TxsSummryTag)
            Stmt.append(TxsSummry)

            # TtlNtries
            TtlNtries = Element(CAMT053Tags.TtlNtriesTag)
            TxsSummry.append(TtlNtries)

            NbOfNtries = Element(CAMT053Tags.NbOfNtriesTag)
            NbOfNtries.text = CAMT053InputData.NbOfNtries
            TtlNtries.append(NbOfNtries)

            NbOfNtriesSum = Element(CAMT053Tags.SumTag)
            NbOfNtriesSum.text = CAMT053InputData.NbOfNtries_Sum
            TtlNtries.append(NbOfNtriesSum)

            if CAMT053InputData.Txs_Credit == 1 and CAMT053InputData.Txs_Debit == 0:
                # TtlCdtNtries
                TtlCdtNtries = Element(CAMT053Tags.TtlCdtNtriesTag)
                TxsSummry.append(TtlCdtNtries)

                TtlCdtNtries_NbOfNtries = Element(CAMT053Tags.NbOfNtriesTag)
                TtlCdtNtries_NbOfNtries.text = CAMT053InputData.TtlCdtNtries
                TtlCdtNtries.append(TtlCdtNtries_NbOfNtries)

                TtlCdtNtriesSum = Element(CAMT053Tags.SumTag)
                TtlCdtNtriesSum.text = CAMT053InputData.TtlCdtNtries_Sum
                TtlCdtNtries.append(TtlCdtNtriesSum)

                # TtlDbtNtries
                TtlDbtNtries = Element(CAMT053Tags.TtlDbtNtriesTag)
                TxsSummry.append(TtlDbtNtries)

                TtlDbtNtries_NbOfNtries = Element(CAMT053Tags.NbOfNtriesTag)
                TtlDbtNtries_NbOfNtries.text = "0"
                TtlDbtNtries.append(TtlDbtNtries_NbOfNtries)

                TtlDbtNtriesSum = Element(CAMT053Tags.SumTag)
                TtlDbtNtriesSum.text = "0"
                TtlDbtNtries.append(TtlDbtNtriesSum)

                TtlDbtNtries = Element(CAMT053Tags.TtlDbtNtriesTag)
                TxsSummry.append(TtlDbtNtries)

                TtlDbtNtries_NbOfNtries = Element(CAMT053Tags.NbOfNtriesTag)
                TtlDbtNtries_NbOfNtries.text = CAMT053InputData.NbOfNtries
                TtlDbtNtries.append(TtlDbtNtries_NbOfNtries)

                TtlDbtNtriesSum = Element(CAMT053Tags.SumTag)
                TtlDbtNtriesSum.text = CAMT053InputData.NbOfNtries_Sum
                TtlDbtNtries.append(TtlDbtNtriesSum)

            elif CAMT053InputData.Txs_Credit == 0 and CAMT053InputData.Txs_Debit == 1:
                # TtlCdtNtries
                TtlCdtNtries = Element(CAMT053Tags.TtlCdtNtriesTag)
                TxsSummry.append(TtlCdtNtries)

                TtlCdtNtries_NbOfNtries = Element(CAMT053Tags.NbOfNtriesTag)
                TtlCdtNtries_NbOfNtries.text = "0"
                TtlCdtNtries.append(TtlCdtNtries_NbOfNtries)

                TtlCdtNtriesSum = Element(CAMT053Tags.SumTag)
                TtlCdtNtriesSum.text = "0"
                TtlCdtNtries.append(TtlCdtNtriesSum)

                # TtlDbtNtries
                TtlDbtNtries = Element(CAMT053Tags.TtlDbtNtriesTag)
                TxsSummry.append(TtlDbtNtries)

                TtlDbtNtries_NbOfNtries = Element(CAMT053Tags.NbOfNtriesTag)
                TtlDbtNtries_NbOfNtries.text = CAMT053InputData.NbOfNtries
                TtlDbtNtries.append(TtlDbtNtries_NbOfNtries)

                TtlDbtNtriesSum = Element(CAMT053Tags.SumTag)
                TtlDbtNtriesSum.text = CAMT053InputData.NbOfNtries_Sum
                TtlDbtNtries.append(TtlDbtNtriesSum)

    def createNtry(self, Stmt):
        temp = CAMT053InputData.Random
        # var = int(temp[temp - 1])
        var = 0

        if self.multiple == False:
            if CAMT053InputData.Ntry_Credit >= 1:
                i = 0
                while i < CAMT053InputData.Ntry_Credit:
                    var = var + 1

                    # Ntry
                    Ntry = Element(CAMT053Tags.NtryTag)
                    Stmt.append(Ntry)

                    NtryRef = Element(CAMT053Tags.NtryRefTag)
                    NtryRef.text = self.random + "-" + str(var)
                    Ntry.append(NtryRef)

                    Amt = Element(CAMT053Tags.AmtTag)
                    Amt.text = CAMT053InputData.Ntry_Credit_Amt
                    Ntry.append(Amt)

                    # set attribute to Amt
                    Attr = Element(CAMT053Tags.CcyTag)
                    Attr.set(CAMT053InputData.Ntry_Credit_Ccy, "NOK")

                    CdtDbtInd = Element(CAMT053Tags.CdtDbtIndTag)
                    CdtDbtInd.text = "CRDT"
                    Ntry.append(CdtDbtInd)

                    Sts = Element(CAMT053Tags.StsTag)
                    Sts.text = CAMT053InputData.Sts
                    Ntry.append(Sts)

                    BookgDt = Element(CAMT053Tags.BookgDtTag)
                    Ntry.append(BookgDt)

                    Dt = Element(CAMT053Tags.DtTag)
                    Dt.text = CAMT053InputData.Dt
                    BookgDt.append(Dt)

                    ValDt = Element(CAMT053Tags.ValDtTag)
                    Ntry.append(ValDt)

                    Dt2 = Element(CAMT053Tags.DtTag)
                    Dt2.text = CAMT053InputData.Dt
                    ValDt.append(Dt2)

                    AcctSvcrRef = Element(CAMT053Tags.AcctSvcrRefTag)
                    AcctSvcrRef.text = CAMT053InputData.Random
                    Ntry.append(AcctSvcrRef)

                    # BkTxCd
                    BkTxCd = Element(CAMT053Tags.BkTxCdTag)
                    Ntry.append(BkTxCd)

                    Domn = Element(CAMT053Tags.DomnTag)
                    BkTxCd.append(Domn)

                    BkTxCd_Cd = Element(CAMT053Tags.CdTag)
                    BkTxCd_Cd.text = CAMT053InputData.BkTxCd_Cd
                    Domn.append(BkTxCd_Cd)

                    Fmly = Element(CAMT053Tags.FmlyTag)
                    Domn.append(Fmly)

                    Fmly_Cd = Element(CAMT053Tags.FmlyCdTag)
                    Fmly_Cd.text = CAMT053InputData.Fmly_Cd
                    Fmly.append(Fmly_Cd)

                    SubFmlyCd = Element(CAMT053Tags.SubFmlyCdTag)
                    SubFmlyCd.text = CAMT053InputData.SubFmlyCd
                    Fmly.append(SubFmlyCd)

                    Prtry = Element(CAMT053Tags.PrtryTag)
                    BkTxCd.append(Prtry)

                    Prtry_Cd = Element(CAMT053Tags.Prtry_CdTag)
                    Prtry_Cd.text = CAMT053InputData.Prtry_Cd
                    Prtry.append(Prtry_Cd)

                    Issr = Element(CAMT053Tags.IssrTag)
                    Issr.text = CAMT053InputData.Issr
                    Prtry.append(Issr)

                    self.createCrdtNtryDtls(Ntry)
            if CAMT053InputData.Ntry_Debit >= 1:
                for i in CAMT053InputData.Ntry_Debit:
                    var = var + 1
                    # Ntry
                    Ntry = Element(CAMT053Tags.NtryTag)
                    Stmt.append(Ntry)

                    NtryRef = Element(CAMT053Tags.NtryRefTag)
                    NtryRef.text = self.random + "-" + var
                    Ntry.append(NtryRef)

                    Amt = Element(CAMT053Tags.AmtTag)
                    Amt.text = CAMT053InputData.Ntry_Debit_Amt
                    Ntry.append(Amt)

                    # set attribute to Amt
                    Attr = Element(CAMT053Tags.CcyTag)
                    Attr.set(CAMT053InputData.Ntry_Credit_Ccy, "NOK")

                    CdtDbtInd = Element(CAMT053Tags.CdtDbtIndTag)
                    CdtDbtInd.text = "DBIT"
                    Ntry.append(CdtDbtInd)

                    Sts = Element(CAMT053Tags.StsTag)
                    Sts.text = CAMT053InputData.Sts
                    Ntry.append(Sts)

                    BookgDt = Element(CAMT053Tags.BookgDtTag)
                    Ntry.append(BookgDt)

                    Dt = Element(CAMT053Tags.DtTag)
                    Dt.text = CAMT053InputData.Dt
                    BookgDt.append(Dt)

                    ValDt = Element(CAMT053Tags.ValDtTag)
                    Ntry.append(ValDt)

                    Dt2 = Element(CAMT053Tags.DtTag)
                    Dt2.text = CAMT053InputData.Dt
                    ValDt.append(Dt2)

                    AcctSvcrRef = Element(CAMT053Tags.AcctSvcrRefTag)
                    AcctSvcrRef.text = CAMT053InputData.Random
                    Ntry.append(AcctSvcrRef)

                    # BkTxCd
                    BkTxCd = Element(CAMT053Tags.BkTxCdTag)
                    Ntry.append(BkTxCd)

                    Domn = Element(CAMT053Tags.DomnTag)
                    BkTxCd.append(Domn)

                    BkTxCd_Cd = Element(CAMT053Tags.CdTag)
                    BkTxCd_Cd.text = CAMT053InputData.BkTxCd_Cd
                    Domn.append(BkTxCd_Cd)

                    Fmly = Element(CAMT053Tags.FmlyTag)
                    Domn.append(Fmly)

                    Fmly_Cd = Element(CAMT053Tags.FmlyCdTag)
                    Fmly_Cd.text = CAMT053InputData.Fmly_Cd
                    Fmly.append(Fmly_Cd)

                    SubFmlyCd = Element(CAMT053Tags.SubFmlyCdTag)
                    SubFmlyCd.text = CAMT053InputData.SubFmlyCd
                    Fmly.append(SubFmlyCd)

                    Prtry = Element(CAMT053Tags.PrtryTag)
                    BkTxCd.append(Prtry)

                    Prtry_Cd = Element(CAMT053Tags.Prtry_CdTag)
                    Prtry_Cd.text = CAMT053InputData.Prtry_Cd
                    Prtry.append(Prtry_Cd)

                    Issr = Element(CAMT053Tags.IssrTag)
                    Issr.text = CAMT053InputData.Issr
                    Prtry.append(Issr)

                    self.createDbtrNtryDtls(Ntry)
        elif self.multiple != False:
            if CAMT053InputData.Txs_Credit != 0:
                # Ntry
                Ntry = Element(CAMT053Tags.NtryTag)
                Stmt.append(Ntry)

                NtryRef = Element(CAMT053Tags.NtryRefTag)
                NtryRef.text = CAMT053InputData.Random
                Ntry.append(NtryRef)

                Amt = Element(CAMT053Tags.AmtTag)
                Amt.text = CAMT053InputData.TtlCdtNtries_Sum
                Ntry.append(Amt)
                # set attribute to Amt
                Attr = Element(CAMT053Tags.CcyTag)
                Attr.set(CAMT053InputData.Ntry_Credit_Ccy, "NOK")

                CdtDbtInd = Element(CAMT053Tags.CdtDbtIndTag)
                CdtDbtInd.text = "CRDT"
                Ntry.append(CdtDbtInd)

                Sts = Element(CAMT053Tags.StsTag)
                Sts.text = CAMT053InputData.Sts
                Ntry.append(Sts)

                BookgDt = Element(CAMT053Tags.BookgDtTag)
                Ntry.append(BookgDt)

                Dt = Element(CAMT053Tags.DtTag)
                Dt.text = CAMT053InputData.Dt
                BookgDt.append(Dt)

                ValDt = Element(CAMT053Tags.ValDtTag)
                Ntry.append(ValDt)

                Dt2 = Element(CAMT053Tags.DtTag)
                Dt2.text = CAMT053InputData.Dt
                ValDt.append(Dt2)

                AcctSvcrRef = Element(CAMT053Tags.AcctSvcrRefTag)
                AcctSvcrRef.text = CAMT053InputData.Random
                Ntry.append(AcctSvcrRef)

                # BkTxCd
                BkTxCd = Element(CAMT053Tags.BkTxCdTag)
                Ntry.append(BkTxCd)

                Domn = Element(CAMT053Tags.DomnTag)
                BkTxCd.append(Domn)

                BkTxCd_Cd = Element(CAMT053Tags.CdTag)
                BkTxCd_Cd.text = CAMT053InputData.BkTxCd_Cd
                Domn.append(BkTxCd_Cd)

                Fmly = Element(CAMT053Tags.FmlyTag)
                Domn.append(Fmly)

                Fmly_Cd = Element(CAMT053Tags.FmlyCdTag)
                Fmly_Cd.text = CAMT053InputData.Fmly_Cd
                Fmly.append(Fmly_Cd)

                SubFmlyCd = Element(CAMT053Tags.SubFmlyCdTag)
                SubFmlyCd.text = CAMT053InputData.SubFmlyCd
                Fmly.append(SubFmlyCd)

                Prtry = Element(CAMT053Tags.PrtryTag)
                BkTxCd.append(Prtry)

                Prtry_Cd = Element(CAMT053Tags.Prtry_CdTag)
                Prtry_Cd.text = CAMT053InputData.Prtry_Cd
                Prtry.append(Prtry_Cd)

                Issr = Element(CAMT053Tags.IssrTag)
                Issr.text = CAMT053InputData.Issr
                Prtry.append(Issr)
                self.createCrdtNtryDtls(Ntry)
            elif CAMT053InputData.Txs_Debit != 0:
                # Ntry
                Ntry = Element(CAMT053Tags.NtryTag)
                Stmt.append(Ntry)

                NtryRef = Element(CAMT053Tags.NtryRefTag)
                NtryRef.text = CAMT053InputData.Random
                Ntry.append(NtryRef)

                Amt = Element(CAMT053Tags.AmtTag)
                Amt.text = CAMT053InputData.TtlCdtNtries_Sum
                Ntry.append(Amt)

                # set attribute to Amt
                Attr = Element(CAMT053Tags.CcyTag)
                Attr.set(CAMT053InputData.Ntry_Credit_Ccy, "NOK")

                CdtDbtInd = Element(CAMT053Tags.CdtDbtIndTag)
                CdtDbtInd.text = "DBIT"
                Ntry.append(CdtDbtInd)

                Sts = Element(CAMT053Tags.StsTag)
                Sts.text = CAMT053InputData.Sts
                Ntry.append(Sts)

                BookgDt = Element(CAMT053Tags.BookgDtTag)
                Ntry.append(BookgDt)

                Dt = Element(CAMT053Tags.DtTag)
                Dt.text = CAMT053InputData.Dt
                BookgDt.append(Dt)

                ValDt = Element(CAMT053Tags.ValDtTag)
                Ntry.append(ValDt)

                Dt2 = Element(CAMT053Tags.DtTag)
                Dt2.text = CAMT053InputData.Dt
                ValDt.append(Dt2)

                AcctSvcrRef = Element(CAMT053Tags.AcctSvcrRefTag)
                AcctSvcrRef.text = CAMT053InputData.Random
                Ntry.append(AcctSvcrRef)

                # BkTxCd
                BkTxCd = Element(CAMT053Tags.BkTxCdTag)
                Ntry.append(BkTxCd)

                Domn = Element(CAMT053Tags.DomnTag)
                BkTxCd.append(Domn)

                BkTxCd_Cd = Element(CAMT053Tags.CdTag)
                BkTxCd_Cd.text = CAMT053InputData.BkTxCd_Cd
                Domn.append(BkTxCd_Cd)

                Fmly = Element(CAMT053Tags.FmlyTag)
                Domn.append(Fmly)

                Fmly_Cd = Element(CAMT053Tags.FmlyCdTag)
                Fmly_Cd.text = CAMT053InputData.Fmly_Cd
                Fmly.append(Fmly_Cd)

                SubFmlyCd = Element(CAMT053Tags.SubFmlyCdTag)
                SubFmlyCd.text = CAMT053InputData.SubFmlyCd
                Fmly.append(SubFmlyCd)

                Prtry = Element(CAMT053Tags.PrtryTag)
                BkTxCd.append(Prtry)

                Prtry_Cd = Element(CAMT053Tags.Prtry_CdTag)
                Prtry_Cd.text = CAMT053InputData.Prtry_Cd
                Prtry.append(Prtry_Cd)

                Issr = Element(CAMT053Tags.IssrTag)
                Issr.text = CAMT053InputData.Issr
                Prtry.append(Issr)
                self.createDbtrNtryDtls(Ntry)

    def createCrdtNtryDtls(self, Ntry):
        NtryDtls = Element(CAMT053Tags.NtryDtlsTag)
        Ntry.append(NtryDtls)

        TxDtls = Element(CAMT053Tags.TxDtlsTag)
        NtryDtls.append(TxDtls)

        Refs = Element(CAMT053Tags.RefsTag)
        TxDtls.append(Refs)

        # Ref Inputs
        InstrId = Element(CAMT053Tags.InstrIdTag)
        InstrId.text = CAMT053InputData.InstrId
        Refs.append(InstrId)

        EndToEndId = Element(CAMT053Tags.EndToEndIdTag)
        EndToEndId.text = CAMT053InputData.Random
        Refs.append(EndToEndId)

        # RltdPties
        RltdPties = Element(CAMT053Tags.RltdPtiesTag)
        TxDtls.append(RltdPties)

        # Cdtr
        Cdtr = Element(CAMT053Tags.CdtrTag)
        RltdPties.append(Cdtr)
        Id0 = Element(CAMT053Tags.IdTag)
        Cdtr.append(Id0)

        if self.iBANFlag == True:
            PrvtId = Element(CAMT053Tags.PrvtIdTag)
            Id0.append(PrvtId)

            iban = Element(CAMT053Tags.iBANTag)
            iban.text = CAMT053InputData.InstrId
            PrvtId.append(iban)
        elif self.iBANFlag == False:
            OrgID = Element(CAMT053Tags.OrgIdTag)
            Id0.append(OrgID)

            OthrTag = Element(CAMT053Tags.OthrTag)
            OrgID.append(OthrTag)

            id = Element(CAMT053Tags.IdTag)
            id.text = CAMT053InputData.InstrId
            OthrTag.append(id)

        # RmtInf
        RmtInf = Element(CAMT053Tags.RmtInfTag)
        TxDtls.append(RmtInf)

        Ustrd = Element(CAMT053Tags.UstrdTag)
        Ustrd.text = CAMT053InputData.InstrId
        RmtInf.append(Ustrd)

    def createDbtrNtryDtls(self, Ntry):
        NtryDtls = Element(CAMT053Tags.NtryDtlsTag)
        Ntry.append(NtryDtls)

        TxDtls = Element(CAMT053Tags.TxDtlsTag)
        NtryDtls.append(TxDtls)

        Refs = Element(CAMT053Tags.RefsTag)
        TxDtls.append(Refs)

        # Ref Inputs
        InstrId = Element(CAMT053Tags.InstrIdTag)
        InstrId.text = CAMT053InputData.InstrId
        Refs.append(InstrId)

        EndToEndId = Element(CAMT053Tags.EndToEndIdTag)
        EndToEndId.text = CAMT053InputData.Random
        Refs.append(EndToEndId)

        # RltdPties
        RltdPties = Element(CAMT053Tags.RltdPtiesTag)
        TxDtls.append(RltdPties)

        # Cdtr
        Dbdtr = Element(CAMT053Tags.DbtrTag)
        RltdPties.append(Dbdtr)

        Id0 = Element(CAMT053Tags.IdTag)
        Dbdtr.append(Id0)
        if self.iBANFlag == True:
            PrvtId = Element(CAMT053Tags.PrvtIdTag)
            Id0.append(PrvtId)

            iban = Element(CAMT053Tags.iBANTag)
            iban.text = CAMT053InputData.InstrId
            PrvtId.append(iban)
        elif self.iBANFlag == False:
            OrgID = Element(CAMT053Tags.OrgIdTag)
            Id0.append(OrgID)

            OthrTag = Element(CAMT053Tags.OthrTag)
            OrgID.append(OthrTag)

            id = Element(CAMT053Tags.IdTag)
            id.text = CAMT053InputData.InstrId
            OthrTag.append(id)

        # RmtInf
        RmtInf = Element(CAMT053Tags.RmtInfTag)
        TxDtls.append(RmtInf)

        Ustrd = Element(CAMT053Tags.UstrdTag)
        Ustrd.text = CAMT053InputData.InstrId
        RmtInf.append(Ustrd)


realAccount = 55454854
transactionAccount = 4545454

cp = CAMT053FileProcessing()
cp.generateCAMT053()
