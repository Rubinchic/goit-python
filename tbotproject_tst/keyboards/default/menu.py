from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

'''sub_and_unsub: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="subscribe"),
            KeyboardButton(text="unsubscribe")
        ]
    ],
    resize_keyboard=True
)'''

start_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Give contact☎", request_contact = True)
        ]
    ],
    one_time_keyboard=True,
    resize_keyboard=True
)
