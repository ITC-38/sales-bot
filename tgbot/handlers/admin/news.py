import datetime

from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ContentType

from tgbot.config import PHOTOS_SAVE_DIR
from tgbot.misc.commands import Commands
from tgbot.misc.path_helper import (
    get_file_format, get_photo_save_path_url
)
from tgbot.misc.states import CreateNewsState
from tgbot.misc.utils import mailing_users
from tgbot.models.models import News


async def add_news_command(message: Message):
    await CreateNewsState.name.set()
    await message.answer(
        'Введите название новости'
    )


async def add_new_title(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Введите описание поста')
    await CreateNewsState.title.set()


async def send_post_preview(message: Message, state: FSMContext):
    await state.update_data(title=message.text)
    await message.answer('Отправьте превью поста')
    await CreateNewsState.preview.set()


async def upload_post_preview_and_save(message: Message, state: FSMContext):
    photo_id = message.photo[-1].file_id
    file_obj = await message.bot.get_file(photo_id)
    file_format = get_file_format(file_obj.file_path)
    now = datetime.datetime.now()
    file_path = get_photo_save_path_url(
        PHOTOS_SAVE_DIR,
        'news/' + now.date().__str__(),
        now.strftime('%d-%b-%Y-%H-%M') + '.' + file_format,
    )
    await message.bot.download_file_by_id(
        photo_id,
        destination=file_path
    )
    async with state.proxy() as data:
        post_name = data['name']
        post_title = data['title']
    await News.create(
        name=post_name, title=post_title,
        created_date=now, photo_path=file_path
    )
    await message.answer('Успешно создал новость')
    await mailing_users(
        message.bot,
        f'<b>{post_name}</b>\n{post_title}\n',
        file_path
    )
    await state.finish()


def register_news_handlers(dp: Dispatcher):
    dp.register_message_handler(
        add_news_command,
        text=Commands.create_news.value
    )
    dp.register_message_handler(
        add_new_title,
        state=CreateNewsState.name
    )
    dp.register_message_handler(
        send_post_preview,
        state=CreateNewsState.title
    )
    dp.register_message_handler(
        upload_post_preview_and_save,
        state=CreateNewsState.preview,
        content_types=ContentType.PHOTO
    )
