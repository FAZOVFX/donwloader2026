from aiogram.filters import BaseFilter
from app.config import ADMINS

class AdminFilter(BaseFilter):

    async def __call__(self, message):

        return (
            message.from_user.id
            in ADMINS
        )
