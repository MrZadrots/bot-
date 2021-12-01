from aiogram import types
from aiogram.dispatcher.filters.builtin import Command, CommandStart
from aiogram.types import message, user
from aiogram.types import CallbackQuery
import asyncpg
from loader import dp, db
from data.config import ADMINS
from keyboards.inline.choise_buttons import choise
from keyboards.inline.choise_buttons_admin import choise_admin
import logging
from keyboards.inline.callback_data import buy_callback
from asyncpg import Connection, Record
from asyncpg.exceptions import UniqueViolationError


class DBCommands: 
    pool: Connection=db
    ADD_NEW_APPLICATION = "INSERT INTO applications (chat_id,username,full_name,application_image,application_description,application_status) Values ($1,$2,$3,$4,$5,0) RETURNING id"
    GET_MY_APPLICATION = "SELECT (chat_id,application_image,application_description,application_status) FROM applications WHERE chat_id = $1"

    async def add_new_application(self,data):
        user = types.User.get_current()
        chat_id  = user.id
        username = user.first_name
        full_name = user.full_name
        args = chat_id,username,full_name,data[0],data[1]

        command = self.ADD_NEW_APPLICATION
        logging.info(f"args: {args}")
        try:
            record_id = await self.pool.fetchval(command,*args)
            return record_id
        except UniqueViolationError:
            pass
    
    async def get_my_application(self,user_id):
        args = (user_id)
        command = self.GET_MY_APPLICATION
        try:
            record = await self.pool.fetchval(command,args)
            logging.info(f"record from bd= {record}")
            return record
        except UniqueViolationError:
            pass

database = DBCommands()


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

@dp.callback_query_handler(buy_callback.filter(item_name = 'addApplication'))
async def addApplication(call: CallbackQuery,callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"call= {callback_data}")
    data = ['asdasdas','adasdasd']
    user_id = call.from_user.id
    username = call.from_user.first_name
    full_name = username + call.from_user.last_name
    id = await database.add_new_application(data)
    logging.info(f"id= {id}")
    await call.message.answer("Запись добавлена")

@dp.callback_query_handler(buy_callback.filter(item_name = 'myApplication'))
async def addApplication(call: CallbackQuery,callback_data: dict):
    await call.answer(cache_time=60)
    callbackData = call.data
    user_id = call.from_user.id
    logging.info(f"user_id= {user_id}")
    
    record = await database.get_my_application(user_id)
    logging.info(f"record from bot= {record}")
    await call.message.answer("Ваши заявки")
    await call.message.answer(record)

    
@dp.callback_query_handler(text= 'cancel')
async def cancel(call:CallbackQuery):
    await call.answer("Что открыть меню введите /start", show_alert=False)
    await call.message.edit_reply_markup(reply_markup=None)
