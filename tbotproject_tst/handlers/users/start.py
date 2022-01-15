from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default import *
from states import Flow

from loader import dp


@dp.message_handler(CommandStart(), state=Flow.RegistrState)
async def we_have_number(message: types.Message):
    await message.answer("И снова здравствуй")


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}, для продолжения роботы нам необходимо узнать твой номер.\nДля этого тебе нужно просто нажать на кнопку снизу", reply_markup=start_keyboard)
