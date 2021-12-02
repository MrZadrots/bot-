import logging

from aiogram import Dispatcher
from asyncpg import exceptions

from data.config import ADMINS


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, "Бот Запущен")

        except Exception as err:
            logging.exception(err)

async def alert_for_admin(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin,'Добавлена новая заявка')
        except Exception as err:
            logging.exception(err)