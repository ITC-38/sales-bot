from aiogram.types import KeyboardButton

from tgbot.misc.commands import ButtonsData

SEND_PHONE_NUMBER_BTN = KeyboardButton(
    ButtonsData.send_phone_number.value,
    request_contact=True
)
