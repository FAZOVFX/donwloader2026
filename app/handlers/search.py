from aiogram import Router
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from app.services.youtube_search import (
    search_youtube
)

router = Router()

user_data = {}


@router.message()
async def search_music(message: Message):

    text = message.text

    # YouTube link
    if (
        "youtube.com" in text
        or
        "youtu.be" in text
    ):

        user_data[
            message.chat.id
        ] = text

        keyboard = InlineKeyboardMarkup(
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

        await message.answer(
            "Format tanlang",
            reply_markup=keyboard
        )

        return

    # Search
    results = search_youtube(text)

    buttons = []

    for i, item in enumerate(results):

        title = item["title"][:50]

        url = (
            f"https://youtube.com/watch?v="
            f"{item['id']}"
        )

        user_data[
            f"{message.chat.id}_{i}"
        ] = url

        buttons.append([
            InlineKeyboardButton(
                text=title,
                callback_data=f"music_{i}"
            )
        ])

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=buttons
    )

    await message.answer(
        "Topilgan variantlar:",
        reply_markup=keyboard
    )
