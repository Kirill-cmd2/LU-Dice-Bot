from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

playi=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Qani, boshla o'yinni! 💪")
        ],
    ],
    resize_keyboard=True
)

yana_play=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Yana o'yin! 🤪")
        ],
        [
            KeyboardButton("To'xtat! Yetar endi?! 😐")
        ],
    ],
    resize_keyboard=True
)
