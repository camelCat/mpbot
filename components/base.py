import telebot
bot = telebot.TeleBot("")
#-#
import yaml
from telebot import apihelper




@bot.middleware_handler(update_types = ['message'])
def meta(bot_instance, msg):
    
    username = msg.from_user.username
    # Show the request in terminal
    print(username + ": " + msg.text)

    # Assess the user's level of permission
    global status
    with open('roles.yaml') as f:
        roles = yaml.load(f, Loader=yaml.FullLoader)
        if username in roles.keys():
            status = roles[username]['role']
        else:
            status = 'user'


#-#
    print(status)