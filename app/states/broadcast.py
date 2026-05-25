from aiogram.fsm.state import (
    StatesGroup,
    State
)

class BroadcastState(
    StatesGroup
):

    text = State()
