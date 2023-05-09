from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ContentType, ReplyKeyboardRemove

from tgbot.keyboards.reply import START_OPTIONS
from tgbot.misc.states import SignUpState
from tgbot.models.models import User


async def user_start(message: Message, state: FSMContext):
    await state.finish()
    user_obj = await User.query.where(
        User.tg_id == message.from_user.id
    ).gino.first()
    if not user_obj:
        await message.answer(
            f'Пользователь не опознан...\n'
            f'Отправьте номер телефона чтобы пройти регистрацию\n',
            reply_markup=START_OPTIONS
        )
        await SignUpState.phone_num.set()
        return
    await message.reply("Hello, user!")


async def get_phone_number(message: Message, state: FSMContext):
    await state.set_data({'phone_num': message.contact.phone_number})
    await SignUpState.age.set()
    await message.answer(
        'Напишите свой возраст...',
        reply_markup=ReplyKeyboardRemove()
    )


async def get_age(message: Message, state: FSMContext):
    if not message.text.isdecimal():
        await message.answer('Напишите правильный возраст...')
        return
    int_age = int(message.text)
    if int_age >= 150:
        await message.reply('0_o ты нормальный?? Введи реальный возраст')
        return
    async with state.proxy() as data:
        phone_num = int(data['phone_num'])
    await User.create(
        tg_id=message.from_user.id,
        phone_number=phone_num,
        age=int_age
    )
    await message.answer('Вы успешно зарегистрировались!')


def register_user(dp: Dispatcher):
    dp.register_message_handler(
        user_start, commands=["start"],
        state="*", commands_prefix='!/'
    )
    dp.register_message_handler(
        get_phone_number, state=SignUpState.phone_num,
        content_types=[ContentType.CONTACT]
    )
    dp.register_message_handler(
        get_age, state=SignUpState.age
    )
