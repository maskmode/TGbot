from aiogram import types

from filters import IsGroup
from loader import dp, bot


@dp.message_handler(IsGroup(), content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def new_member(m: types.Message):
    members = ", ".join([m.get_mention(as_html=True) for m in m.new_chat_members])
    await m.reply(f"Hello, {members}, стоимость нахождения в группе 50 рублей в день.\n"
                  "Деньги будут списаны с симкарты")  # {m.new_chat_members[0].full_name}


@dp.message_handler(IsGroup(), content_types=types.ContentType.LEFT_CHAT_MEMBER)
async def new_member(m: types.Message):
    if m.left_chat_member.id == m.from_user.id:
        await m.reply(f"{m.left_chat_member.get_mention(as_html=True)} покинул чат")
    elif m.left_chat_member.id == (await bot.me).id:
        return
    else:
        await m.reply(f"{m.left_chat_member.full_name}\n"
                      f"Был удален пользователем {m.from_user.full_name}")




