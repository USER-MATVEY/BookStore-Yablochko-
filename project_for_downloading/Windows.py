import functools
import UserSide
import AdminSide
from PyQt6.QtCore import Qt
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


# Complete
class StartWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUI__()

    def __initUI__(self):
        self.resize(300, 200)
        self.setWindowTitle('Книжный магазин "Яблочко"')
        greeting_text = QLabel(
            """Приветствуем вас в нашем магазине!""")
        login_button = QPushButton("Вход")
        register_button = QPushButton("Регистрация")

        start_layout = QVBoxLayout()
        start_layout.addWidget(greeting_text)
        start_layout.addWidget(login_button)
        start_layout.addWidget(register_button)

        central_widget = QWidget()
        central_widget.setLayout(start_layout)
        self.setCentralWidget(central_widget)

        login_button.clicked.connect(self.login)
        register_button.clicked.connect(self.register)

    def login(self):
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()

    def register(self):
        self.register_window = RegisterWindow()
        self.register_window.show()
        self.close()


# Complete
class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUI__()

    def __initUI__(self):
        self.resize(300, 200)
        self.setWindowTitle('Книжный магазин "Яблочко"')
        self.email_input = QLineEdit()
        self.passwd_input = QLineEdit()
        submit_button = QPushButton("Войти")
        return_button = QPushButton("Назад")

        input_layout = QFormLayout()
        main_layout = QVBoxLayout()
        input_layout.addRow("Ваш e-mail:", self.email_input)
        input_layout.addRow("Ваш пароль:", self.passwd_input)
        main_layout.addLayout(input_layout)
        main_layout.addWidget(submit_button)
        main_layout.addWidget(return_button)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
        self.show()

        submit_button.clicked.connect(self.validate_user_login)  # TODO: доработать проверку валидности логина
        return_button.clicked.connect(self.back)  # TODO: Переделать

    def validate_user_login(self):
        e_mail = self.email_input.text()
        passwd = self.passwd_input.text()
        user = UserSide.valid_login(e_mail, passwd)
        if user == "user":
            self.UserSession = MainUserWindow()
            self.UserSession.show()
            self.close()
        elif user == "ADMIN":
            self.AdmSession = MainAdminWindow()
            self.AdmSession.show()
            self.close()
        else:
            error_dialog = QMessageBox()
            error_dialog.setIcon(QMessageBox.Icon.Critical)
            error_dialog.setWindowTitle("Ошибка")
            error_dialog.setText("Неправильный логин или пароль.")
            error_dialog.exec()

    def back(self):
        self.start_window = StartWindow()
        self.start_window.show()
        self.close()


# Complete
class RegisterWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUI__()

    def __initUI__(self):
        self.resize(300, 300)
        self.setWindowTitle('Книжный магазин "Яблочко"')

        self.name_input = QLineEdit()
        self.telephone_input = QLineEdit()
        self.email_input = QLineEdit()
        self.passwd_input = QLineEdit()
        register_button = QPushButton("Зарегистрироваться")
        return_button = QPushButton("Назад")

        input_layout = QFormLayout()
        input_layout.addRow("Ваш e-mail:", self.email_input)
        input_layout.addRow("Ваше имя:", self.name_input)
        input_layout.addRow("Ваш телефон:", self.telephone_input)
        input_layout.addRow("Ваш пароль:", self.passwd_input)
        main_layout = QVBoxLayout()
        main_layout.addLayout(input_layout)
        main_layout.addWidget(register_button)
        main_layout.addWidget(return_button)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
        self.show()

        register_button.clicked.connect(self.register_user)
        return_button.clicked.connect(self.back)  # TODO: Переделать

    def register_user(self):
        info = [
            self.name_input.text(),
            self.telephone_input.text(),
            self.email_input.text(),
            self.passwd_input.text()
        ]

        if UserSide.valid_login(info[2], info[3]) != "NO":
            error_dialog = QMessageBox()
            error_dialog.setIcon(QMessageBox.Icon.Critical)
            error_dialog.setWindowTitle("Ошибка")
            error_dialog.setText("Пользователь с такой почтой уже есть!")
            error_dialog.exec()
        else:
            UserSide.register_user(info)
            self.UserSession = MainUserWindow()
            self.UserSession.show()
            self.close()

    def back(self):
        self.start_window = StartWindow()
        self.start_window.show()
        self.close()


