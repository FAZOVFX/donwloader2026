async def check_sub(bot, user_id, channel):

    member = await bot.get_chat_member(
        channel,
        user_id
    )

    return member.status in [
        "member",
        "administrator",
        "creator"
    ]
