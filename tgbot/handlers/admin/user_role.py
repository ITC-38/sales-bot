from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from sqlalchemy.testing import in_

from tgbot.keyboards.reply import (
    CANCEL_KEYBOARD, START_ADMIN_COMMANDS, ROLE_OPTION_BTNS
)
from tgbot.misc.commands import ButtonsData, Commands
from tgbot.misc.states import CreateRoleState, DeleteRoleState
from tgbot.models.models import UserRole


async def add_role_command(message: Message):
    await CreateRoleState.name.set()
    await message.answer(
        'Напишите название роли',
        reply_markup=CANCEL_KEYBOARD
    )


async def create_role(message: Message, state: FSMContext):
    if message.text == ButtonsData.cancel.value:
        await state.finish()
        await message.answer(
            'Команда отменена',
            reply_markup=START_ADMIN_COMMANDS
        )
        return
    role_name = message.text
    role_obj = await UserRole.query.where(
        UserRole.name == role_name
    ).gino.first()
    if role_obj:
        await message.answer(
            'Роль уже существует! Введите другое название',
            reply_markup=CANCEL_KEYBOARD
        )
        return
    await UserRole.create(name=role_name)
    await state.finish()
    await message.answer(
        'Успешно создал роль',
        reply_markup=START_ADMIN_COMMANDS
    )


async def get_user_roles(message: Message):
    roles: list[UserRole] = await UserRole.query.gino.all()
    answer = 'Список ролей:\n\n' + '\n\n'.join(map(
        lambda model: model.tg_beautify(),
        roles
    ))
    await message.answer(answer, reply_markup=ROLE_OPTION_BTNS)


async def delete_user_role_command(message: Message):
    await DeleteRoleState.role_id.set()
    await message.answer('Введите 🆔 ролей через запятую')


async def delete_role(message: Message, state: FSMContext):
    split_ids = message.text.split(',')
    check_ids = all(map(
        lambda model: model.isdecimal(),
        split_ids
    ))
    if not check_ids:
        await message.answer('Введите правильное число')
        return
    resolved_ids = list(map(int, split_ids))
    await UserRole.delete.where(
        UserRole.id.in_(resolved_ids)
    ).gino.status()
    await state.finish()
    await message.answer('Успешно удалил...', reply_markup=START_ADMIN_COMMANDS)


def register_user_role_handlers(dp: Dispatcher):
    dp.register_message_handler(
        add_role_command, text=Commands.create_role.value
    )
    dp.register_message_handler(
        create_role, state=CreateRoleState.name
    )
    dp.register_message_handler(
        get_user_roles, text=Commands.roles_list.value
    )
    dp.register_message_handler(
        delete_user_role_command, text=Commands.delete_role.value
    )
    dp.register_message_handler(
        delete_role, state=DeleteRoleState.role_id
    )
