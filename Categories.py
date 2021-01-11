class Category:
    def __init__(self, name):
        self.__name = name

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name


class SpendCategory(Category):
    type = "spend"

    def __init__(self, name):
        Category.__init__(self, name)


class IncomeCategory(Category):
    type = "income"

    def __init__(self, name):
        Category.__init__(self, name)
