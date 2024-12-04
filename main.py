import token

import telebot
from keyboards import main_keyboard
from handlers import register_handlers
from utils import get_token

token=get_token()
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard1 = main_keyboard()
    bot.send_message(message.chat.id, "Доброго дня! Нажміть на 'Вибрати книгу по жанру жанр' щоб обрати жанр.",
                     reply_markup=keyboard1)


# Реєструємо обробники
register_handlers(bot)

if __name__ == "__main__":
    bot.polling()