from aiogram import Router
from aiogram.types import CallbackQuery

router = Router()

@router.callback_query()
async def callbacks(call: CallbackQuery):

    await call.answer()
