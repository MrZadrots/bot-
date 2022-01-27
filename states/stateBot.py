from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMAdder(StatesGroup):
    photo = State()
    place = State()
    flor = State()
    description = State()

