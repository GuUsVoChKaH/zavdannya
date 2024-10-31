import telebot
bot = telebot.TeleBot('7320488187:AAEBETxflKu2O3uyL_xhDZQBC1LakEPzHKw')

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

bot.polling()