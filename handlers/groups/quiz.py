import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Command, Text

from filters import IsGroup
from loader import dp, bot
import random

logging.basicConfig(level=logging.INFO)


def get_n():
    global n
    n = random.randint(1, 100)
    return n


# Хэндлер на команду /start
@dp.message_handler(Command("GoQuiz"))
async def bot_echo(message: types.Message):
    await message.answer("Введите число от 1 до 100 и попробуй угадать:")


get_n()


@dp.message_handler(content_types=types.ContentType.ANY)
async def get_one(message: types.Message):
    # await message.answer("Выбрана первая")

    # await message.answer(f"echo {message.text}, {n * 2}")
    try:
        if n == int(message.text):
            await message.answer(f"Верный ответ {n}! Я загадал новое число, угадаешь? Введи число:")
            get_n()
        elif n > int(message.text):
            await message.answer(f"Больше {message.text}")
        elif n < int(message.text):
            await message.answer(f"Меньше {message.text}")
    except:
        await message.answer(f"Введи число, {message.text} не число")

#
# async def cmd_start(message: types.Message):
#     poll_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     poll_keyboard.add(types.KeyboardButton(text="Начать игру",
#                                            request_poll=types.KeyboardButtonPollType(type=types.PollType.QUIZ)))
#     poll_keyboard.add(types.KeyboardButton(text="Отмена"))
#     await message.answer("Нажмите на кнопку ниже и создайте викторину!", reply_markup=poll_keyboard)
#
#
# # Хэндлер на текстовое сообщение с текстом “Отмена”
# @dp.message_handler(lambda message: message.text == "Отмена")
# async def action_cancel(message: types.Message):
#     remove_keyboard = types.ReplyKeyboardRemove()
#     await message.answer("Действие отменено. Введите /GoQuiz, чтобы начать заново.", reply_markup=remove_keyboard)
