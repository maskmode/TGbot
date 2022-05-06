import asyncio
import re
import datetime as dt

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.utils.exceptions import BadRequest

from filters import IsGroup, AdminFilter
from loader import dp, bot


@dp.message_handler(IsGroup(), Command("ro", prefixes="!/"), AdminFilter())
async def read_only(m: types.Message):
    member = m.reply_to_message.from_user
    member_id = member.id
    chat_id = m.chat.id
    command_parse = re.compile(r'(/ro) ?(\d+)? ?([\w+\D]+)?')
    parsed = command_parse.match(m.text)
    ban_time = parsed.group(2)
    comment = parsed.group(3)
    if not ban_time:
        ban_time = 5
    else:
        ban_time = int(ban_time)

    untill_date = dt.datetime.now() + dt.timedelta(minutes=ban_time)

    read_only_permissions = types.ChatPermissions(
        can_send_messages=False,
        can_send_polls=False,
        can_change_info=False,
        can_invite_users=True,
        can_pin_messages=False,
        can_send_media_messages=False,
        can_send_other_messages=False,
        can_add_web_page_previews=False
    )
    try:
        await bot.restrict_chat_member(chat_id, user_id=member_id, permissions=read_only_permissions,
                                       until_date=untill_date)
        await m.reply(
            f"Режим только чтение для {member.get_mention(as_html=True)} на {ban_time} минут. Причина - {comment}")
    except BadRequest:
        await m.answer("Пользователь является администратором")
    except Exception as err:
        await m.answer(f"{err.__class__.__name__}: {err}")

    service_message = await m.reply("Сообщение самоудалится через 5 секунд")
    await asyncio.sleep(5)
    await m.delete()
    await service_message.delete()


@dp.message_handler(IsGroup(), Command("unro", prefixes="!/"), AdminFilter())
async def read_only_off(m: types.Message):
    member = m.reply_to_message.from_user
    member_id = member.id
    chat_id = m.chat.id

    read_only_off = types.ChatPermissions(
        can_send_messages=True,
        can_send_polls=True,
        can_change_info=False,
        can_invite_users=True,
        can_pin_messages=False,
        can_send_media_messages=True,
        can_send_other_messages=True,
        can_add_web_page_previews=True
    )

    await m.chat.restrict(user_id=member_id,permissions=read_only_off, until_date=0)
    await m.reply(f"Пользователь {member.full_name} разбанен")

@dp.message_handler(IsGroup(), Command("ban", prefixes="!/"), AdminFilter())
async def ban(m: types.Message):
    member = m.reply_to_message.from_user
    member_id = member.id
    chat_id = m.chat.id
    await m.chat.kick(member_id)
    await m.reply(f"Пользователь {member.full_name} забанен")

@dp.message_handler(IsGroup(), Command("unban", prefixes="!/"), AdminFilter())
async def unban(m: types.Message):
    member = m.reply_to_message.from_user
    member_id = member.id
    chat_id = m.chat.id
    await m.chat.unban(member_id)
    await m.reply(f"Пользователь {member.full_name} разбанен")