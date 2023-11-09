'''
class Point:

    def __new__(cls, *args, **kwargs):
        print('вызов __new__ для ' + str(cls))

    def __init__(self, x=0, y=0):
        print("вызов __init__ для " + str(self))
        self.x = x
        self.y = y

pt = Point(1, 2)
print(pt)
'''


'''
class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def __del__(self):
        print('__del__')
        DataBase.__instance = None

    def connect(self):
        print(f'соединение с БД: {self.user}, {self.password}, {self.port}')

    def close(self):
        print(f'Соединение разорвано')

    def read(self):
        print('Чтение данных')

    def write(self, data):
        print(f'Записываем данные {data}')


bd = DataBase('user', 'psw1', '8000')
bd2 = DataBase('user', 'psw1', '8000')
print(bd)
print(bd2)
'''

'''
class Test:
    def __repr__(self):
        return 'Object Test'

    def __str__(self):
        return 'Test String'

    def __bool__(self):
        return 2 < 6

t = Test()
print(str(t))
'''

'''
class Clock:
    __day = 86400

    def __init__(self, seconds:int):
        if not isinstance(seconds, int):
            raise TypeError('Нужно ввести целое число')
        self.seconds = seconds % self.__day

    def get_time(self):
        s = self.seconds % 60
        m = self.seconds // 60 % 60
        h = self.seconds // 3600 % 24
        return f'{h}:{m}:{s}'

    def __eq__(self, other):
        if isinstance(other, int):
            return self.seconds == other
        elif isinstance(other, Clock):
            return self.seconds == other.seconds
        else:
            raise TypeError('Нужно ввести целое число или объект класса Clock')

    def __lt__(self, other):
        if not isinstance(other(int, Clock)):
            raise TypeError('Type Error')
        sc = other if isinstance(other, int) else other.seconds
        return self.seconds <= sc

    def __ls__(self, other):
        if not isinstance(other(int, Clock)):
            raise TypeError('Type Error')
        sc = other if isinstance(other, int) else other.seconds
        return self.seconds <= sc

    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError("Не можем сложить")

        sc = other if isinstance(other, int) else other.seconds
        return  Clock(self.seconds + sc)

cl =Clock(8677)
cl2 = Clock(23423)
cl = cl + 20
print(cl.get_time())
cl = cl + cl2
print(cl.get_time())
'''

# class Passport:
#     def __init__(self, first_name, last_name, country, date_of_birth, numb_of_passport):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.date_of_birth = date_of_birth
#         self.country = country
#         self.numb_of_passport = numb_of_passport
#
#     def PrintInfo(self):
#         print(f'''
# Full name: {self.first_name} {self.last_name}
# Date of Birth: {self.date_of_birth}
# Country: {self.country}
# Passport: {self.numb_of_passport}
# ''')
#
#     def __repr__(self):
#         return f'name {self.first_name} {self.last_name}, Passport {self.numb_of_passport}'
#
# class ForeIgnPassport(Passport):
#
#     def __init__(self, first_name, last_name, country, date_of_birth, numb_of_passport, visa):
#         super().__init__(first_name, last_name, country, date_of_birth, numb_of_passport)
#         self.visa = visa
#
#     def PrintInfo(self):
#         super().PrintInfo()
#         print('Visa:', self.visa)
#
# MFC = []
# p = Passport('Ivan', 'Ivanov', 'Russia', '14.05.2005', '8221 457896')
# MFC.append(p)
# fp = ForeIgnPassport('Ivan', 'Ivanov', 'Russia', '14.05.2005', '8221 457896', 'China')
# MFC.append(fp)
# print(MFC)
# for item in MFC:
#     item.PrintInfo()
#
# my_str = 'sdfsdf'
# my_list = [1, 5, 6, 4, 3, 22, 77, 2]
#
# for char in my_str:
#     print(char)
#
# for number in my_list:
#     print(number)

