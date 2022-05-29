#money_keeper

from config import TOKEN
import logging
from aiogram import Bot, Dispatcher, executor, types
import expenses



API_TOKEN = TOKEN

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply(
        "Добро пожаловать!\n"
        "I'm MoneyKeeperBot!\n"
        "Пример добавления расхода: 'такси 50'\n"
        )


@dp.message_handler()
async def add_expense(message: types.Message):
    try:
        expense = expenses.add_expense(message.text)
        t = f'Мы на верном пути, {expense}'
        await message.answer(t)
    except:
        pass
    

        




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)