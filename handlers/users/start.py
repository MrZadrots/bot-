from aiogram import types
import logging
from aiogram.dispatcher.filters.builtin import Command, CommandStart
from aiogram.types import message, reply_keyboard, user
from aiogram.types import CallbackQuery
from loader import dp, db, bot
from data.config import ADMINS
from keyboards.inline.choise_buttons import choise
from keyboards.inline.choise_buttons_admin import choise_admin
from keyboards.inline.callback_data import buy_callback
from keyboards.inline.callback_data_campus import campus_callback
from utils.func import find_flor
from asyncpg import Connection, Record
from asyncpg.exceptions import UniqueViolationError
#from utils.db_api.DBCommands import DBCommands
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from utils.notify_admins import alert_for_admin
from utils.func import create_array_for_print
from keyboards.inline.campus_keyboard import campus_keyboard
from keyboards.default.client_kb  import kb_client
from states.stateBot import FSMAdder

from keyboards.inline.flor_keyboard import first_flor,second_flor,third_flor


class DBCommands: 
    pool: Connection=db
    ADD_NEW_APPLICATION = "INSERT INTO applications (chat_id,username,application_image,application_description,application_status) Values ($1,$2,$3,$4,0) RETURNING id"
    GET_MY_APPLICATION = "SELECT (chat_id,application_image,application_description,application_status) FROM applications WHERE chat_id = $1"

    async def add_new_application(self,state):
        args = []
        async with state.proxy() as data: 
            chat_id = int(data['chat_id'])
            username = data['username']
            application_image = data['photo']
            application_description = data['description']
        command = self.ADD_NEW_APPLICATION
        args = [chat_id,username,application_image,application_description]
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

@dp.message_handler(CommandStart())
async def bot_menu(message: types.Message):
    await message.answer(text=f"Привет, {message.from_user.full_name}! Что начать пользоваться ботом введи /menu или нажми кнопку",
                            reply_markup=kb_client)



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
        #await message.answer(text="Вот, что ты можешь сделать",
                            #reply_markup=choise_admin)
        await message.answer(text="Я скажу, когда добавять заявку")
    else:
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
    await bot.send_message(message.from_user.id,'Вот, что ты можешь сделать', reply_markup=choise)

@dp.message_handler(content_types=['photo'],state=FSMAdder.photo)
async def load_photo(message:types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    file_info = await bot.get_file(message.photo[-1].file_id)
    await message.photo[-1].download(file_info.file_path)
    await FSMAdder.next()
    await message.answer(text="Теперь выберите место",reply_markup=campus_keyboard)

@dp.callback_query_handler(campus_callback.filter(item_name = 'campus'),state = FSMAdder.place)
async def load_place(call: CallbackQuery, callback_data: dict,state = FSMAdder.place):
    print("CallBack", call)
    async with state.proxy() as data:
        data['place']= callback_data['item_value']
    await FSMAdder.next()

    campus = callback_data['item_value']

    if campus == '1 корпус':
        print(campus)
        await bot.send_message(call.from_user.id,'Выбери этаж', reply_markup=first_flor)
    if campus == '2 корпус':
        print(campus)
        await bot.send_message(call.from_user.id,'Выбери этаж', reply_markup=second_flor)        
    if campus == '3 корпус':
        print(campus)
        await bot.send_message(call.from_user.id,'Выбери этаж', reply_markup=third_flor)  

@dp.callback_query_handler(campus_callback.filter(item_name = 'flor'),state = FSMAdder.flor)
async def load_flor(call: CallbackQuery, callback_data: dict,state = FSMAdder.flor):
    async with state.proxy() as data:
        data['flor']= callback_data['item_value']
    await FSMAdder.next()
    await bot.send_message(call.from_user.id,'Добавь описание', reply_markup=None)  


@dp.message_handler(state=FSMAdder.description)
async def load_desc(message = types.Message, state = FSMAdder.description):
    logging.info(message.from_user)
    async with state.proxy() as data:
        data['description'] = message.text
        data['username'] = message.from_user.first_name
        data['chat_id'] = message.from_user.id
        logging.info(f'Data: {data}')
        logging.info(f'Message {message.from_user}')
    answerBD = await database.add_new_application(state)
    await state.finish()

    if answerBD:
        #Оповещение админу 
        await alert_for_admin(dp)
        await message.reply("Ваша заявка добалена.")
        await bot.send_message(message.from_user.id,'Вот, что ты можешь сделать', reply_markup=choise)
    else:
        await message.reply("Ошибка! Попробуйте еще раз :)")


@dp.callback_query_handler(buy_callback.filter(item_name = 'myApplication'))
async def myApplication(call: CallbackQuery,callback_data: dict):
    user_id = call.from_user.id
    logging.info(f"User_INFO: {call.from_user}")
    record = await database.get_my_application(user_id)
    delete_str = '<Record row=('
    logging.info(f"record from bot= {record}")
    if record is None:
        await bot.send_message(user_id,'Что-то пошло ни так. Попробуйте снова :)',reply_markup=choise)
    if len(record) == 0 :
        await bot.send_message(user_id,'У вас пока нет заявок',reply_markup=choise)
        return
    for i in record:
        string = str(i) 
        string = string.replace(delete_str,'')
        string = string.replace(')>','')
        logging.info(string)
        array_message = create_array_for_print(string)
        await bot.send_photo(user_id, str(array_message[1]), f'Описание:\n{array_message[2]}\n\nСтатус:\n{array_message[3]}')
    await bot.send_message(user_id,'Вот, что ты можешь сделать', reply_markup=choise)

@dp.message_handler(commands= 'view')
async def myApplication(message: types.Message):
    user_id = message.from_user.id
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
    await call.answer("Чтобы открыть меню введите /menu", show_alert=False)
    await call.message.delete()
    await call.message.edit_reply_markup(reply_markup=None)
