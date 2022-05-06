import io

from aiogram import types
from aiogram.dispatcher.filters import Command, AdminFilter

from filters import IsGroup
from loader import dp, bot


@dp.message_handler(IsGroup(), Command("set_photo", prefixes="!/"), AdminFilter())
async def set_new_photo(m: types.Message):
    sourse_message = m.reply_to_message
    photo = sourse_message.photo[-1]
    photo = await photo.download(destination=io.BytesIO())
    input_file = types.InputFile(path_or_bytesio=photo)
    # await bot.set_chat_photo(chat_id=m.chat.id, photo=input_file)
    await m.chat.set_photo(photo=input_file)


@dp.message_handler(IsGroup(), Command("set_title", prefixes="!/"), AdminFilter())
async def set_new_title(m: types.Message):
    sourse_message = m.reply_to_message
    title = sourse_message.text
    await m.chat.set_title(title)

@dp.message_handler(IsGroup(), Command("set_description", prefixes="!/"), AdminFilter())
async def set_new_description(m: types.Message):
    sourse_message = m.reply_to_message
    description = sourse_message.text
    await m.chat.set_description(description)






