from aiogram.dispatcher.filters.state import (
    StatesGroup, State
)


class SignUpState(StatesGroup):
    phone_num = State()
    age = State()


class CreateRoleState(StatesGroup):
    name = State()


class DeleteRoleState(StatesGroup):
    role_id = State()
