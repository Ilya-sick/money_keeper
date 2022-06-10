#money_keeper

from calendar import month
import db
import datetime as dt


categories = {
    'food':['магазин', 'еда', 'продукты', 'памперсы', 'аптека'],
    'transport':['транспорт', 'метро', 'такси', 'маршрутка', 'автобус'],
    'clothes' : ['одежда', 'обувь'],
    'communications' : ['связь', 'телефон', 'интернет', 'билайн'],
    'money_transfer' : ['переводы', 'перевод', 'скинул', 'перевел', 'перевёл'],
    'apartments' : ['квартира', 'мебель', 'леруа'],
    'gos_uslugi' : ['налоги', 'квартплата'],
    'auto' : ['автомобиль', 'веста', 'авто', 'машина', 'бензин', 'запчасти'],
    'restaurant' : ['кафе', 'ресторан', 'кофе', 'шаверма'],
    'other' : ['другое', 'ерунда']
}

# looking for category and send parsed message to db
def add_expense(users_message, user_id):
    datetime_now = get_time_right_now()
    #datetime_today_midnight = get_date_today_midnight()
    datetime_start_month_midnight = get_date_start_month()
    parsed_message = parse_message(users_message)
    find_categories = add_categories(parsed_message[0])
    send_exp_cat_in_db = db.add_expense_and_category_to_db(parsed_message[1], find_categories, user_id, datetime_now)
    get_exp = db.get_expense(find_categories, user_id, datetime_start_month_midnight)
    get_all_expenses_for_period = get_all_expenses_for_month(user_id)
            
    return f'расход - <b><i>{parsed_message[1]}</i></b>р. добавлен в категорию <i><b>{categories[find_categories][0]}</b></i>!\n\n{categories[find_categories][0]}/месяц: {get_exp}р.\nвсего/месяц: {get_all_expenses_for_period}р.'

# split users message
def parse_message(users_message):
    parsed = users_message.split(' ')
    if (len(parsed)) == 2 and int(parsed[1]) != 0:
        return parsed
    else:
        return f"Что-то пошло не так, попробуйте снова...)"


def add_categories(first_part_message):
    for category, category_values in categories.items():
        if first_part_message.lower() in category_values:
            if category is not None:
                return f'{category}'
            else:
                return f"Такой категории нет..."


def get_all_expenses_for_month(user_id):
    start_month_midnight = get_date_start_month()
    all_categories_list = get_all_categories()
    return db.get_expense(all_categories_list, user_id, start_month_midnight)
    
def get_time_right_now():
    moscow_time = dt.datetime.utcnow() + dt.timedelta(hours=3)
    return int(moscow_time.timestamp())

def get_date_today_midnight():
    day_now = dt.datetime.utcnow() + dt.timedelta(hours=3)
    today_midnight = day_now.replace(hour=0, minute=0, second=0, microsecond=0)
    return int(today_midnight.timestamp())
    
def get_date_start_month():
    day_now = dt.datetime.utcnow() + dt.timedelta(hours=3)
    start_month_midnight = day_now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    return int(start_month_midnight.timestamp())

def get_all_categories():
    all_cat = []
    for category in categories.keys():
        all_cat.append(category)
    return f"{', '.join(all_cat)}"

def get_statistics(user_id, category):
    day_start_month = get_date_start_month()
    day_start_today = get_date_today_midnight()
    sum_month_stat = db.get_statistics(user_id, category, day_start_month)
    sum_day_stat = db.get_statistics(user_id, category, day_start_today)
    return f"• <b>{categories[category][0]}</b> (день/<b>месяц</b>) : {sum_day_stat}/<b>{sum_month_stat}</b>"
        
         
def del_last_expenses(user_id):
    delete_exp = db.find_and_del_last_expense(user_id)
    return delete_exp
    