# Complete FOR DEMO
class MainUserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUI__()

    def __initUI__(self):
        self.resize(400, 300)
        self.setWindowTitle('Книжный Магазин "Яблочко"')

        catalog_button = QPushButton("Каталог")
        user_orders_button = QPushButton("Ваши заказы")
        user_info_button = QPushButton("Ваш аккаунт")
        logout_button = QPushButton("Выйти из аккаунта")

        buttons_layout = QVBoxLayout()
        buttons_layout.addWidget(catalog_button)
        buttons_layout.addWidget(user_orders_button)
        buttons_layout.addWidget(user_info_button)
        buttons_layout.addWidget(logout_button)

        central_widget = QWidget()
        central_widget.setLayout(buttons_layout)
        self.setCentralWidget(central_widget)

        catalog_button.clicked.connect(self.open_catalog)
        user_orders_button.clicked.connect(self.open_orders)
        logout_button.clicked.connect(self.logout)

    def open_catalog(self):
        self.catalog = UserCatalogWindow()
        self.catalog.show()

    def open_orders(self):
        self.order_win = UserOrdersWindow()
        self.order_win.show()

    def logout(self):
        self.new_start = StartWindow()
        self.new_start.show()
        self.close()


class MainAdminWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUI__()

    def __initUI__(self):
        self.resize(300, 200)
        self.setWindowTitle('Книжный Магазин "Яблочко"')

        catalog_button = QPushButton("Изменение Каталога")
        user_orders_button = QPushButton("Заказы")
        user_info_button = QPushButton("Список аккаунтов")
        logout_button = QPushButton("Выйти из аккаунта")

        buttons_layout = QVBoxLayout()
        buttons_layout.addWidget(catalog_button)
        buttons_layout.addWidget(user_orders_button)
        buttons_layout.addWidget(user_info_button)
        buttons_layout.addWidget(logout_button)

        central_widget = QWidget()
        central_widget.setLayout(buttons_layout)
        self.setCentralWidget(central_widget)

        catalog_button.clicked.connect(self.open_catalog_menu)
        logout_button.clicked.connect(self.logout)

    def open_catalog_menu(self):
        self.catalog_menu = AdminCatalogWindow()
        self.catalog_menu.show()

    def logout(self):
        self.new_start = StartWindow()
        self.new_start.show()
        self.close()


# Complete FOR DEMO
class UserCatalogWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        UserSide.set_books()
        self.__initUI__()

    def __initUI__(self):
        self.resize(400, 300)
        self.setWindowTitle('Книжный магазин "Яблочко"')

        book_group = QGroupBox()
        work_group = QGroupBox()

        self.rnd_book_1 = QPushButton("Книга 1")
        self.rnd_book_2 = QPushButton("Книга 2")
        self.rnd_book_3 = QPushButton("Книга 3")
        self.rnd_book_4 = QPushButton("Книга 4")
        self.rnd_book_5 = QPushButton("Книга 5")
        self.rnd_book_6 = QPushButton("Книга 6")
        self.rnd_book_1.setObjectName("rndButton")
        self.rnd_book_2.setObjectName("rndButton")
        self.rnd_book_3.setObjectName("rndButton")
        self.rnd_book_4.setObjectName("rndButton")
        self.rnd_book_5.setObjectName("rndButton")
        self.rnd_book_6.setObjectName("rndButton")

        book_type_choose = QComboBox()
        book_type_choose.addItems(["Фантастика", "Фэнтези", "Классика", "Стихи"])
        shuffle_book_button = QPushButton("Мне повезёт с книгой!")
        create_order_button = QPushButton("Оформить заказ по текущей корзине")
        refresh_basket = QPushButton("Обновить корзину")
        clear_basket_button = QPushButton("Очисить корзину")
        self.info = QListWidget(self)

        book_layout_1 = QHBoxLayout()
        book_layout_2 = QHBoxLayout()
        book_group_layout = QVBoxLayout()
        book_layout_1.addWidget(self.rnd_book_1)
        book_layout_1.addWidget(self.rnd_book_2)
        book_layout_1.addWidget(self.rnd_book_3)
        book_layout_2.addWidget(self.rnd_book_4)
        book_layout_2.addWidget(self.rnd_book_5)
        book_layout_2.addWidget(self.rnd_book_6)
        book_group_layout.addLayout(book_layout_1)
        book_group_layout.addLayout(book_layout_2)

        info_layout = QVBoxLayout()
        info_layout.addWidget(book_type_choose)
        info_layout.addWidget(shuffle_book_button)
        info_layout.addWidget(create_order_button)
        info_layout.addWidget(refresh_basket)
        info_layout.addWidget(clear_basket_button)
        info_layout.addWidget(self.info)

        work_group.setLayout(info_layout)
        book_group.setLayout(book_group_layout)

        main_layout = QHBoxLayout()
        main_layout.addWidget(book_group)
        main_layout.addWidget(work_group)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
        self.show()

        shuffle_book_button.clicked.connect(UserSide.set_books)
        refresh_basket.clicked.connect(self.refresh)
        clear_basket_button.clicked.connect(self.clear_basket)
        create_order_button.clicked.connect(self.create_order)

        self.rnd_book_1.clicked.connect(self.open_book)
        self.rnd_book_2.clicked.connect(self.open_book)
        self.rnd_book_3.clicked.connect(self.open_book)
        self.rnd_book_4.clicked.connect(self.open_book)
        self.rnd_book_5.clicked.connect(self.open_book)
        self.rnd_book_6.clicked.connect(self.open_book)

    def open_book(self):
        book_info = UserSide.get_book()
        self.book_win = BookWindow(book_info)
        self.book_win.show()

    def refresh(self):
        self.clear_basket()
        books = UserSide.get_basket()
        for book in books:
            self.info.addItem(book)

    def create_order(self):
        items = UserSide.get_basket()
        UserSide.new_order(items)

    def clear_basket(self):
        self.info.clear()


