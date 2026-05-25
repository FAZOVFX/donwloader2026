import asyncio

from app.loader import (
    bot,
    dp
)

from app.handlers.start import router as start_router
from app.handlers.youtube import router as youtube_router
from app.handlers.instagram import router as insta_router
from app.handlers.search import router as search_router
from app.handlers.admin import router as admin_router
from app.handlers.callback import router as callback_router

dp.include_router(start_router)
dp.include_router(youtube_router)
dp.include_router(insta_router)
dp.include_router(search_router)
dp.include_router(admin_router)
dp.include_router(callback_router)

async def main():

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
