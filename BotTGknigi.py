import telebot
import random

bot = telebot.TeleBot('7573172744:AAGi6UeABlD6ah9DrCWZ9faIJwhPtrlRKvY')

@bot.message_handler(commands=['start'])
def start(message):
    keyboard1 = keyboard()
    bot.send_message(message.chat.id, "Доброго дня! Нажміть на 'Вибрати' щоб отримати рандомну книгу", reply_markup=keyboard1)
    keyboard()

def keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)

    button1 = telebot.types.KeyboardButton(text="Вибрати")
    keyboard.add(button1)
    return keyboard

def get_random_link():
    with open('links.txt', 'r') as file:  
        links = file.readlines()          
    return random.choice(links).strip()

@bot.message_handler(func=lambda message: message.text == "Вибрати")
def send_random_link(message):
    random_link = get_random_link()  
    bot.send_message(message.chat.id, random_link)

bot.polling()
