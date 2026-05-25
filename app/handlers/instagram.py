from aiogram import Router, F
from aiogram.types import Message

from app.services.downloader import (
    download_video
)

router = Router()


@router.message(
    F.text.contains("instagram.com")
)
async def instagram_download(
    message: Message
):

    msg = await message.answer(
        "Instagram video yuklanmoqda..."
    )

    try:

        path = download_video(
            message.text
        )

        await message.answer_video(
            video=path
        )

        await msg.delete()

    except Exception as e:

        await message.answer(
            f"Xato: {e}"
        )
