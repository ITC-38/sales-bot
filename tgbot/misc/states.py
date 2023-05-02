from aiogram.dispatcher.filters.state import StatesGroup, State


class SignUpState(StatesGroup):
    phone_num = State()
    age = State()
