from loader import bot, dp
from config import admins_id
import handlers


async def send_to_admin(*args):
    for id in admins_id:
        try:
            await bot.send_message(chat_id = id, text = "Bot starts!")
        except:
            pass

if __name__ == "__main__":
    from aiogram.utils.executor import start_polling
    start_polling(dp, on_startup = send_to_admin, skip_updates = True)