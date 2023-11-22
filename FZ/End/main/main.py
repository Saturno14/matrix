
import threading
import mouse
import time
import telepot
import psutil
import time
import socket
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup
import subprocess
import sys

#------------------------------------------------------------------------------------

def block ():
    global executing
    executing = True

    def move_mouse():
        #until executing is False, move mouse to (1,0)
        global executing
        while executing:
            mouse.move(950,500, absolute=True, duration=0)

    threading.Thread(target=move_mouse).start()

#------------------------------------------------------------------------------------
def sblock ():
    global executing
    executing = True

    def stop_infinite_mouse_control():
        #stops infinite control of mouse after 10 seconds if program fails to execute
        global executing
        executing = False

    threading.Thread(target=stop_infinite_mouse_control).start()
#------------------------------------------------------------------------------------
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
    sblock()

def blocco(): 
    block()
    
    
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
subprocess.check_call([sys.executable,'C:\matrix\matrix\dist\matrix'])
while 1:
    time.sleep(10)
#-------------------------------------------------------------------------------------------------------------------

