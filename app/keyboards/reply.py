from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton
)

admin_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="STATISTIKA"
            )
        ],

        [
            KeyboardButton(
                text="BROADCAST"
            )
        ]
    ],

    resize_keyboard=True
)
