from aiogram import types

from keyboards.inline import *
from keyboards.default import *
from loader import dp, bot
from states import Flow

from aiogram import Bot, Dispatcher, executor, types


lst_answer = [
    ['1980', '1989'],
    ['aiogram', 'telebot']
]


#и так, мы получили номер телефона:)
@dp.message_handler(content_types=types.ContentTypes.CONTACT)
async def we_have_contact(message):
    await Flow.RegistrState.set()
    await message.answer(f'добро пожаловать, {message.contact.first_name} (*^▽^*)')

#состояния
#@dp.message_handler()
#async def check_states():
#    await ()


#quiz
@dp.message_handler(commands=['quiz'])
async def start_quiz(message: types.Message):
    await message.answer('И так, ты стал участником игры "угадайка". Первый вопрос:\nв каком году Гвидо ван Россум начал создания python?')

#false
@dp.message_handler(text='1980')
async def false_ft(message: types.Message):
    await message.answer('Неправильно(\nИстория языка программирования Python началась в конце 1980-х. Гвидо ван Россум задумал Python в 1980-х годах, а приступил к его созданию в декабре 1989 года.\n\nНовый вопрос:\nкакая самая популярная библиотека на python для создания telegram ботов?')

#true
@dp.message_handler(text='1989')
async def true_fy(message: types.Message):
    await message.answer(f'Молодец!\nИстория языка программирования Python началась в конце 1980-х. Гвидо ван Россум задумал Python в 1980-х годах, а приступил к его созданию в декабре 1989 года.\n\nНовый вопрос:\nкакая самая популярная библиотека на python для создания telegram ботов?')

#s_true
@dp.message_handler(text='aiogram')
async def true_s(message: types.Message):
    await message.answer('Молодец!)')

#f_true
@dp.message_handler(text='telebot')
async def true_s(message: types.Message):
    await message.answer('Не угадал, самой удобной считают aiogram)')