import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import BOT_TOKEN


bot = Bot(token = BOT_TOKEN, parse_mode = types.ParseMode.HTML)
dp = Dispatcher(bot, storage = MemoryStorage())


logging.basicConfig(level=logging.INFO)
