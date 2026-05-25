import asyncpg

async def connect_db():

    return await asyncpg.connect(
        user="postgres",
        password="password",
        database="botdb",
        host="localhost"
    )
