from aiogram.types import KeyboardButton

from tgbot.misc.commands import ButtonsData, Commands

SEND_PHONE_NUMBER_BTN = KeyboardButton(
    ButtonsData.send_phone_number.value,
    request_contact=True
)
CREATE_ROLE_BTN = KeyboardButton(
    Commands.create_role.value
)
CANCEL = KeyboardButton(
    ButtonsData.cancel.value
)
ROLES_LIST_BTN = KeyboardButton(
    Commands.roles_list.value
)
DELETE_ROLE_BTN = KeyboardButton(
    Commands.delete_role.value
)
CREATE_NEWS_BTN = KeyboardButton(
    Commands.create_news.value
)
