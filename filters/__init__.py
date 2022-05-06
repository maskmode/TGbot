from aiogram import Dispatcher
from .group_chat import IsGroup
from .admins import AdminFilter


def setup(dp: Dispatcher):
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(IsGroup)