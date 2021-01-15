import telebot
bot = telebot.TeleBot("")
status = 1
#-#


@bot.message_handler(func=lambda statls: status!="admin")
def admin_access(msg):
    bot.send_message(msg.from_user.id, "Error400")
    print()


@bot.message_handler(commands=['addadmin'])
def addadmin(msg):
    message = msg.text.split()
    syntax = "/addadmin <user id>"

    if len(message) != 2:
        bot.send_message(msg.from_user.id, "Wrong syntax (" + syntax + ")")
