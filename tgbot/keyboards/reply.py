from aiogram.types import ReplyKeyboardMarkup

from tgbot.buttons.reply import (
    SEND_PHONE_NUMBER_BTN,
    CREATE_ROLE_BTN, CANCEL,
    ROLES_LIST_BTN, DELETE_ROLE_BTN
)


START_OPTIONS = ReplyKeyboardMarkup([
    [SEND_PHONE_NUMBER_BTN]
], resize_keyboard=True)

START_ADMIN_COMMANDS = ReplyKeyboardMarkup([
    [ROLES_LIST_BTN]
], resize_keyboard=True)

CANCEL_KEYBOARD = ReplyKeyboardMarkup([
    [CANCEL]
], resize_keyboard=True)

ROLE_OPTION_BTNS = ReplyKeyboardMarkup([
    [CREATE_ROLE_BTN, DELETE_ROLE_BTN]
], resize_keyboard=True)
