import datetime


class Record:
    def __init__(self, amount, category, time=datetime.datetime.now(), comment=None):
        self.__time = time
        if isinstance(amount, str):
            amount = float(amount)
        self.__amount = amount
        self.__category = category
        self.comment = comment

    def setTime(self, time):
        self.__time = time

    def getTime(self):
        return self.__time

    def setAmount(self, amount):
        if isinstance(amount, str):
            amount = float(amount)
        self.__amount = amount

    def getAmount(self):
        return self.__amount

    def setCategory(self, cat):
        self.__category = cat

    def getCategory(self):
        return self.__category

    def setComment(self, comm):
        self.comment = comm

    def getComment(self):
        return self.comment


class Spend(Record):
    def __init__(self, amount, category, time=datetime.datetime.now(), comment=None):
        Record.__init__(self, amount, category, time, comment)


class Income(Record):
    def __init__(self, amount, category, time=datetime.datetime.now(), comment=None):
        Record.__init__(self, amount, category, time, comment)
