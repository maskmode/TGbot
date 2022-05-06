from aiogram import types
import logging

from loader import dp


@dp.channel_post_handler(content_types=types.ContentTypes.ANY)
async def new_post(m: types.Message):
    logging.info(f"Новое сообщение в канале {m.chat.title}.\n"
                 f"{m.text}")