# Complete
class BookWindow(QMainWindow):
    def __init__(self, info_list):
        super().__init__()
        self.info = info_list
        self.__initUI__()

    def __initUI__(self):
        self.resize(400, 300)
        self.setWindowTitle('Книжный магазин "Яблочко"')

        central_widget = QWidget()
        main_layout = QHBoxLayout()

        image_label = QLabel()
        image = QPixmap(self.info["path"])
        image = image.scaled(200, 300)
        image_label.setPixmap(image)

        info_layout = QVBoxLayout()

        title_label = QLabel('Название: ' + self.info["bookname"])
        author_label = QLabel('Автор: ' + self.info["author"])
        genre_label = QLabel('Жанр: ' + self.info["genre"])
        publisher_label = QLabel('Издательство: ' + self.info["publisher"])
        year_label = QLabel('Год издания: ' + self.info["publication_date"])
        price_label = QLabel('Цена: ' + str(self.info["price"]))

        info_layout.addWidget(title_label)
        info_layout.addWidget(author_label)
        info_layout.addWidget(genre_label)
        info_layout.addWidget(publisher_label)
        info_layout.addWidget(year_label)
        info_layout.addWidget(price_label)

        button_layout = QHBoxLayout()
        add_to_cart_button = QPushButton('В корзину')
        close_button = QPushButton('Закрыть')
        add_to_cart_button.setObjectName("ordButton")
        close_button.setObjectName("ordButton")

        button_layout.addWidget(add_to_cart_button)
        button_layout.addWidget(close_button)

        info_layout.addLayout(button_layout)

        main_layout.addWidget(image_label)
        main_layout.addLayout(info_layout)

        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        add_to_cart_button.clicked.connect(self.to_basket)
        close_button.clicked.connect(self.close)

    def to_basket(self):
        UserSide.add_to_basket(self.info["bookname"])


# Complete
class UserOrdersWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.orders = UserSide.get_user_orders()
        self.__initUI__()

    def __initUI__(self):
        self.setWindowTitle('Список заказов')
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        title_label = QLabel('Список заказов', self)
        title_label.setFont(QFont('Arial', 16))
        layout.addWidget(title_label)

        table = QTableWidget(self)
        table.setColumnCount(5)
        table.setHorizontalHeaderLabels(['Номер заказа', 'Дата', 'Сумма', 'Статус', 'Товары'])
        table.setRowCount(len(self.orders))

        row_num = 0
        for order in self.orders:
            table.setItem(row_num, 0, QTableWidgetItem(order))
            table.setItem(row_num, 1, QTableWidgetItem(self.orders[order]["date"]))
            table.setItem(row_num, 2, QTableWidgetItem(str(self.orders[order]["sum_price"])))
            table.setItem(row_num, 3, QTableWidgetItem(self.orders[order]["order_status"]))

            products_button = QPushButton('Просмотреть товары', self)
            products_button.setObjectName("ordButton")
            products_button.clicked.connect(functools.partial(self.show_product_list, order))
            table.setCellWidget(row_num, 4, products_button)
            row_num += 1

        # Настройка таблицы
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        layout.addWidget(table)

    def show_product_list(self, order):
        self.product_list_window = ProductListWindow(self.orders[order]["books"])
        self.product_list_window.show()


# Complete
class ProductListWindow(QMainWindow):
    def __init__(self, books):
        super().__init__()
        self.books_list = books
        self.__initUI__()

    def __initUI__(self):
        self.setWindowTitle('Список товаров')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()
        self.setLayout(layout)

        title_label = QLabel('Список товаров', self)
        title_label.setFont(QFont('Arial', 16))
        layout.addWidget(title_label)

        list_widget = QListWidget(self)
        for book in self.books_list:
            list_widget.addItem(book)
        layout.addWidget(list_widget)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


class AdminCatalogWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUI__()

    def __initUI__(self):
        self.resize(400, 400)
        self.setWindowTitle('Книжный магазин "Яблоко"')

        show_catalog_button = QPushButton("Открыть список книг в каталоге")
        add_book_button = QPushButton("Добавить книгу в каталог")
        change_book_button = QPushButton("Изменить книгу")
        delete_book_button = QPushButton("Удалить книгу")

        button_layout = QVBoxLayout()
        button_layout.addWidget(show_catalog_button)
        button_layout.addWidget(add_book_button)
        button_layout.addWidget(change_book_button)
        button_layout.addWidget(delete_book_button)

        central_widget = QWidget()
        central_widget.setLayout(button_layout)
        self.setCentralWidget(central_widget)
