from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


b1 = KeyboardButton("Добавить новую заявку")
b2 = KeyboardButton("Посмотреть мои заявки")

kb_client = ReplyKeyboardMarkup()
kb_client.add(b1).add(b2)