from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



first: InlineKeyboardMarkup = InlineKeyboardMarkup (
    inline_keyboard=[
        [
            InlineKeyboardButton(text="subscribe", callback_data="subscribe"),
            InlineKeyboardButton(text="unsubscribe", callback_data="unsubscribe")
        ]
    ]
)

def create_button(ft, list_answer):
    a = len(list_answer[ft])
    return InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=list_answer[ft][i], callback_data=str(i)) for i in range(0, a)
        ]
    ]
)