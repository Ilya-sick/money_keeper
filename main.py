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
        f"Добро пожаловать, {message.from_user.first_name}!\n"
        "I'm MoneyKeeperBot!😊\n\n"
        'Пример добавления расхода:  <b><i>"магазин 50"</i></b>,  "<b><i>Такси 200</i></b>"\n\n'
        "Посмотреть все категории: /categories\n", 
        parse_mode=types.ParseMode.HTML
        )
    

@dp.message_handler(commands=['categories'])
async def show_all_categories(message: types.Message):
    """
    This handler will be called when user sends `/categories'
    """
    for cat_key in expenses.categories:
        show_all_categories = f"• <b>{expenses.categories[cat_key][0]}</b> ({', '.join(expenses.categories[cat_key][1:])})"
        await message.answer(
            f"{show_all_categories}", 
            parse_mode=types.ParseMode.HTML
            )
    await message.answer(
        'Пример добавления расхода:  <b><i>"магазин 50"</i></b>,  "<b><i>Такси 200</i></b>"\n'
        "Посмотреть статистику: /statistics\n"
        "Наибольшая трата за все время по категориям: /largest_payment\n", 
        parse_mode=types.ParseMode.HTML
        )
    

@dp.message_handler(commands = ['statistics'])
async def get_statistics_to_user(message: types.Message):
    try:
        for category in expenses.categories.keys():
            show_stat = expenses.get_statistics(message.from_user.id, category)
            show_expense_per_month = expenses.get_all_expenses_for_month(message.from_user.id)
            await message.answer(
                show_stat, 
                parse_mode=types.ParseMode.HTML
                )
        await message.answer(
            f"• <b>всего</b> (месяц): {show_expense_per_month}", 
            parse_mode=types.ParseMode.HTML
            )
        await message.answer(
            "Наибольшая трата за все время по категориям: /largest_payment\n", 
            parse_mode=types.ParseMode.HTML
            )
    except:
        pass


@dp.message_handler(commands = ['largest_payment'])
async def get_largest_payment_to_user(message: types.Message):
    try:
        for category in expenses.categories.keys():
            show_largest_payment_per_month = expenses.get_largest_payment_per_month(message.from_user.id, category)
            await message.answer(
                f"• Наибольшая трата в категории <b>{expenses.categories[category][0]}</b>: <b>{show_largest_payment_per_month}</b>р.", 
                parse_mode=types.ParseMode.HTML
                )
    except:
        pass

    
@dp.message_handler(commands=['del'])
async def del_last_expense(message: types.Message):
    try:
        del_last_exp = expenses.del_last_expenses(message.from_user.id)
        await message.answer(
            del_last_exp,
            parse_mode= types.ParseMode.HTML
        )
    except:
        pass


# handling users message
@dp.message_handler()
async def add_expense(message: types.Message):
    try:
        expense = expenses.add_expense(message.text, message.from_user.id)
        text_answer = f"{message.from_user.first_name}, {expense}\nпосмотреть все категории:  /categories\nпосмотреть статистику:  /statistics\n\nудалить последний расход:  /del\n"
        await message.answer(text_answer, parse_mode=types.ParseMode.HTML)
    except:
        await message.reply(
            "Что-то пошло не так, попробуйте снова😔\n"
            'Пример добавления расхода:  <b><i>"магазин 50"</i></b>,  "<b><i>Такси 200</i></b>"\n'
            "Посмотреть все категории: /categories\n", 
            parse_mode=types.ParseMode.HTML
            )


    

        




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)