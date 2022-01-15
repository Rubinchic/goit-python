from aiogram import Bot, Dispatcher, executor, types
import asyncio
from loader import dp, bot
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from datetime import datetime


async def on_startup(dispatcher):
    # Уведомляет про запуск
    await on_startup_notify(dispatcher)

# тестовый таймер
'''async def scheduled(wait_for):
    while True:
        await asyncio.sleep(wait_for)

        now = datetime.utcnow()
        await bot.send_message(594936610, f"{now}", disable_notification = True)'''


if __name__ == '__main__':
    '''loop = asyncio.get_event_loop()
    loop.create_task(scheduled(10))'''
    executor.start_polling(dp, on_startup=on_startup)