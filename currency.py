db_currency = ([])

def currency(name,price):
    pass

def addCurrency(name):
    async def on_message(message):
        if message.content == "!addcurrency":
            db_currency.append([name])
        pass

def removeCurrency(name):
    pass
