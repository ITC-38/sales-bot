from enum import Enum


class Commands(Enum):
    create_role = 'Создать роль пользователей 🤝'
    roles_list = 'Роли пользователей📜'
    delete_role = 'Удалить роль 🗑️'
    create_news = 'Создать новость 📰'


class ButtonsData(Enum):
    send_phone_number = 'Отправить номер телефона 📞'
    cancel = 'Отменить 🚫󠁿'
