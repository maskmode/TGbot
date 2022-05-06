from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

post_callback = CallbackData("create_post", "action")

confirm_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Уверен",
                                 callback_data=post_callback.new(action="post")),
            InlineKeyboardButton(text="Не уверен",
                                 callback_data=post_callback.new(action="cancel"))
        ]

    ]
)
