from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class IsGroup(BoundFilter):
    async def check(self, m: types.Message) -> bool:
        return m.chat.type in (
            types.ChatType.GROUP,
            types.ChatType.SUPERGROUP
        )