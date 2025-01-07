"""РЕШЕНИЯ ДОМАШЕК"""

# 1-hw

a = int(input('введите первое число'))

c = int(input('введите второе число'))

print(a * c)

# 2-hw

a = int(input('введите длину прямоугольника'))

b = int(input('введите ширину прямоугольника'))

print(a * b)

# 3-hw

a = float(input("введите первое число"))

b = float(input("введите второе число"))

if a >= b:
    print(a, "большее число")
elif b >= a:
    print(b, "большее число")
else:
    print('не знаю такого')

# 4-hw

month = int(input("Введите номер месяца 1-12: "))
# у каждого месяца свой номер
if month in [12, 1, 2]:
    print("Зима")
elif month in [3, 4, 5]:
    print("Весна")
elif month in [6, 7, 8]:
    print("Лето")
elif month in [9, 10, 11]:
    print("Осень")
else:
    print("ТОЛЬКО от 1 до 12! ")

month = int(input("Введите номер месяца (1-12): "))
if month == 1 or month == 2 or month == 3:
    print("Зима")
elif month == 4 or month == 5 or month == 6:
    print("Весна")
elif month == 7 or month == 8 or month == 9:
    print("Лето")
else:
    print("Осень")

# 5-hw

birthday = float(input('введите год рождения'))
todayyear = 2024

if birthday == birthday < todayyear:
    print('ваш возраст', todayyear - birthday)
else:
    print('что ты пишешь')

#

year = int(input("Введите год рождения: "))
result = 2024 - year

print(f"Ваш возраст: {result}.")

# 6-hw

while True:
    a = input("Введите первое число: ")
    if a.lower() == "выход":
        print("Программа завершена.")
        break
    if a.isdigit() or (a[0] == '-' and a[1:].isdigit()):
        a = float(a)
    else:
        print("Ошибка: введите корректное число.")

    b = input("Введите второе число: ")
    if b.isdigit() or (b[0] == '-' and b[1:].isdigit()):
        b = float(b)
    else:
        print("Ошибка: введите корректное число.")
    op = input("Введите оператор (+, -, *, /): ")
    if op == "+":
        print(f"Результат: {a + b}")
    elif op == "-":
        print(f"Результат: {a - b}")
    elif op == "*":
        print(f"Результат: {a * b}")
    elif op == "/":
        if b == 0:
            print("Ошибка: деление на ноль.")
        else:
            print(f"Результат: {a / b}")
    else:
        print("Ошибка: некорректный оператор.")

# 7-hw
import random

secret_number = random.randint(1, 100)
user_guess = 0
print("Угадай число от 1 до 100.")

while user_guess != secret_number:
    user_guess = int(input("Введите ваше предположение: "))

if user_guess < secret_number:
    print("Больше!")
elif user_guess > secret_number:
    print("Меньше!")
else:
    print("Поздравляю! Вы угадали число!")

# 8-hw

while True:

    number = int(input("Введите число (или 0 для выхода): "))

    if number == 0:
        print("Выход из программы.")

    break

    i = 1

    while i <= 10:
        print(f"{number} * {i} = {number * i}")
        i += 1

print()

# 9-hw

# grades = {}
#
# while True:
#     name = input('введите имя ученика (напишите стоп чтоб завершить)')
#     if name == "стоп":
#         for students, grades in grades.items():
#     print(f"результаты {students} : {grades}")
#     break
#     grade = int(input('введите оценку'))
#
# grades[name] = grade


grades = {}

while True:
    name = input("Введите имя ученика (или 'стоп'): ")
    if name == 'стоп':
        break

    while True:
        grade = input("Введите оценку: ")

        if grade.isdigit() and 1 <= int(grade) <= 5:
            grades[name] = int(grade)
            break
        else:
            print("Введите оценку от 1 до 5.")

print("\nРезультаты:")
for name, grade in grades.items():
    print(f"{name}: {grade}")

# 10-hw

products = {
    "яблоко": 50,
    "банан": 30,
    "молоко": 80
}

product_name = input("Введите название продукта: ")

