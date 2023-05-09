from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from tgbot.keyboards.reply import START_ADMIN_COMMANDS


async def admin_start(message: Message, state: FSMContext):
    await state.finish()
    await message.reply('Hello, admin!', reply_markup=START_ADMIN_COMMANDS)


def register_admin(dp: Dispatcher):
    dp.register_message_handler(
        admin_start, commands=['start'],
        state='*', is_superuser=True,
        commands_prefix='!/'
    )
