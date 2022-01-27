from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from keyboards.inline import callback_data_campus
from keyboards.inline.callback_data_campus import campus_callback

campus_keyboard = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text = '1 корпус', callback_data = campus_callback.new(
                item_name="campus", item_value='1 корпус'
            )),
            InlineKeyboardButton(text = '2 корпус', callback_data=campus_callback.new(
                item_name="campus", item_value='2 корпус'
            )),
            InlineKeyboardButton(text = '3 корпус', callback_data=campus_callback.new(
                item_name="campus", item_value='3 корпус'
            ))
            
        ],
        [
            InlineKeyboardButton(text="Отмена",callback_data="cancel")
        ]
    ]
)
