#
#
#
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
#
#
b1 = KeyboardButton('/Amenajari_interior')
b2 = KeyboardButton('/Amenajari_exterior')
b3 = KeyboardButton('/Meniu')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.row(b1, b2, b3)