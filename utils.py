import random
from dotenv import load_dotenv
import os

def get_token():
    load_dotenv()
    token=os.getenv("TOKEN")
    return token


def get_random_link_in_range(start, end):
    try:
        with open('links.txt', 'r', encoding='utf-8') as file:
            links = file.readlines()  # Зчитуємо всі рядки у список

        if 0 <= start < len(links) and start < end <= len(links):
            index_range = range(start, end)  # Створюємо діапазон індексів
            random_index = random.choice(index_range)  # Вибираємо випадковий індекс з діапазону
            return links[random_index].strip()  # Повертаємо випадкове посилання без зайвих пробілів
        else:
            return "Неправильний діапазон або відсутні посилання в заданому діапазоні."
    except FileNotFoundError:
        return "Файл з посиланнями не знайдено."