import logging

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from keyboards.callback_data import buy_callback
from keyboards.inline.inline_keyboard import inline_key, pear_keyboard
from loader import dp


@dp.message_handler(Command("items"))
async def show_items(message: types.Message):
    await message.answer(text="На продажу у нас есть 2 товара: Яблоки и груша\n"
                         "Если ничего не надо, жми отмена",
                         reply_markup=inline_key)

@dp.callback_query_handler(buy_callback.filter(item_name="pear"))
async def buying_pear(call: CallbackQuery, callback_data: dict):
    #await bot.answer_callback_query(callback_query_id=call.id)
    await call.answer(cache_time=1)
    logging.info(f"callback_data = {call.data}")
    logging.info(f"callback_data_dict = {callback_data}")
    quantity = callback_data.get("quantity")
    await call.message.answer(f"Вы выбрали грушу. Груш всего {quantity}",
                              reply_markup=pear_keyboard)

@dp.callback_query_handler(text="cancel")
async def cancel(call: CallbackQuery):
    #await bot.answer_callback_query(callback_query_id=call.id)
    await call.answer("Вы отменили покупку", show_alert=True)
    await call.message.edit_reply_markup()











