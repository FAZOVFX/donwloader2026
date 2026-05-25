from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message()
async def search_music(message: Message):

    await message.answer(
        "Qidirilmoqda..."
    )
