from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Первая")

        ],
        [
            KeyboardButton(text="Вторая"),
            KeyboardButton(text="Вторая2"),

        ],
    ],
    resize_keyboard=True
)
