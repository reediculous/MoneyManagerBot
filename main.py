import telebot

from Purse import Purse
from Sessions import Session
from Categories import *
from Recording import *
from Plotter import *


def parseCommand(command):
    words = command.split(" ")
    commandName = words.pop(0)
    args = words
    return args


TOKEN = "1571840282:AAF0tklAuMCYmUJEFl7gQzAbEoTQ60xC1ls"
bot = telebot.TeleBot(TOKEN)

# Объявляем словарь сессий, где
# Ключ — id пользователя
# значения — экземпляр класса Session c информацией о пользователе
sessions = {}  # TODO: реализовать хранение данных в БД


@bot.message_handler(content_types=["text", "document"])
# TODO: добавить возможность взаимодействовать с ботом через клавиатуру
def start(message):
    user = message.from_user.id
    global sessions
    if message.text == "/start":  # Инициализирует новый пустой кошелек и новую сессию
        purse = Purse(user, [], [])
        IncomeCats = {}
        SpendCats = {}
        sessions[user] = Session(purse, IncomeCats, SpendCats)
        bot.send_message(user, "started your session")
    if message.text == "/cats":  # Отправляет информацию о категориях расходов и доходов
        bot.send_message(user, sessions[user].stringCats())
    if "/income" in message.text:  # Добавляет новую запись дохода
        args = parseCommand(message.text)
        cat = args[0]
        amount = args[1]
        if not cat in sessions[user].getIncomeCats():
            cat = IncomeCategory(cat)
            sessions[user].addIncomeCat(cat)
        else:
            cat = sessions[user].getIncomeCats()[cat]
        newRecord = Income(amount, cat)
        sessions[user].purse.addIncomeRecord(newRecord)
        bot.send_message(user, "done")
    if "/spent" in message.text:  # Добавляет новую запись расхода
        args = parseCommand(message.text)
        cat = args[0]
        amount = args[1]
        if not cat in sessions[user].getSpendCats():
            cat = SpendCategory(cat)
            sessions[user].addSpendCat(cat)
        else:
            cat = sessions[user].getSpendCats()[cat]
        newRecord = Spend(amount, cat)
        sessions[user].purse.addSpendRecord(newRecord)
        bot.send_message(user, "done")
    # TODO: сделать возможность узнать доход/расход/баланс за определенное время
    if message.text == "/suminc":  # Отправляет суммарный доход за все время
        bot.send_message(user, "TOTAL INCOME: " + str(sessions[user].purse.getIncomeSummary()))
    if message.text == "/sumsp":  # Отправляет суммарный расход за все время
        bot.send_message(user, "TOTAL SPENDINGS: " + str(sessions[user].purse.getSpendSummary()))
    if message.text == "/balance":  # Отправляет суммарный баланс
        bot.send_message(user, "TOTAL BALANCE: " + str(sessions[user].purse.getBalance()))
    if message.text == "/incpie":  # Строит диаграмму доходов по категориям
        createPie("income", sessions[user])
    # TODO: (Высший приоритет) добавить реализацию различных диаграмм и отправку их изображений пользователю


if __name__ == '__main__':
    bot.polling()
