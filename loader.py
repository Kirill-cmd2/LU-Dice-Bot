import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, types
from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storagee=MemoryStorage()
dp = Dispatcher(bot, storage=storagee)

logging.basicConfig(level=logging.INFO)
