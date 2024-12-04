from keyboards import main_keyboard1
from utils import get_random_link_in_range


def register_handlers(bot):
    @bot.message_handler(func=lambda message: message.text == "Вибрати книгу по жанру жанр")
    def choose_genre(message):
        keyboard = main_keyboard1()
        bot.send_message(message.chat.id, "Оберіть жанр:", reply_markup=keyboard)

    @bot.message_handler(func=lambda message: message.text.lower() == "романтика")
    def send_romance_link(message):
        random_link = get_random_link_in_range(0, 5)
        bot.send_message(message.chat.id, f"Ось книга в жанрі 'романтика': {random_link}")

    @bot.message_handler(func=lambda message: message.text.lower() == "українська проза")
    def send_ukrainian_prose_link(message):
        random_link = get_random_link_in_range(7, 9)
        bot.send_message(message.chat.id, f"Ось книга в жанрі 'Українська проза': {random_link}")

    @bot.message_handler(func=lambda message: message.text.lower() == "філософія")
    def send_philosophy_link(message):
        random_link = get_random_link_in_range(11, 15)
        bot.send_message(message.chat.id, f"Ось книга в жанрі 'філософія': {random_link}")

    @bot.message_handler(func=lambda message: message.text.lower() == "фантастика")
    def send_fantasy_link(message):
        random_link = get_random_link_in_range(17, 20)
        bot.send_message(message.chat.id, f"Ось книга в жанрі 'фантастика': {random_link}")