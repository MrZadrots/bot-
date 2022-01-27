from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from keyboards.inline import callback_data_campus
from keyboards.inline.callback_data_campus import campus_callback

second_flor = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text = '1 этаж', callback_data = campus_callback.new(
                item_name="flor", item_value='1 этаж'
            )),
            InlineKeyboardButton(text = '2 этаж', callback_data=campus_callback.new(
                item_name="flor", item_value='2 этаж'
            )),
            InlineKeyboardButton(text = '3 этаж', callback_data=campus_callback.new(
                item_name="flor", item_value='3 этаж'
            )),
             InlineKeyboardButton(text = '4 этаж', callback_data=campus_callback.new(
                item_name="flor", item_value='4 этаж'
            ))
            
        ],
        [
            InlineKeyboardButton(text="Отмена",callback_data="cancel")
        ]
    ]
)
