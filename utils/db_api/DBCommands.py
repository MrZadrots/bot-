'''
from asyncpg import Connection, Record
from asyncpg.exceptions import UniqueViolationError
#from loader import dp, db
from aiogram import types
import logging

class DBCommands: 
    def init(db):
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
            record = await self.pool.fetch(command,args)
            logging.info(f"record from bd= {record}")
            return record
        except UniqueViolationError:
            pass
'''