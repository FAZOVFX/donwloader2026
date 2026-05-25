from aiogram import Router
from aiogram.types import Message
from app.config import ADMINS

router = Router()

@router.message()
async def admin_panel(message: Message):

    if message.from_user.id in ADMINS:
        await message.answer(
            "Admin panel"
        )
