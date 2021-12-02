from aiogram import types
import logging
from aiogram.dispatcher.filters.builtin import Command, CommandStart
from aiogram.types import CallbackQuery
from loader import dp, db, bot
from data.config import ADMINS
from keyboards.inline.choise_buttons import choise
from keyboards.inline.choise_buttons_admin import choise_admin
from keyboards.inline.callback_data import buy_callback
from asyncpg import Connection, Record
from asyncpg.exceptions import UniqueViolationError

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from utils.notify_admins import alert_for_admin
from utils.func import create_array_for_print

from keyboards.default.client_kb  import kb_client

class FSMAdder(StatesGroup):
    photo = State()
    description = State()


class DBCommands: 
    pool: Connection=db
    ADD_NEW_APPLICATION = "INSERT INTO applications (chat_id,username,full_name,application_image,application_description,application_status) Values ($1,$2,$3,$4,$5,0) RETURNING id"
    GET_MY_APPLICATION = "SELECT (chat_id,application_image,application_description,application_status) FROM applications WHERE chat_id = $1"

    async def add_new_application(self,state):
        args = []
        async with state.proxy() as data: 
            chat_id = int(data['chat_id'])
            username = data['username']
            full_name = data ['full_name']
            application_image = data['photo']
            application_description = data['description']
        command = self.ADD_NEW_APPLICATION
        args = [chat_id,username,full_name,application_image,application_description]
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
            record = await self.pool.fetch(command,args)
            logging.info(f"record from bd= {record}")
            return record
        except UniqueViolationError:
            pass

database = DBCommands()


@dp.message_handler(commands='menu')
async def bot_start(message: types.Message):
    user_name  =  message.from_user.full_name
    #await message.answer(f"Привет, {message.from_user.full_name}!")
    user_id  = message.from_user.id
    is_admin = False
    for admin in ADMINS: 
        if admin == str(user_id):
            is_admin = True
    if is_admin:
        await message.answer(text="Вот, что ты можешь сделать",
                            reply_markup=choise_admin)
    else:
        #await message.answer(text=f"Привет, {message.from_user.full_name}! Вот, что ты можешь сделать",
                            #reply_markup=choise)
        await message.answer(text="Вот, что ты можешь сделать",
                            reply_markup=choise)

@dp.callback_query_handler(text = 'add')
async def cm_start(message: types.Message):
    await FSMAdder.photo.set()
    #await message.reply("Загрузите фото")
    await bot.send_message(message.from_user.id,'Загрузите фото')



@dp.message_handler(state="*",commands='отмена')
@dp.message_handler(Text(equals='отмена',ignore_case=True),state='*')
async def cancel_add_hanbler(message: types.Message,state=FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('ОК')

@dp.message_handler(content_types=['photo'],state=FSMAdder.photo)
async def load_photo(message:types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMAdder.next()
    await message.reply("Теперь введите место")

@dp.message_handler(state=FSMAdder.description)
async def load_desc(message = types.Message, state = FSMAdder.description):
    async with state.proxy() as data:
        data['description'] = message.text
        data['username'] = message.from_user.first_name
        data['chat_id'] = message.from_user.id
        data['full_name'] = message.from_user.first_name + message.from_user.last_name
        logging.info(f'Data: {data}')
        logging.info(f'Message {message.from_user}')
    answerBD = await database.add_new_application(state)
    await state.finish()
    if answerBD:
        #Оповещение админу 
        await alert_for_admin(dp)
        await message.reply("Ваша заявка добалена.")
    else:
        await message.reply("Ошибка! Попробуйте еще раз :)")
    



@dp.callback_query_handler(buy_callback.filter(item_name = 'myApplication'))
async def myApplication(call: CallbackQuery,callback_data: dict):
    await call.answer(cache_time=60)
    callbackData = call.data
    user_id = call.from_user.id
    logging.info(f"user_id= {user_id}")
    
    record = await database.get_my_application(user_id)
    delete_str = '<Record row=('
    logging.info(f"record from bot= {record}")
    answer = "Ваши заявки: \n"
    for i in record:
        string = str(i) 
        string = string.replace(delete_str,'')
        string = string.replace(')>','')
        logging.info(string)
        array_message = create_array_for_print(string)
        answer += string + "\n"
        await bot.send_photo(user_id, str(array_message[1]), f'Описание:\n{array_message[2]}\n Статус:\n{array_message[3]}')

@dp.callback_query_handler(text= 'cancel')
async def cancel(call:CallbackQuery):
    await call.answer("Что открыть меню введите /menu", show_alert=False)
    await call.message.delete()
    await call.message.edit_reply_markup(reply_markup=None)
