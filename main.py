import telebot
import os

telebot.apihelper.ENABLE_MIDDLEWARE = True
bot = telebot.TeleBot("1308963390:AAFCTIwHspIzuXdxaVshAMwp3GtsXE33Mnw")
cwd = os.getcwd()
components = [
    'base',
    'user',
    'admin',
]


for component in components:
    
    code = open(cwd + "/components/" + component + ".py").read()
    code = code.split("#-#")
    code = code[1].split("\n")
    code = "\n".join(code)
    
    exec(code)
    print("*** [{}] module loaded".format(component))
    
bot.polling()