import asyncio
import threading
import os

from flask import Flask

from app.loader import (
    bot,
    dp
)

# START
from app.handlers.start import (
    router as start_router
)

# INSTAGRAM
from app.handlers.instagram import (
    router as insta_router
)

# SEARCH + YOUTUBE
from app.handlers.search import (
    router as search_router
)

# CALLBACKS
from app.handlers.callback import (
    router as callback_router
)

# ROUTERS
dp.include_router(start_router)

dp.include_router(insta_router)

dp.include_router(search_router)

dp.include_router(callback_router)

# FLASK
web = Flask(__name__)

@web.route("/")
def home():

    return "Bot is running"


# WEB SERVER
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


# TELEGRAM BOT
async def run_bot():

    await dp.start_polling(bot)


# MAIN
if __name__ == "__main__":

    # FLASK THREAD
    threading.Thread(
        target=run_web
    ).start()

    # BOT START
    asyncio.run(
        run_bot()
    )
