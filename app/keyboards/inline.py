from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

def format_keyboard():

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="1080P VIDEO",
                    callback_data="video"
                ),

                InlineKeyboardButton(
                    text="MP3",
                    callback_data="mp3"
                )
            ]
        ]
    )
