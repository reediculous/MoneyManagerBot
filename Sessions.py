class Session:
    def __init__(self, purse, incCategories, spCategories):
        self.purse = purse
        self.__incCats = incCategories
        self.__spCats = spCategories

    def getIncomeCats(self):
        return self.__incCats

    def getSpendCats(self):
        return self.__spCats

    def addIncomeCat(self, cat):
        self.__incCats[cat.getName()] = cat

    def addSpendCat(self, cat):
        self.__spCats[cat.getName()] = cat

    def stringCats(self):
        '''
        Формирует сообщение о существующих категориях
        '''
        sb = "INCOME:\n"
        for cat in self.__incCats:
            sb += cat + "\n"
        sb += "---\n"
        sb += "SPENDINGS:\n"
        for cat in self.__spCats:
            sb += cat + "\n"
        return sb