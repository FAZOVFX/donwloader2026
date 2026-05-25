from aiogram import Router, F
from aiogram.types import Message
from app.keyboards.inline import format_keyboard

router = Router()

@router.message(
    F.text.contains("youtube.com")
)
async def youtube_handler(message: Message):

    await message.answer(
        "Format tanlang",
        reply_markup=format_keyboard()
    )
