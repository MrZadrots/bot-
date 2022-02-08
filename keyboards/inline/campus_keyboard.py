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
            )),
            InlineKeyboardButton(text = '4 корпус', callback_data=campus_callback.new(
                item_name="campus", item_value='4 корпус'
            )),
           
        ],
        [
            InlineKeyboardButton(text = '5 корпус', callback_data=campus_callback.new(
                item_name="campus", item_value='5 корпус'
            )),
            InlineKeyboardButton(text = '6 корпус', callback_data=campus_callback.new(
                item_name="campus", item_value='6 корпус'
            )),
            InlineKeyboardButton(text = '7 корпус', callback_data=campus_callback.new(
                item_name="campus", item_value='7 корпус'
            )),
            InlineKeyboardButton(text = '8 корпус', callback_data=campus_callback.new(
                item_name="campus", item_value='8 корпус'
            ))
        ],
    ]
)
