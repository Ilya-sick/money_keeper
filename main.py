# money_keeper

from config import TOKEN
import logging
from aiogram import Bot, Dispatcher, executor, types
import expenses
import db



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
        "I'm MoneyKeeperBot!😊\n"
        'Пример добавления расхода:  "магазин 50",  "Такси 200"\n'
        "Посмотреть все категории: '/categories'\n"
        )

@dp.message_handler(commands=['categories'])
async def show_all_categories(message: types.Message):
    """
    This handler will be called when user sends `/categories'
    """
    for cat_key in expenses.categories:
        show_all_categories = f"• {expenses.categories[cat_key][0]} ({', '.join(expenses.categories[cat_key][1:])})"
        await message.answer(
            f"{show_all_categories}"
            )
    await message.answer(
        'Пример добавления расхода:  "магазин 50",  "Такси 200"\n'
        )

@dp.message_handler(commands=['expenses'])
async def get_expense_to_user(message: types.Message):
    try:
        show_expense = db.get_expense(message.from_user.id)
        await message.answer(
            f'Пожалуйста, укажите период: "месяц", "неделя", "день".\n'
            f"{show_expense}"
        )
    except:
        pass

# handling users message
@dp.message_handler()
async def add_expense(message: types.Message):
    try:
        expense = expenses.add_expense(message.text, message.from_user.id)
        text_answer = f'Готово, {message.from_user.first_name}! {expense}' 
        await message.answer(text_answer)
    except:
        await message.reply(
            "Что-то пошло не так, попробуйте снова😔\n"
            'Пример добавления расхода:  "магазин 50",  "Такси 200"\n'
            "Посмотреть все категории: '/categories'\n"
            "Посмотреть последние расходы: '/expenses'\n"
            )


    

        




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)