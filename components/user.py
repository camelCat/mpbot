import telebot
bot = telebot.TeleBot("")
#-#
@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(msg.from_user.id, 'Welcome')
    