from kucoin.client import Client
import time
import datetime
import telegram
import asyncio

api_key = '652ba5004e791f0001d2c9cd'
api_secret = '11e05bd3-fc05-4510-98d6-a4f1d1d1af3a'
api_passphrase = 'scuolA2017!'

my_token = '6470866156:AAGXHrLD2Z5lhZTUOVhZAlsk_1MQjd8XNME'
chat_id = -1001985855189

client = Client(api_key, api_secret, api_passphrase)

symbols = client.get_symbols()
simboliusdt = []

for index, symbol in enumerate(symbols):
        if 'USDT' in symbols[index]["symbol"]:
            simboliusdt.append(symbols[index]["symbol"])

hourSignal = []
dailySignal = []
start = datetime.datetime.now().minute

async def send(msg, chat_id, token):
    bot = telegram.Bot(token)
    await bot.sendMessage(chat_id,msg)
    print('Message Sent!')

while True:
    now = datetime.datetime.now().minute
    if now > start:
        stringa = 'Controllare: ',hourSignal
        asyncio.run(send(stringa,chat_id,my_token))
        print('open position/send message')
        start=start+1
    print(datetime.datetime.now().minute)
    for index, symbol in enumerate(simboliusdt):
        data = client.get_kline_data(simboliusdt[index], '1hour')
        try:
            Past1Hvol =  int(float(data[1][6]))
            actual = int(float(data[0][6]))
            Min1Hpast =  float(data[1][4])
            MinNow = float(data[0][4])
            if MinNow > Min1Hpast:
                if Past1Hvol > 300 and actual > Past1Hvol*10 or Past1Hvol > 20 and actual > Past1Hvol*50:
                    if simboliusdt[index] not in hourSignal:
                        hourSignal.append(simboliusdt[index])
        except:
            print("Kucoin Error")
    print(datetime.datetime.now().minute)
    
    

