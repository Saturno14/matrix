import telepot
import psutil
import time
import socket
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup

def greenSquare():
    return u'\U00002705'
def redSquare():
    return u'\U0000274C'
def alfoId():
    return "905942017"
def alfoUsername():
    return "@Saturno14xd"
def botToken():
    return "1517149691:AAGFFQ8DHq-Y771e_ywf8LiKJVATICRtlDE"

def notifyTelegramPoint():
    bot.sendMessage(alfoId(), '.')

def waitForInternetConnection():
    try:
        host = socket.gethostbyname("www.google.com")
        s = socket.create_connection((host, 80), 2)
        return True
    except:
        pass
    return False


def sblocco(): 
    blocco = 0
    print(blocco)

def blocco(): 
    blocco = 1
    print(blocco)
    
    
def handle(msg): 
    contentType, chatType, chatId = telepot.glance(msg)
    text = msg['text'].upper()
    if not (chatId ==905942017):
        bot.sendMessage(chatId, "Non sono tenuto a parlare con te")
        bot.sendMessage(alfoId(), 'Wuaglió qualcuno mi ha scritto... Ecco cosa:\n' + msg)
    elif(text == 'BLOCCO'):
        blocco()
        notifyTelegramPoint()
    elif(text == 'SBLOCCO'):
        sblocco()
        notifyTelegramPoint()
   

        
time.sleep(10)
waitForInternetConnection()
bot = telepot.Bot(botToken())
MessageLoop(bot, handle).run_as_thread()
keyboard = ReplyKeyboardMarkup(keyboard=[['BLOCCO','SBLOCCO'] ])
bot.sendMessage(alfoId(), 'wO.Ow', reply_markup=keyboard)
while 1:
    time.sleep(10)