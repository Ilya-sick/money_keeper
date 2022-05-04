#money_keeper

categories = {
    'food':['еда', 'продукты'],
    'transport':['транспорт','метро', 'такси', 'маршрутка', 'автобус'],
    'clothes' : ['одежда', 'шмотки', 'обувь'],
    'communications' : ['телефон', 'связь', 'интернет', 'билайн'],
    'baby' : ['ребенок', 'ребёнок', 'малыш', 'памперсы', 'подгузники', 'смесь'],
    'money_transfer' : ['перевод', 'скинул', 'перевел', 'перевёл'],
    'apartments' : ['квартира', 'мебель', 'леруа'],
    'pharmacy' : ['аптека', 'таблетки'],
    'gos_uslugi' : ['налоги', 'квартплата'],
    'auto' : ['авто', 'автомобиль', 'машина', 'бензин', 'запчасти'],
    'trip' : ['путешествия', 'арзамас'],
    'restaurant' : ['ресторан', 'кафе', 'кофе', 'шаверма']
}
print(list(categories.values()))
#users_message = 'еда 250'


def add_expense(users_message):
    parsed_message = parse_message(users_message)
    find_categories = add_categories(parsed_message[0])

    return print(parsed_message,find_categories)



def parse_message(users_message):
    parsed = users_message.split(' ')
    if (len(parsed)) == 2 and int(parsed[1])/int(parsed[1]) == 1 and int(parsed[1]) != 0:
        return parsed
    else:
        return f"Чувак, что-то пошло не так, попробуй снова...)"

def add_categories(first_part_message):
    for category, category_values in categories.items():
        if first_part_message.lower() in category_values:
            return f'{category}'
