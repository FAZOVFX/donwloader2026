from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(
    F.text.contains("instagram.com")
)
async def insta_handler(message: Message):

    await message.answer(
        "Instagram video yuklanmoqda..."
    )
