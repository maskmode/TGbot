from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class IsForwarded(BoundFilter):
    async def check(self, m: types.Message) -> bool:
        try:
            if m.forward_from_chat.type:
                return m.forward_from_chat.type == types.ChatType.CHANNEL
        except:
            return False
