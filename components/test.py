import telebot
bot = telebot.TeleBot("")
#-#
@bot.message_handler(commands=['deploy'])
def complete_test(msg):
    bot.send_message(msg.from_user.id, "Deploying on server...")
    bot.stop_polling()
    exit(0)