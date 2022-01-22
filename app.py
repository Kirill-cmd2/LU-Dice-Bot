from loader import bot
from config import admins_id

async def send_to_admin(*args):
    await bot.send_message(chat_id=admins_id[0], text="Bot starts!")
    
async def on_shd(dp):
    await bot.send_message(chat_id=admins_id[0], text="Bot closes!")
    await bot.close()

if __name__ == "__main__":
    from aiogram import executor
    from handlers import dp
    executor.start_polling(dp, on_startup=send_to_admin, on_shutdown=on_shd, skip_updates=True)