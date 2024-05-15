from aiogram.fsm.state import StatesGroup, State

class KickPenalty(StatesGroup):
    shot = State()

class KeepPenalty(StatesGroup):
    kep = State()    


class KickFinal(StatesGroup):
    shot = State()

class KeepFinal(StatesGroup):
    kep = State()