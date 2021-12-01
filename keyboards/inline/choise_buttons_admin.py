from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from keyboards.inline.callback_data import buy_callback

choise_admin = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text = 'Посмотреть все заявки', callback_data=buy_callback.new(
               item_name="milk", quantity=1
            )),
            InlineKeyboardButton(text = 'Изменить заявку', callback_data=buy_callback.new(
              item_name="kefir", quantity=1
            ))
        ],
        [
            InlineKeyboardButton(text="Отмена",callback_data="cancel")
        ]
    ]
)