if product_name in products:
    print("Цена:", products[product_name])
else:
    print("Продукт не в наличии")

"""2"""

a = input("введите название продукта")

dict_1 = {"банан": 30, "яблоко": 20, "клубника": 40, "груша": 15, "молоко": 60, }

if a not in dict_1: print("такого у нас нет")

if a in dict_1: print(dict_1[a])

# 11-hw

list_of_currencies = {"USD": 89, "EUR": 88, "GBP": 101}
name = input("Введите код валюты: ")
amount = float(input("Введите количество: "))

if name in list_of_currencies:
    res = amount * list_of_currencies[name]
    print(f" Результат: {res}")
else:
    print("Может вы ввели что-то неверно?")

# 12-hw


name = input("Введите ваше имя: ")
surname = input("Введите вашу фамилию: ")
license_plate = input("Введите номерной знак: ")

if (len(license_plate) == 6 or len(license_plate) == 7) and license_plate[0].isalpha() and license_plate[
                                                                                           1:5].isdigit() and license_plate[
                                                                                                              5:].isalpha():
    license_type = "старый"
elif len(license_plate) == 6 and license_plate[:3].isdigit() and license_plate[3:].isalpha():
    license_type = "новый"
else:
    license_type = "неверный формат"

if license_type != "неверный формат":
    print(f"{name} {surname}, номерной знак {license_plate}, у Вас {license_type} образец.")
else:
    print("Номерной знак имеет неверный формат.")

#

name = input("введите свое имя")
surname = input('введите свою фамилию')
num = input("введите номерной знак")

if len(num) == 7 or 6 and num[1:5].isdigit() and num[0].isalpha() and num[5:].isalpha() and len(num[5:]) <= 2:
    num_type = "старый образец"

elif len(num) == 6 and num[:3].isdigit() and num[3].isalpha() and len(num[3:]) == 3:
    num_type = "новый образец"

else:
    print('ошибка')

exit()
print(f'{name} {surname}, номерной знак {num}, у вас {num_type}')


# 13-hw
# 14-hw

def apply_operation(numbers, operation):
    return [operation(num) for num in numbers]


numbers = [1, 2, 3, 4, 5]
squared = apply_operation(numbers, lambda x: x ** 2)
print(squared)
is_even = apply_operation(numbers, lambda x: x % 2 == 0)
print(is_even)

# 15-hw

words = ["python", "lambda", "map", "function", "programming"]

uppercase_words = list(map(lambda x: x.upper(), words))

print(uppercase_words)

word_lengths = list(map(lambda x: len(x), words))

print(word_lengths)


# 16-hw

class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.status = True

    def check_status(self):
        if self.status:
            self.status = True
            return "книга в наличии"
        else:
            self.status = True
            return "выдана"

    def give_book(self):
        if self.status:
            self.status = False
            return f"Книга {self.name} выдана."
        else:
            return f"Книга {self.name} уже выдана."

    def return_book(self):
        if self.status:
            self.status = True
            return f"вы вернули книгу {self.name}"


author_1 = Book("test", "test")
print(author_1.check_status())
print(author_1.give_book())
print(author_1.give_book())
print(author_1.check_status())
print(author_1.return_book())
print(author_1.check_status())


"""2"""


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.status = "В наличии"

    def issue(self):
        if self.status == "В наличии":
            self.status = "Выдана"
            print(f"Книга '{self.title}' выдана.")
        else:
            print(f"Книга '{self.title}' уже выдана.")

    def return_book(self):
        if self.status == "Выдана":
            self.status = "В наличии"
            print(f"Книга '{self.title}' возвращена.")
        else:
            print(f"Книга '{self.title}' не была выдана.")

    def check_status(self):
        print(f"Статус книги '{self.title}': {self.status}")


# Пример использования
book1 = Book("Война и мир", "Лев Толстой")
book1.check_status()
book1.issue()
book1.check_status()
book1.return_book()
book1.check_status()


# 17-hw

class Account:
    def __init__(self, account_type, balance=0):
        self.balance = balance
        self.account_type = account_type


