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
        Student.total_students += 1

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
