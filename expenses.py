#money_keeper

categories = ['еда']
users_message = 'еда 250'


def add_expense(users_message):
    parsed_message = parse_message(users_message)
    find_categories = add_categories(parsed_message[0])



def parse_message(users_message):
    parsed = users_message.split(' ')
    return parsed

def add_categories(first_part_message):
    print(first_part_message)
    if first_part_message in categories:
        print('ehf)'

    return first_part_message