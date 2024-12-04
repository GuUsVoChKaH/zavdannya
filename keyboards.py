from telebot import types


def main_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    button1 = types.KeyboardButton(text="Вибрати книгу по жанру жанр")
    keyboard.add(button1)
    return keyboard


def main_keyboard1():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button_romance = types.KeyboardButton(text="романтика")
    button_ukrainian_prose = types.KeyboardButton(text="Українська проза")
    button_philosophy = types.KeyboardButton(text="філософія")
    button_fantasy = types.KeyboardButton(text="фантастика")
    keyboard.add(button_romance, button_ukrainian_prose, button_philosophy, button_fantasy)
    return keyboard