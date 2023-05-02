from aiogram.types import ReplyKeyboardMarkup

from tgbot.buttons.reply import SEND_PHONE_NUMBER_BTN

START_OPTIONS = ReplyKeyboardMarkup([
    [SEND_PHONE_NUMBER_BTN]
], resize_keyboard=True)
