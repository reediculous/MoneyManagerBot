import matplotlib.pyplot as plt


def createPie(reg, session):
    '''
    Создает круговую диаграмму доходов или расходов для указнной сессии
    '''
    size = []
    labels = []
    if reg == "income":
        cats = session.getIncomeCats()
        size = []
        for cat in cats:
            size.append(session.purse.getIncomeCatSummary(cat))
            labels.append(cat)
        print(size)
    elif reg == "spend":
        cats = session.getSpendCats()
        size = []
        for cat in cats:
            size.append(session.purse.getSpendCatSummary(cat))

    fig1, ax1 = plt.subplots()
    ax1.pie(size, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')
    plt.show()


def createBar():
    pass
