from aiogram import Dispatcher

from .database import GetBDUser
from .throttling import ThrottlingMiddleware


def setup(dp: Dispatcher):
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(GetBDUser())
