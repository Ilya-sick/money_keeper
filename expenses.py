#money_keeper

import db

from unicodedata import category


categories = {
    'food':['еда', 'продукты'],
    'transport':['транспорт','метро', 'такси', 'маршрутка', 'автобус'],
    'clothes' : ['одежда', 'шмотки', 'обувь'],
    'communications' : ['связь', 'телефон', 'интернет', 'билайн'],
    'baby' : ['ребенок', 'ребёнок', 'малыш', 'памперсы', 'подгузники', 'смесь'],
    'money_transfer' : ['переводы', 'перевод', 'скинул', 'перевел', 'перевёл'],
    'apartments' : ['квартира', 'мебель', 'леруа'],
    'pharmacy' : ['аптека', 'таблетки'],
    'gos_uslugi' : ['налоги', 'квартплата'],
    'auto' : ['автомобиль', 'веста', 'авто', 'машина', 'бензин', 'запчасти'],
    'trip' : ['путешествия', 'арзамас', 'питер'],
    'restaurant' : ['ресторан', 'кафе', 'кофе', 'шаверма'],
    'other' : ['другое']
}

# looking for category and send parsed message to db
def add_expense(users_message):
    parsed_message = parse_message(users_message)
    find_categories = add_categories(parsed_message[0])
    send_exp_cat_in_db = db.add_expense_and_category_in_db(parsed_message[1], find_categories)
            
    return f'Ваш расход - {parsed_message[1]}р. добавлен в категорию {categories[find_categories][0]}!'


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


def show_all_categories_to_user():
    for cat_key in categories:
        print (f"{categories[cat_key]} : {categories[cat_key]}")
        return f"{categories[cat_key]}"