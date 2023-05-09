from dataclasses import dataclass
from pathlib import Path

from environs import Env


BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_DIR = BASE_DIR / 'media/'
PHOTOS_SAVE_DIR = MEDIA_DIR / 'photos'


@dataclass
class DbConfig:
    host: str
    password: str
    user: str
    database: str

    def get_db_url(self):
        return f'postgresql://{self.user}:{self.password}@' \
               f'{self.host}:5432/{self.database}'


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]
    use_redis: bool


@dataclass
class Config:
    tg_bot: TgBot
    db: DbConfig


def load_config(path: str = None) -> Config:
    env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env.str("BOT_TOKEN"),
            admin_ids=list(map(int, env.str("ADMINS").split(","))),
            use_redis=env.bool("USE_REDIS"),
        ),
        db=DbConfig(
            host=env.str('DB_HOST'),
            password=env.str('DB_PASS'),
            user=env.str('DB_USER'),
            database=env.str('DB_NAME')
        )
    )


def load_db_config(path: str = None) -> DbConfig:
    env = Env()
    env.read_env(path)
    return DbConfig(
            host=env.str('DB_HOST'),
            password=env.str('DB_PASS'),
            user=env.str('DB_USER'),
            database=env.str('DB_NAME')
        )
