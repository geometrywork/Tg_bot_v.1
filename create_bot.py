from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from config import tg_bot_token

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)