from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import sqlite3
import asyncio
from datetime import datetime, timedelta

# Инициализация бота
bot = Bot(token='6709488553:AAHD6B6kEBKDuWJeYRuCOewGIOICi8Iin-A')  # Замените на ваш реальный токен
dp = Dispatcher(bot)

# Подключение к базе данных
conn = sqlite3.connect('birthdays.db')
cursor = conn.cursor()

# Функция для отправки сообщения
async def send_reminder(chat_ids, text):
    for chat_id in chat_ids:
        await bot.send_message(chat_id, text)

chat_ids = ['1614745488', '5370135122', '859201191', '900444056', '487990460', '873239242', '175940933', '1132572310', '362695376', '740060512', '670750262', '6546647143', '561082095', '1316887740', '6299553224', '702560359', '370259515', '850931530', '936636955', '5151319918', '1046584303']  # Замените на ваши реальные chat_ids

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет, напоминалка уже запущена, ты успеешь вовремя поздравить своих друзей!")

async def main():
    while True:
        # Получение текущей даты
        current_date = datetime.now().date()

        # Получение списка дней рождения из базы данных
        cursor.execute("SELECT name, birthday FROM people")
        birthdays = cursor.fetchall()

        # Отправка напоминаний за 7 дней и за 1 день до дня рождения
        for name, birthday in birthdays:
            bday_date = datetime.strptime(birthday, '%Y-%m-%d').date()
            if current_date + timedelta(days=7) == bday_date:
                await send_reminder(chat_ids, f"Через 7 дней у {name} день рождения!")
            elif current_date + timedelta(days=1) == bday_date:
                await send_reminder(chat_ids, f"Завтра у {name} день рождения!")

        # Задержка на 24 часа
        await asyncio.sleep(24 * 60 * 60)

    # Закрытие соединения с базой данных
    conn.close()

# Запуск асинхронной функции
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    executor.start_polling(dp, skip_updates=True)





# 6709488553:AAHD6B6kEBKDuWJeYRuCOewGIOICi8Iin-A
# 1614745488
# 5370135122
# await asyncio.sleep(24 * 60 * 60)
# '5231075040',
# await asyncio.sleep(0.2 * 0.2)
# '859201191', '900444056', '487990460', '873239242', '175940933', '1132572310', '362695376', '740060512', '670750262', '6546647143', '561082095', '1316887740', '6299553224', '702560359', '370259515', '850931530', '936636955', '5151319918', '1046584303']