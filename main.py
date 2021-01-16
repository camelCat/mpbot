import telebot
import os
from sys import argv

telebot.apihelper.ENABLE_MIDDLEWARE = True

cwd = os.getcwd()

components = [
    'base',
    'user',
    'admin',
]
test_key = "1308963390:AAFCTIwHspIzuXdxaVshAMwp3GtsXE33Mnw"
deploy_key = "1566427814:AAE11a1uGVDf15W__m2bpCCrLf2DJunR2So"

if len(argv) == 1 or argv[1] == 'deploy':
    bot = telebot.TeleBot(deploy_key)
elif argv[1] == 'test':
    bot = telebot.TeleBot(test_key)
    components.insert(1, 'test')
    print(components)


for component in components:
    
    code = open(cwd + "/components/" + component + ".py").read()
    code = code.split("#-#")
    code = code[1].split("\n")
    code = "\n".join(code)
    
    exec(code)
    print("*** [{}] module loaded".format(component))
    
bot.polling()