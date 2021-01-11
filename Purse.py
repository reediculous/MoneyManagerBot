class Purse:
    def __init__(self, owner, incRecords, spRecords):
        self.__balance = 0
        self.__increcords = incRecords
        self.__sprecords = spRecords
        self.__owner = owner

    def setOwner(self, owner):
        self.__owner = owner

    def getOwner(self):
        return self.__owner

    def getIncomeRecords(self):
        return self.__increcords

    def getSpendRecords(self):
        return self.__sprecords

    def getBalance(self):
        return self.__balance

    def addIncomeRecord(self, record):
        self.__increcords.append(record)
        self.__balance += record.getAmount()

    def addSpendRecord(self, record):
        self.__sprecords.append(record)
        self.__balance -= record.getAmount()

    def getIncomeSummary(self):
        s = 0
        for inc in self.__increcords:
            s += inc.getAmount()
        return str(s)

    def getIncomeCatSummary(self, cat):
        s = 0
        for inc in self.__increcords:
            if inc.getCategory().getName() == cat:
                s += inc.getAmount()
        return s

    def getSpendCatSummary(self, cat):
        s = 0
        for sp in self.__sprecords:
            if sp.getCategory().getName() == cat:
                s += sp.getAmount()
        return s

    def getSpendSummary(self):
        s = 0
        for sp in self.__sprecords:
            s += sp.getAmount()
        return str(s)
