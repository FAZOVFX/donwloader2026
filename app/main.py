import asyncio
import threading
import os

from flask import Flask

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

# Routerlar
dp.include_router(start_router)
dp.include_router(youtube_router)
dp.include_router(insta_router)
dp.include_router(search_router)
dp.include_router(admin_router)
dp.include_router(callback_router)

# Flask app
web = Flask(__name__)

@web.route("/")
def home():
    return "Bot is running"


# Web server
def run_web():

    port = int(
        os.environ.get(
            "PORT",
            10000
        )
    )

    web.run(
        host="0.0.0.0",
        port=port
    )


# Telegram bot
async def run_bot():

    await dp.start_polling(bot)


# Main
if __name__ == "__main__":

    # Flask thread
    threading.Thread(
        target=run_web
    ).start()

    # Bot polling
    asyncio.run(
        run_bot()
    )
