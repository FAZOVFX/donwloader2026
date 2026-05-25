async def add_user(
    db,
    user_id
):

    await db.execute(

        '''
        INSERT INTO users(user_id)
        VALUES($1)
        ''',

        user_id
    )
