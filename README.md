
# MoneyKeeperBot

Telegram Bot for accounting user`s expenses.

Bot created for users, who like Telegram and simle interface.

Category:
• <b>магазин</b> (еда, продукты, памперсы, аптека)
• <b>транспорт</b> (метро, такси, маршрутка, автобус)
• <b>одежда</b> (обувь)
• <b>связь</b> (телефон, интернет, билайн)
• <b>переводы</b> (перевод, скинул, перевел, перевёл)
• <b>квартира</b> (мебель, леруа)
• <b>налоги</b> (квартплата)
• <b>автомобиль</b> (веста, авто, машина, бензин, запчасти)
• <b>кафе</b> (ресторан, кофе, шаверма)
• <b>другое</b> (ерунда)

# How to use:

For starting send command "/_start_".

For viewing all categories send "/_categories_".

For saving expenses, send message to MoneyKeeperBot in format: "category expense" (_for example_: "Магазин 200", "такси 180", "шАвЕрМа 150"). Not case sensitive.

For viewing statistics, choose command "/_statistics_". User gets statistics in format: "category (day/month) : expenses_per_day/expenses_per_month" for all categories (_for example_: • <b>магазин</b> (день/<b>месяц</b>) : 0/<b>200</b>)

For delete last expense, choose command "/_del_".

Bot features:

- _keep your expenses_
- _show statistics_
- _delete last records_

Library: aiogram, sqlite3

DataBase: SQLite

# Simply and easily!