@classmethod
def from_deposit(cls, deposit, account_type):
    return cls(account_type, balance=deposit)

    def deposit(self, amount):
        self.balance += amount


@classmethod
def change_account_type(cls, account, new):
    account.account_type = new
    account = Account.from_deposit(100, "Savings")
    account.deposit(50)
    print(account.balance)

    Account.change_account_type(account, "Current")
    print(account.account_type)


# 18-hw

from abc import ABC, abstractmethod


class Converter(ABC):
    @staticmethod
    @abstractmethod
    def convert(value):
        pass


class CelsiusToFahrenheitConverter(Converter):
    @staticmethod
    def convert(value):
        return value * 9 / 5 + 32


class KilometersToMilesConverter(Converter):
    @staticmethod
    def convert(value):
        return value * 0.621371


print(KilometersToMilesConverter.convert(10))
print(CelsiusToFahrenheitConverter.convert(25))


# 19-hw

class Student:
    total_students = 0

    def __init__(self):
        self.name = name
        Student.total_students += 2

    @staticmethod
    def det_total_results():
        return Student.total_students


s1 = Student('Test1')
s2 = Student('Tets2')

print((Student.get_total_students()))

# 20-hw

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.width * self.length


circle = Circle(radius=7)
rectangle = Rectangle(length=5, width=3)

print(circle.get_area())
print(rectangle.get_area())


#21-hw  перегрузка операторов

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

# 22-hw сравнение обьектов

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)

    def __eq__(self, other):
        return self.average() == other.average()

    def __lt__(self, other):
        return self.average() < other.average()

    def __gt__(self, other):
        return self.average() > other.average()

    def __repr__(self):
        return f"Student({self.name}, {self.grades})"


# 23-hw parsing

# 24-hw class Student

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def add_grade(self, grade):
        if 1 <= grade <= 5:
            self.grades.append(grade)
            print(f"Оценка {grade} добавлена для {self.name}.")
        else:
            print("Оценка должна быть в пределах от 1 до 5.")

    def calculate_average(self):
        if self.grades:
            average = sum(self.grades) / len(self.grades)
            return round(average, 2)
        return 0

    def display_info(self):
        print(f"Студент: {self.name}")
        print(f"Возраст: {self.age}")
        print(f"Оценки: {self.grades}")
        print(f"Средний балл: {self.calculate_average()}")


# Пример использования
student = Student("Боб", 20)
student.add_grade(4)
student.add_grade(5)
student.add_grade(3)
student.display_info()


# 25-hw Bankaccount

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Внесено {amount} на счет.")
        else:
            print("Сумма депозита должна быть положительной.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Снято {amount} с счета.")
        elif amount <= 0:
            print("Сумма снятия должна быть положительной.")
        else:
            print("Недостаточно средств на счете.")

    def get_balance(self):
        return self.balance


class BankAccountWithOwner(BankAccount):
    def __init__(self, owner, balance=0):
        super().__init__(balance)
        self.owner = owner

    def display_account_info(self):
        print(f"Владелец счета: {self.owner}")
        print(f"Баланс счета: {self.get_balance()}")


account = BankAccountWithOwner("Иван Иванов", 1000)
account.deposit(500)
account.withdraw(300)
account.display_account_info()
print(f"Текущий баланс: {account.get_balance()}")


# 26-hw Полиморфизм

class Product:
    def __init__(self, price):
        if price > 0:
            self._price = price
        else:
            print("Цена должна быть положительным числом.")
            self._price = 0

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            print("Цена должна быть положительным числом.")

    def get_description(self):
        return "Это продукт с базовой информацией."


class Clothes(Product):
    def __init__(self, price, size):
        super().__init__(price)
        if size in ['S', 'M', 'L', 'XL']:
            self._size = size
        else:
            print("Некорректный размер. Возможные значения: 'S', 'M', 'L', 'XL'.")
            self._size = 'M'

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value in ['S', 'M', 'L', 'XL']:
            self._size = value
        else:
            print("Недопустимый размер. Возможные значения: 'S', 'M', 'L', 'XL'.")

    def get_description(self):
        return f"Одежда, размер: {self.size}, цена: {self.price}"


