from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import user

from loader import dp
from data.config import ADMINS
from keyboards.inline.choise_buttons import choise
from keyboards.inline.choise_buttons_admin import choise_admin


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user_name  =  message.from_user.full_name
    #await message.answer(f"Привет, {message.from_user.full_name}!")
    user_id  = message.from_user.id
    is_admin = False
    for admin in ADMINS: 
        if admin == str(user_id):
            is_admin = True
    if is_admin:
        await message.answer(text=f"Привет, {message.from_user.full_name}! Вот, что ты можешь сделать",
                            reply_markup=choise_admin)
    else:
        await message.answer(text=f"Привет, {message.from_user.full_name}! Вот, что ты можешь сделать",
                            reply_markup=choise)
