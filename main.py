import requests
from datetime import datetime
import telebot 
from tokendata import TOKEN



def get_data():
    req= requests.get("https://yobit.net/api/3/ticker/btc_usd")
    response=req.json()
    print(response)
    sell_price = response["btc_usd"]["sell"]
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price: {sell_price}")

def telegram_bot(TOKEN):
    bot = telebot.TeleBot(TOKEN)

    @bot.message_handler(commands=["start"])
    def start_message(message):
      bot.send_message(message.chat.id, "Yo do u want to know the bitcoin price?")

    @bot.message_handler(content_types=["text"])
    def send_text(message):
        if message.text.lower()=="/price":
            try:
                req= requests.get("https://yobit.net/api/3/ticker/btc_usd")
                response=req.json()
                sell_price = response["btc_usd"]["sell"]
                def  toFixed (sell_price, digits=3):
                    return f"{sell_price:.{digits}f}"
                bot.send_message(
                    message.chat.id, 
                    f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nBTC - USD\nSell BTC price: ${sell_price}"

                )
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    "Something was wrong..."
                )
        else:
            bot.send_message(
                    message.chat.id,
                    "Please, check commands")
            
    bot.polling()

if __name__ =='__main__':
    #get_data()
    telegram_bot(TOKEN)