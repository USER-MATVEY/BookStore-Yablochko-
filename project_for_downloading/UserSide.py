import datetime
import json
from random import randint

current_user_ID = ""
books_list = ["", "", "", "", "", ""]
basket = []


def valid_login(email: str, passwd: str) -> str:
    global current_user_ID
    with open("Database/UserDatabase.json", "r") as data:
        users = json.load(data)
        for user in users:
            if users[user]["email"] == email and users[user]["passwd"] == passwd:
                if users[user]["category"] == "ADMIN":
                    return "ADMIN"
                current_user_ID = user
                return "user"
        return "NO"


def register_user(info_list: list[str]):
    with open("Database/UserDatabase.json", "r") as data:
        users = json.load(data)

    #TODO:Создание ID-генератора
    users["ID"] = {
            "name": info_list[0],
            "telephone": info_list[1],
            "email": info_list[2],
            "passwd": info_list[3],
            "category": "user"
        }

    with open("Database/UserDatabase.json", 'w') as data:
        json.dump(users, data)


def set_books():
    global books_list

    with open("Database/BookDatabase.json", "r") as data:
        books = json.load(data)
        for i in range(0, 6):
            books_list[i] = books[str(randint(0, len(books)-1))]


def get_book():
    global books_list
    return books_list[randint(0, 5)]


def add_to_basket(book):
    basket.append(book)


def get_basket():
    return basket


def get_user_orders():
    user_orders = {}
    with open("Database/OrdersDatabase.json", "r") as data:
        orders = json.load(data)
        for order in orders:
            if orders[order]["user"] == current_user_ID:
                user_orders[order] = orders[order]
    return user_orders


def new_order(book_list: list):
    with open("Database/OrdersDatabase.json", "r") as ordata:
        orders = json.load(ordata)

    #TODO: Сделать подсчёт стоимости заказа
    summ = 0

    #TODO: Сделать генерацию id
    orders["ID"] = {
        "user": current_user_ID,
        "date": str(datetime.date.today()),
        "sum_price": summ,
        "order_status": "Waiting to peak up",
        "books": book_list
    }

    with open("Database/OrdersDatabase.json", "w") as data:
        json.dump(orders, data)
