from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from keyboards.inline import callback_data_campus
from keyboards.inline.callback_data_campus import campus_callback

first_flor = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text = '1', callback_data = campus_callback.new(
                item_name="flor", item_value='1 этаж'
            )),
            InlineKeyboardButton(text = '2', callback_data=campus_callback.new(
                item_name="flor", item_value='2 этаж'
            )),
            InlineKeyboardButton(text = '3', callback_data=campus_callback.new(
                item_name="flor", item_value='3 этаж'
            )),
            InlineKeyboardButton(text = '4', callback_data=campus_callback.new(
                item_name="flor", item_value='4 этаж'
            )),
            InlineKeyboardButton(text = '5', callback_data=campus_callback.new(
                item_name="flor", item_value='5 этаж'
            ))
            
        ],
    ]
)

second_flor = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text = '1', callback_data = campus_callback.new(
                item_name="flor", item_value='1 этаж'
            )),
            InlineKeyboardButton(text = '2', callback_data=campus_callback.new(
                item_name="flor", item_value='2 этаж'
            )),
            InlineKeyboardButton(text = '3', callback_data=campus_callback.new(
                item_name="flor", item_value='3 этаж'
            )),
            InlineKeyboardButton(text = '4', callback_data=campus_callback.new(
                item_name="flor", item_value='4 этаж'
            )),
            InlineKeyboardButton(text = '5', callback_data=campus_callback.new(
                item_name="flor", item_value='5 этаж'
            )),
            InlineKeyboardButton(text = '6', callback_data=campus_callback.new(
                item_name="flor", item_value='6 этаж'
            ))        
        ],
    ]
)

third_flor = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text = '1', callback_data = campus_callback.new(
                item_name="flor", item_value='1 этаж'
            )),
            InlineKeyboardButton(text = '2', callback_data=campus_callback.new(
                item_name="flor", item_value='2 этаж'
            ))       
        ],
    ]
)
fourth_flor = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text = '1', callback_data = campus_callback.new(
                item_name="flor", item_value='1 этаж'
            )),
            InlineKeyboardButton(text = '2', callback_data=campus_callback.new(
                item_name="flor", item_value='2 этаж'
            )),
            InlineKeyboardButton(text = '3', callback_data=campus_callback.new(
                item_name="flor", item_value='3 этаж'
            )),
             InlineKeyboardButton(text = '4', callback_data=campus_callback.new(
                item_name="flor", item_value='4 этаж'
            )),
             InlineKeyboardButton(text = '5', callback_data=campus_callback.new(
                item_name="flor", item_value='5 этаж'
            ))
            
        ],
    ]
)


fifth_flor = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text = '1', callback_data = campus_callback.new(
                item_name="flor", item_value='1 этаж'
            )),
            InlineKeyboardButton(text = '2', callback_data=campus_callback.new(
                item_name="flor", item_value='2 этаж'
            ))     
        ],
    ]
)

sixth_flor = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text = '1', callback_data = campus_callback.new(
                item_name="flor", item_value='1 этаж'
            )),
            InlineKeyboardButton(text = '2', callback_data=campus_callback.new(
                item_name="flor", item_value='2 этаж'
            )),
            InlineKeyboardButton(text = '3', callback_data=campus_callback.new(
                item_name="flor", item_value='3 этаж'
            )), 
            InlineKeyboardButton(text = '4', callback_data=campus_callback.new(
                item_name="flor", item_value='4 этаж'
            ))
        ],
        [
            InlineKeyboardButton(text = '5', callback_data=campus_callback.new(
                item_name="flor", item_value='5 этаж'
            )),
            InlineKeyboardButton(text = '6', callback_data=campus_callback.new(
                item_name="flor", item_value='6 этаж'
            )),
            InlineKeyboardButton(text = '7', callback_data=campus_callback.new(
                item_name="flor", item_value='7 этаж'
            )),
            InlineKeyboardButton(text = '8', callback_data=campus_callback.new(
                item_name="flor", item_value='8 этаж'
            )),
        ],
        [
            InlineKeyboardButton(text = '9', callback_data=campus_callback.new(
                item_name="flor", item_value='9 этаж'
            )),
            InlineKeyboardButton(text = '10', callback_data=campus_callback.new(
                item_name="flor", item_value='10 этаж'
            )),
            InlineKeyboardButton(text = '11', callback_data=campus_callback.new(
                item_name="flor", item_value='11 этаж'
            ))  
        ]
    ]

)

seventh_flor = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text = '1', callback_data = campus_callback.new(
                item_name="flor", item_value='1 этаж'
            )),
            InlineKeyboardButton(text = '2', callback_data=campus_callback.new(
                item_name="flor", item_value='2 этаж'
            )),
            InlineKeyboardButton(text = '3', callback_data=campus_callback.new(
                item_name="flor", item_value='3 этаж'
            )), 
            InlineKeyboardButton(text = '4', callback_data=campus_callback.new(
                item_name="flor", item_value='4 этаж'
            ))
        ],
        [
            InlineKeyboardButton(text = '5', callback_data=campus_callback.new(
                item_name="flor", item_value='5 этаж'
            )),
            InlineKeyboardButton(text = '6', callback_data=campus_callback.new(
                item_name="flor", item_value='6 этаж'
            )),
            InlineKeyboardButton(text = '7', callback_data=campus_callback.new(
                item_name="flor", item_value='7 этаж'
            )),
            InlineKeyboardButton(text = '8', callback_data=campus_callback.new(
                item_name="flor", item_value='8 этаж'
            ))
        ]
    ]
)

eighth_flor = InlineKeyboardMarkup(row_width=5,
    inline_keyboard = [
        [
            InlineKeyboardButton(text = '1', callback_data = campus_callback.new(
                item_name="flor", item_value='1 этаж'
            )),
            InlineKeyboardButton(text = '2', callback_data=campus_callback.new(
                item_name="flor", item_value='2 этаж'
            )),
            InlineKeyboardButton(text = '3', callback_data=campus_callback.new(
                item_name="flor", item_value='3 этаж'
            )), 
            InlineKeyboardButton(text = '4', callback_data=campus_callback.new(
                item_name="flor", item_value='4 этаж'
            )),  
        ],
        [
            InlineKeyboardButton(text = '5', callback_data=campus_callback.new(
                item_name="flor", item_value='5 этаж'
            )),
            InlineKeyboardButton(text = '6', callback_data=campus_callback.new(
                item_name="flor", item_value='6 этаж'
            )),
            InlineKeyboardButton(text = '7', callback_data=campus_callback.new(
                item_name="flor", item_value='7 этаж'
            )),
            InlineKeyboardButton(text = '8', callback_data=campus_callback.new(
                item_name="flor", item_value='8 этаж'
            ))
        ]
    ]
)

