from aiogram import Dispatcher

from .admin import register_admin
from .news import register_news_handlers
from .user_role import register_user_role_handlers


def register_admin_handlers(dp: Dispatcher):
    register_admin(dp)
    register_user_role_handlers(dp)
    register_news_handlers(dp)
