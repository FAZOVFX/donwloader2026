from aiogram import Router
from aiogram.types import (
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from app.services.downloader import (
    download_video,
    download_mp3
)

from app.handlers.search import (
    user_data
)

router = Router()


@router.callback_query()
async def callbacks(call: CallbackQuery):

    data = call.data

    # Search result selected
    if data.startswith("music_"):

        idx = data.split("_")[1]

        url = user_data[
            f"{call.message.chat.id}_{idx}"
        ]

        user_data[
            call.message.chat.id
        ] = url

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

        await call.message.answer(
            "Format tanlang",
            reply_markup=keyboard
        )

    # Video download
    elif data == "video":

        url = user_data[
            call.message.chat.id
        ]

        msg = await call.message.answer(
            "Video yuklanmoqda..."
        )

        path = download_video(url)

        await call.message.answer_video(
            video=path
        )

        await msg.delete()

    # MP3 download
    elif data == "mp3":

        url = user_data[
            call.message.chat.id
        ]

        msg = await call.message.answer(
            "MP3 yuklanmoqda..."
        )

        path = download_mp3(url)

        await call.message.answer_audio(
            audio=path
        )

        await msg.delete()
