import logging
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command
from aiogram.types.message import Message
from aiogram.types import CallbackQuery
from loader import dp
from keyboards.inline.callback_data import buy_callback


@dp.callback_query_handler(text_contains="addApplication")
async def addApplication(call: CallbackQuery,callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"call= {callback_data}")

    await call.message.answer("Запись изменена")

@dp.callback_query_handler(buy_callback.filte(item_name = 'myApplication'))
async def addApplication(call: CallbackQuery):
    await call.answer(cache_time=60)
    callbackData = call.data
    logging.info(f"call= {callbackData}")

    await call.message.answer("Запись отправлена")