class Electronics(Product):
    def __init__(self, price, warranty_years):
        super().__init__(price)
        if warranty_years >= 0:
            self._warranty_years = warranty_years
        else:
            print("Гарантия должна быть неотрицательным числом.")
            self._warranty_years = 0

    @property
    def warranty_years(self):
        return self._warranty_years

    @warranty_years.setter
    def warranty_years(self, value):
        if value >= 0:
            self._warranty_years = value
        else:
            print("Гарантия должна быть неотрицательным числом.")

    def get_description(self):
        return f"Электронное устройство, гарантия: {self.warranty_years} лет, цена: {self.price}"


class Food(Product):
    def __init__(self, price, expiration_date):
        super().__init__(price)
        if expiration_date >= "2025-01-01":
            self._expiration_date = expiration_date
        else:
            print("Срок годности не может быть в прошлом.")
            self._expiration_date = "2025-01-01"

    @property
    def expiration_date(self):
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, value):
        if value >= "2025-01-01":
            self._expiration_date = value
        else:
            print("Срок годности не может быть в прошлом.")

    def get_description(self):
        return f"Продукт питания, срок годности до: {self.expiration_date}, цена: {self.price}"


clothes = Clothes(1000, 'M')
electronics = Electronics(3000, 2)
food = Food(500, "2025-05-01")

print(clothes.get_description())
print(electronics.get_description())
print(food.get_description())

# 27-hw Инкапсуляция

class Student:
    def __init__(self):
        self.__grades = []

    @property
    def grades(self):
        return self.__grades

    def add_grade(self, grade):
        if 1 <= grade <= 5:
            self.__grades.append(grade)
        else:
            print("Некорректная оценка! Оценка должна быть числом от 1 до 5.")


student = Student()

student.add_grade(4)
student.add_grade(3.5)
student.add_grade(6)
student.add_grade('A')
print(student.grades)

# 28-hw Электронные устройства

from abc import ABC, abstractmethod


class ElectronicDevice(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class Smartphone(ElectronicDevice):
    def turn_on(self):
        print("Смартфон включён")

    def turn_off(self):
        print("Смартфон выключен")


class Laptop(ElectronicDevice):
    def turn_on(self):
        print("Ноутбук включён")

    def turn_off(self):
        print("Ноутбук выключен")


smartphone = Smartphone()
laptop = Laptop()


smartphone.turn_on()
smartphone.turn_off()

laptop.turn_on()
laptop.turn_off()

# 29-hw Перевозка грузов

from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def carry_load(self, weight):
        pass


class Truck(Transport):
    def carry_load(self, weight):
        return self._check_weight(weight, 1000)

    def _check_weight(self, weight, max_weight):
        return "Перегруз" if weight > max_weight else "Груз принят"


class Ship(Transport):
    def carry_load(self, weight):
        return self._check_weight(weight, 50000)

    def _check_weight(self, weight, max_weight):
        return "Перегруз" if weight > max_weight else "Груз принят"


def main():
    weight = float(input("Введите вес груза (в кг): "))

    truck = Truck()
    ship = Ship()

    print("Для грузовика:", truck.carry_load(weight))
    print("Для корабля:", ship.carry_load(weight))
main()

# 30-hw Простой класс с стр

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Имя: {self.name}, Возраст: {self.age}"

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

# 31-hw

class MathUtils:
    @staticmethod
    def calculate_area(**kwargs):
        if kwargs.get('radius') is not None:
            radius = kwargs.get('radius')
            return 3.14 * radius ** 2
        elif kwargs.get('length') is not None and kwargs.get('width') is not None:
            length = kwargs.get('length')
            width = kwargs.get('width')
            return length * width
        else:
            print("Необходимо указать radius для круга или length и width для прямоугольника")


print(MathUtils.calculate_area(radius=5))
print(MathUtils.calculate_area(length=4, width=3))