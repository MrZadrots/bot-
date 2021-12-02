from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from keyboards.inline.callback_data import buy_callback

choise = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text = 'Добавить новую заявку', callback_data="add",
            ),
            InlineKeyboardButton(text = 'Посмотреть мои заявки', callback_data=buy_callback.new(
                item_name="myApplication",
            ))
        ],
        [
            InlineKeyboardButton(text="Отмена",callback_data="cancel")
        ]
    ]
)
