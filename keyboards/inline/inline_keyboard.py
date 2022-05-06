from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.callback_data import buy_callback

inline_key = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(
                                              text="Груша",
                                              callback_data=buy_callback.new(item_name="pear",
                                                                             quantity=1)
                                          ),
                                          InlineKeyboardButton(
                                              text="Яблоко",
                                              callback_data="buy:apple:5"
                                          ),
                                          InlineKeyboardButton(
                                              text="Отмена",
                                              callback_data="cancel"
                                          )
                                      ]
                                  ]
                                  )

pear_keyboard = InlineKeyboardMarkup()

PEAR_LINK = "https://www.youtube.com/"

pear_link = InlineKeyboardButton(text="Купи тут", url=PEAR_LINK)
pear_keyboard.insert(pear_link)
