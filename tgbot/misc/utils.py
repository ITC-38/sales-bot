from aiogram import Bot
from aiogram.types import InputFile

from tgbot.models.models import User


async def mailing_users(
        bot: Bot, msg_body: str,
        photo_path: str) -> None:
    users: list[User] = await User.query.gino.all()
    for user in users:
        await bot.send_photo(
            user.tg_id,
            InputFile(photo_path),
            caption=msg_body
        )
