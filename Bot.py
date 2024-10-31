import telebot
bot = telebot.TeleBot('7573172744:AAGi6UeABlD6ah9DrCWZ9faIJwhPtrlRKvY')

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

bot.polling()