'''
class Equipment:

    def __init__(self, name, make, year):
        self.name = name
        self.make = make
        self.year = year

    def action(self):
        return 'Не определено'

    def __str__(self):
        return f'{self.name}, {self.make}, {self.year}.'

    def __le__(self, other):
        if not isinstance(other, Equipment):
            raise TypeError
        return self.year <= other.year

class Printer(Equipment):
    def __init__(self, series, name, make, year):
        super().__init__(name, make, year)
        self.series = series

    def action(self):
        return 'Печатает'

    def __str__(self):
        return f'{self.series}, {self.name}, {self.make}, {self.year}'

def allItems(sklad):
    for item in sklad:
        print(item)

class Scaner(Equipment):

    def __init__(self, name, make, year):
        super().__init__(name, make, year)

    def action(self):
        return 'Сканирует'

class Xerox(Equipment):

    def __init__(self, name, make, year):
        super().__init__(name, make, year)

    def action(self):
        return 'Копирует и печатает на листочек'

def get_items(sklad):
    for item in sklad:
        if isinstance(item, Printer):
            print(item)

sklad = []
e = Equipment('Noname', 'X', 200)
sklad.append(e)
s = Printer('dfgdfgdf', 'fgd', 'dfgfd', 2545)
x = Xerox('sdfsdf', 'sdfsdf', 5000)

print(e)
print(s)
print(x)

print(sklad)
'''

# Класс "Битва"
'''
from random import randint

class Soldier:
    def __init__(self, name='No name', health=100):
        self.name = name
        self.health = health

    def set_name(self, name):
        self.name = name

    def make_kick(self, enemy):
        enemy.health -= 20
        if enemy.health < 0:
            enemy.health = 0
        self.health += 10
        print(self.name, 'бьёт', enemy.name)
        print(f'{enemy.name} = {enemy.health}')

    def __str__(self):
        return f'{self.name} (Health: {self.health})'

    def __lt__(self, other):
        return self.health < other.health

class Battle:
    def __init__(self, u1, u2):
        self.u1 = u1
        self.u2 = u2
        self.result = 'Сражения не было'

    def battle(self):

        while self.u1.health > 0 and self.u2.health > 0:
            n = randint(1,2)
            if n == 1:
                self.u1.make_kick(self.u2)
            else:
                self.u2.make_kick(self.u1)

        if self.u1.health > self.u2.health:
            self.result = f"{self.u1.name} Победил"
        elif self.u2.health > self.u1.health:
            self.result = f"{self.u2.name} Победил"

    def who_win(self):
        return self.result

first = Soldier('Mr. First', 140)
second = Soldier()
second.set_name('Mr. Second')
b = Battle(first, second)
b.battle()
print(b.who_win)
'''

'''
# Задача про карты
import time, random

class Card:
    NumsList = ['Джокер', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз']
    MastList = ['Пики', 'Крести', 'Бубни', 'Черви']

    def __init__(self, i, j):
        self.Mastb = self.MastList[i - 1]
        self.Num = self.NumsList[j - 1]

class DeckOfCards:
    def __init__(self):
        self.deck = [None] * 56
        k = 0
        for i in range(1, 4 + 1):
            for j in range(1, 14 + 1):
                self.deck[k] = Card(i, j)
                k += 1

    def shuffle(self):
        random.shuffle(self.deck)

    def get(self, i):
        if 0 <= i <= 55:
            answer = self.deck[i].Num
            answer += " "
            answer += self.deck[i].Mastb
        else:
            answer = "В колоде только 56 карт"
        return answer

d = DeckOfCards()
d.shuffle()
print('Выберите карту из колоды в 56 карт: ')
a = int(input())
if a <= 56:
    card = d.get(a - 1)
    print(f'Вы взяли карту: {card}', end='.\n')
else:
    print("В колоде только 56 карт")
'''


