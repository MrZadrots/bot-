from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from keyboards.inline.callback_data import buy_callback

choise_admin = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text='Посмотреть все заявки', callback_data=buy_callback.new(
               item_name="allApplications",
            )),
            InlineKeyboardButton(text = 'Изменить заявку', callback_data=buy_callback.new(
              item_name="changeApplication",
            ))
        ],
        [
            InlineKeyboardButton(text="Отмена",callback_data="cancel")
        ]
    ]
)
