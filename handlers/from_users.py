from config import admins_id
from loader import bot,dp
from aiogram.types import Message,ContentTypes


@dp.message_handler() #content_types = ContentTypes.TEXT
async def from_user_text(message:Message):
    for id in admins_id:
        await bot.send_message(chat_id=id, text=f"{message.from_user.first_name}:  {message.text}")


@dp.message_handler(content_types=ContentTypes.PHOTO)
async def from_user_photo(message:Message):
    for id in admins_id:
        await bot.send_message(chat_id=id, text=message.from_user.full_name)
        await bot.send_photo(chat_id=id, photo=message.photo[0].file_id)


@dp.message_handler(content_types=ContentTypes.STICKER)
async def from_user_sticker(message:Message):
    for id in admins_id:
        await bot.send_message(chat_id=id, text=message.from_user.full_name)
        await bot.send_sticker(chat_id=id, sticker=message.sticker.file_id)

@dp.message_handler(content_types=ContentTypes.VIDEO)
async def from_user_video(message:Message):
    for id in admins_id:
        await bot.send_message(chat_id=id, text=message.from_user.full_name)
        await bot.send_video(chat_id=id, video=message.video.file_id)


@dp.message_handler(content_types=ContentTypes.AUDIO)
async def from_user_audio(message:Message):
    for id in admins_id:
        await bot.send_message(chat_id=id, text=message.from_user.full_name)
        await bot.send_audio(chat_id=id, audio=message.audio.file_id)


@dp.message_handler(content_types=ContentTypes.VOICE)
async def from_user_voice(message:Message):
    for id in admins_id:
        await bot.send_message(chat_id=id, text=message.from_user.full_name)
        await bot.send_voice(chat_id=id, voice=message.voice.file_id)