# Задача на класс Vector3D
'''
class Vector3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def display(self):
        print(f'{self.x}, {self.y}, {self.z}')

    def read(self):
        self.x = int(input('Введите x: '))
        self.y = int(input('Введите y: '))
        self.z = int(input('Введите z: '))

    def __add__(self, other):
        if isinstance(other, Vector3D):
            return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise ValueError("Можно добавить только один объект")

    def __sub__(self, other):
        if isinstance(other, Vector3D):
            return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            raise ValueError("Можно только вычесть другой объект Vector3D.")

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector3D(self.x * other, self.y * other, self.z * other)
        elif isinstance(other, Vector3D):
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            raise ValueError("Умножение не поддерживается для этого типа данных.")

    def __matmul__(self, other):
        if isinstance(other, Vector3D):
            return Vector3D(
                self.y * other.z - self.z * other.y,
                self.z * other.x - self.x * other.z,
                self.x * other.y - self.y * other.x,
            )
        else:
            raise ValueError("Можно вычислить векторное произведение только с другим объектом Vector3D.")

vec1 = Vector3D(4, 1, 2)
vec1.display()

vec2 = Vector3D()
vec2.read()

vec3 = Vector3D(1, 2, 3)

vec4 = vec1 + vec2
vec4.display()

a = vec4 * vec3
print(a)

vec4 = vec1 * 10
vec4.display()

vec4 = vec1 @ vec3
vec4.display()
'''

'''
# Задание Прямоугольный Треугольник
import math

class Triangle:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def increase_side(self, percent):
        self.side1 *= 1 + percent / 100
        self.side2 *= 1 + percent / 100

    def decrease_side(self,  percent):
        self.side1 *= 1 - percent / 100
        self.side2 *= 1 - percent / 100

    def radius_of_circumscribed_circle(self):
        return (self.side1 * self.side2) / (2 * math.sqrt(self.side1**2 + self.side2**2))

    def perimeter(self):
        return self.side1 + self.side2 + math.sqrt(self.side1**2 + self.side2**2)

    def angles(self):
        angle1 = math.degrees(math.asin(self.side1 / self.perimeter()))
        angle2 = math.degrees(math.asin(self.side2 / self.perimeter()))
        angle3 = 180 - angle1 - angle2
        return angle1, angle2, angle3

triangle = Triangle(5, 8)
print(f"Стороны: {triangle.side1} {triangle.side2}")

triangle.increase_side(20)
print(f"Стороны после увеличения на 20%: {triangle.side1} {triangle.side2}")

triangle.decrease_side(15)
print(f"Стороны после уменьшения на 15%: {triangle.side1} {triangle.side2}")

print(f'Радиус окружности: {triangle.radius_of_circumscribed_circle()}')
print(f'Периметр треугольника: {triangle.perimeter()}')
print(f'Значения углов: {triangle.angles()}')
'''

# Задача на класс Автобус
class Bus:
    def __init__(self):
        self.speed = 0
        self.capacity = 0
        self.maxSpeed = 100
        self.passengers = []
        self.seats = {}
        self.hasEmptySeats = False

    def boarding(self, passenger_names):
        for name in passenger_names:
            if len(self.passengers) < self.capacity:
                self.passengers.append(name)
                self.seats[name] = True
                print(f"{name} сел в автобус.")
            else:
                print(f"Нет свободных мест для {name}.")

    def getOff(self, passenger_names):
        for name in passenger_names:
            if name in self.passengers:
                self.passengers.remove(name)
                self.seats[name] = False
                print(f"{name} вышел из автобуса.")
            else:
                print(f"{name} его нет в автобусе.")

    def increaseSpeed(self, value):
        if self.speed + value <= self.maxSpeed:
            self.speed += value
            print(f"Скорость увеличилась до {self.speed} км/ч.")
        else:
            print("Автобус не может превышать максимальную скорость.")

    def decreaseSpeed(self, value):
        if self.speed - value >= 0:
            self.speed -= value
            print(f"Скорость снизилась до {self.speed} км/ч.")
        else:
            print(f"Скорость не может быть ниже нуля.")

    def __contains__(self, passenger_name):
        return passenger_name in self.passengers

    def __iadd__(self, passenger_name):
        self.boarding([passenger_name])
        return self

    def __isub__(self, passenger_name):
        self.getOff([passenger_name])
        return  self

bus = Bus()
bus.capacity = 30
bus.boarding(["Кирилл", "Максим", "Миша"])
bus.increaseSpeed(10)
bus += "Влад"
bus -= "Никита"
if "Кирилл" in bus:
    print("Кирилл сел в автобус")