from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardRemove

from keyboards.default import menu
from loader import dp


@dp.message_handler(Command('menu'))
async def show_menu(message: types.Message):
    await message.answer("Нажми кнопку ниже", reply_markup=menu)


@dp.message_handler(text="Первая")
async def get_one(message: types.Message):
    await message.answer("Выбрана первая")


# dp.message_handler(Text(equals=["Первая", "Вторая"]))

@dp.message_handler(Text(endswith="ая"))
async def get_num(message: types.Message):
    await message.answer(f"Выбрано {message.text}", reply_markup=ReplyKeyboardRemove())
