from loader import bot, dp
from config import admins_id
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message


@dp.message_handler(Command('id', prefixes='.'))
async def yozdim(msg:Message,state:FSMContext):
    async with state.proxy() as data:
        data['user_id']=msg.text[4:]
        data['adm_id']=msg.from_user.id


@dp.message_handler(Command('sm', prefixes='.'))
async def novviyoz(msg:Message,state:FSMContext):
    async with state.proxy() as data:
        to_user_id=data['user_id']
        admin_id=data['adm_id']
    matn=msg.text[4:]
    
    msg_id = await bot.send_message(chat_id=to_user_id, text=matn)
    
    for id in admins_id:
        await bot.send_message(chat_id=id, text=(f"{admin_id} dan\n{to_user_id} ga\n{matn}\nXabarning IDsi: {msg_id.message_id}"))


@dp.message_handler(Command('del', prefixes='.'))
async def delete_msg(msg:Message, state:FSMContext):
    async with state.proxy() as data:
        to_user_id=data['user_id']
    msg_id=int(msg.text[5:])
    
    await bot.delete_message(chat_id=to_user_id, message_id=msg_id)
