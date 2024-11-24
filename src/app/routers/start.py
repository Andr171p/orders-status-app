from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from src.config import config
from src.utils import load_json


start_router = Router()


@start_router.message(Command("start"))
async def start(message: Message) -> None:
    # user_id: int = message.from_user.id
    username: str = message.from_user.username
    text = await load_json(path=config.messages.greeting)
    await message.answer(
        text=text['start'].format(username=username)
    )
