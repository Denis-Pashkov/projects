""" От простых классов к составным """

from tkinter.messagebox import NO
from typing import TypeVar
from random import choice, randrange
import re
from string import ascii_lowercase, digits
from random import randint
import random
import sys


class Car:
    pass


setattr(Car, 'model', "Тойота")
setattr(Car, 'color', "Розовый")
setattr(Car, 'number', "П111УУ77")

print(Car.__dict__['color'])


class Notes:
    uid = 1005435
    title = "Шутка"
    author = "И.С. Бах"
    pages = 2


print(getattr(Notes, 'author'))


class Dictionary:
    rus = "Питон"
    eng = "Python"


print(getattr(Dictionary, 'rus_word', False))


class TravelBlog:
    total_blogs = 0

    def __new__(cls, *args, **kwargs):
        cls.total_blogs += 1
        return super().__new__(cls, *args, **kwargs)


tb1 = TravelBlog()

tb1.name = 'Франция'
tb1.days = 6

tb2 = TravelBlog()

tb2.name = 'Италия'
tb2.days = 5

print(TravelBlog.total_blogs, tb1.name, tb1.days, tb2.name, tb2.days, sep='\n')


class Figure:
    type_fig = 'ellipse'
    color = 'red'


fig1 = Figure()

fig1.start_pt = (10, 5)
fig1.end_pt = (100, 20)
fig1.color = 'blue'

fig1 = Figure()

fig1.start_pt = (10, 5)
fig1.end_pt = (100, 20)
fig1.color = 'blue'

del fig1.color

print(' '.join([i for i in fig1.__dict__.keys()]))
print(*fig1.__dict__.keys())


class Person:
    name = 'Сергей Иванов'
    job = 'Программист'
    city = 'Москва'


p1 = Person()

print('job' in p1.__dict__.keys())

setattr()
getattr()
hasattr()
delattr()


class MediaPlayer:
    def open(self, file: str) -> None:
        self.filename = file

    def play(self) -> None:
        print(f'Воспроизведение {self.filename}')


media1 = MediaPlayer()
media2 = MediaPlayer()

media1.open('filemedia1')
media2.open('filemedia2')

media1.play()
media2.play()


class Graph:
    LIMIT_Y = [0, 10]

    @staticmethod
    def index_exist(lst, ind):
        try:
            lst[ind]
            return True
        except IndexError:
            return False

    def set_data(self, data: list) -> None:
        l_index = self.LIMIT_Y[0]
        r_index = self.LIMIT_Y[1] + 1

        if self.index_exist(data, l_index):
            if self.index_exist(data, r_index):
                self.data = data[l_index:r_index]
            else:
                self.data = data[l_index:]

    def draw(self) -> None:
        print(' '.join([str(i) for i in self.data]))


graph_1 = Graph()

graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()


class Graph:
    LIMIT_Y = [0, 10]

    def set_data(self, data: list) -> None:
        self.data = data

    def draw(self) -> None:
        print(' '.join(
            [str(i) for i in self.data if self.LIMIT_Y[0] <= i <= self.LIMIT_Y[1]]))


graph_1 = Graph()
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()


class Stepik:
    def next_task(self):
        return "Следующее задание"


my_st = Stepik()

my_st.next_task()
Stepik.next_task(my_st)


class StreamData:
    def create(self, fields, lst_values):
        if len(fields) == len(lst_values):
            try:
                for i in range(len(fields)):
                    self.__setattr__(fields[i], lst_values[i])
                return True
            except:
                return False
        else:
            return False


class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        # считывание списка строк из входного потока
        lst_in = list(map(str.strip, sys.stdin.readlines()))
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


sr = StreamReader()
data, result = sr.readlines()

sd = StreamData()
print(sd.create(list(sr.FIELDS), '10 Питон-основы-мастерства 512'))


# считывание списка строк из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    @staticmethod
    def index_exist(lst, ind):
        try:
            lst[ind]
            return True
        except IndexError:
            return False

    def insert(self, data) -> None:
        for i in data:
            self.lst_data.append(i)

    def select(self, a, b):
        l_index = a
        r_index = b + 1

        if self.index_exist(self.lst_data, l_index):

            if self.index_exist(self.lst_data, r_index):
                self.lst_data = self.lst_data[l_index:r_index]
            else:
                self.lst_data = self.lst_data[l_index:]
            lst_data1 = []
            for i in range(len(self.lst_data)):
                z = self.lst_data[i].split(' ')
                dic = {'id': '', 'name': '', 'old': '', 'salary': ''}
                for j, k in zip(z, dic):
                    dic[k] = j
                lst_data1.append(dic)
            return lst_data1

        def insert(self, data):
            for c in data:
                self.lst_data += [dict(zip(self.FIELDS, c.split()))]


class Translator:
    tr_lst = []

    def add(self, eng, rus) -> None:
        if [eng, rus] not in self.tr_lst:
            self.tr_lst.append([eng, rus])

    def remove(self, eng) -> None:
        self.tr_lst = [i for i in self.tr_lst if i[0] != eng]

    def translate(self, eng) -> list:
        return [i[1] for i in self.tr_lst if i[0] == eng]


tr = Translator()

tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")

tr.remove('car')

print(' '.join(tr.translate('go')))


class Point:
    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y
        self.color = color


points = []

for i in range(1, 2000, 2):
    points.append(Point(i, i))

points.pop(1)
points.insert(1, Point(3, 3, 'yellow'))


class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class_lst = [Line, Rect, Ellipse]
elements = []
for i in range(217):
    elements.append(random.choice(class_lst)(random.randint(0, 100), random.randint(0, 100), random.randint(0, 100),
                                             random.randint(0, 100)))

for i in elements:
    if isinstance(i, Line):
        i.sp = (0, 0)
        i.ep = (0, 0)


class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if (not isinstance(self.a, int) or not isinstance(self.b, int) or not isinstance(self.c, int)) or (
                self.a <= 0 or self.b <= 0 or self.c <= 0):
            return 1
        elif self.a + self.b <= self.c or self.b + self.c <= self.a or self.a + self.c <= self.b:
            return 2
        else:
            return 3


# a, b, c = map(int, input().split())

tr = TriangleChecker('3', 4, 5)

print(tr.is_triangle())


class Graph:
    def __init__(self, data: list, is_show=True):
        self.data = data
        self.is_show = is_show

    def set_data(self, data):
        self.data = data

    def show_table(self):
        if self.is_show:
            print(' '.join(map(str, self.data)))
        else:
            print('Отображение данных закрыто')

    def show_graph(self):
        if self.is_show:
            print(
                f'Графическое отображение данных: {" ".join(map(str, self.data))}')
        else:
            print('Отображение данных закрыто')

    def show_bar(self):
        if self.is_show:
            print(f'Столбчатая диаграмма: {" ".join(map(str, self.data))}')
        else:
            print('Отображение данных закрыто')

    def set_show(self, fl_show):
        self.is_show = fl_show


data_graph = list(map(int, input().split()))

gr = Graph(data_graph)

gr.show_bar()

gr.set_show(False)

gr.show_table()


class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name, cpu, mem_slots, total_mem_slots=4):
        self.name = name
        self.cpu = cpu
        self.mem_slots = mem_slots[:total_mem_slots]
        self.total_mem_slots = total_mem_slots

    def get_config(self) -> list:
        lst = [f'Материнская плата: {self.name}',
               f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
               f'Слотов памяти: {self.total_mem_slots}',
               f'Память: ']
        for i in self.mem_slots:
            lst[3] += f'{i.name} - {i.volume}; '
        lst[3] = lst[3][:-2]
        return lst


mb = MotherBoard('Name', CPU('Name', 1), [
                 Memory('Name1', 1), Memory('Name2', 2)])
mb.get_config()


class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        return [f'{i.name}: {i.price}' for i in self.goods]


class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price


cart = Cart()

cart.add(TV('TV1', 22000))
cart.add(TV('TV2', 25000))
cart.add(Table('Table', 23000))
cart.add(Notebook('Notebook1', 24000))
cart.add(Notebook('Notebook2', 25000))
cart.add(Cup('Cup', 21000))

print(cart.get_list())


class ListObject:
    def __init__(self, data: str, next_obj=None) -> None:
        self.data = data
        self.next_obj = next_obj

    def link(self, obj: object) -> None:
        self.next_obj = obj


lst_in = list(map(str.strip, sys.stdin.readlines()))

head_obj = ListObject(lst_in[0])

lst = [head_obj]
for i in lst_in[1:]:
    lst.append(ListObject(i))

for i in range(len(lst)):
    if 0 <= (i + 1) < len(lst):
        lst[i].link(lst[i + 1])


class Cell:
    def __init__(self, mine=False, fl_open=False, around_mines=0):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = fl_open


class GamePole:
    def __init__(self, N, M):
        self.pole = []
        self.n = N
        self.m = M

    def init(self):
        amount_mine = self.m

        for i in range(self.n):
            self.pole.append([])

        for i in range(self.n):
            for j in range(self.n):
                self.pole[i].append(Cell())

        while amount_mine > 0:
            choice_1 = randint(0, len(self.pole) - 1)
            choice_2 = randint(0, len(self.pole) - 1)

            if self.pole[choice_1][choice_2].mine:
                continue
            else:
                self.pole[choice_1][choice_2].mine = True
                amount_mine -= 1

    def around_mine_m(self, x, y):
        def cell_exist(x, y):
            try:
                self.pole[x][y]
                return True
            except IndexError:
                return False

        count = 0
        if cell_exist(x + 1, y - 1) and self.pole[x + 1][y - 1].mine:
            count += 1
        if cell_exist(x + 1, y) and self.pole[x + 1][y].mine:
            count += 1
        if cell_exist(x + 1, y + 1) and self.pole[x + 1][y + 1].mine:
            count += 1
        if cell_exist(x, y - 1) and self.pole[x][y - 1].mine:
            count += 1
        if cell_exist(x, y + 1) and self.pole[x][y + 1].mine:
            count += 1
        if cell_exist(x - 1, y - 1) and self.pole[x - 1][y - 1].mine:
            count += 1
        if cell_exist(x - 1, y) and self.pole[x - 1][y].mine:
            count += 1
        if cell_exist(x - 1, y + 1) and self.pole[x - 1][y + 1].mine:
            count += 1
        self.pole[x][y].around_mines = count

    def show(self):
        a = []
        for i in range(self.n):
            a.append([self.n] * self.n)

        for i in range(len(a)):
            for j in range(len(a)):
                if not self.pole[i][j].fl_open:
                    a[i][j] = '#'
                else:
                    if self.pole[i][j].mine:
                        pass
                    # boom
                    else:
                        self.around_mine_m(i, j)
                        a[i][j] = self.pole[i][j].around_mines
        print(*a, sep='\n')


pole_game = GamePole(10, 12)
pole_game.init()
for i in range(0, 10):
    for j in range(0, 10):
        pole_game.pole[i][j].fl_open = True
pole_game.show()


class Cell:
    def __init__(self, around_mines, mine, fl_open=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = fl_open


class GamePole:
    def __init__(self, N, M):
        self.pole = []
        self.n = N
        self.m = M
        self.init()

    def init(self):
        amount_mine = self.m
        arr = []
        for i in range(self.n):
            self.pole.append([])
            arr.append(['x'] * self.n)

        while amount_mine > 0:
            choice_1 = randint(0, len(self.pole) - 1)
            choice_2 = randint(0, len(self.pole) - 1)

            if arr[choice_1][choice_2] == 'mine':
                continue
            else:
                arr[choice_1][choice_2] = 'mine'
                amount_mine -= 1

        for i in range(self.n):
            for j in range(self.n):
                mine = False
                if arr[i][j] == 'mine':
                    mine = True
                self.pole[i].append(Cell(self.around_mine_m(i, j, arr), mine))

    def around_mine_m(self, x, y, arr):
        def cell_exist(x, y):
            try:
                arr[x][y]
                if x >= 0 and y >= 0:
                    return True
                else:
                    return False
            except:
                return False

        if not arr[x][y] == 'mine':
            count = 0
            if cell_exist(x + 1, y - 1) and arr[x + 1][y - 1] == 'mine':
                count += 1
            if cell_exist(x + 1, y) and arr[x + 1][y] == 'mine':
                count += 1
            if cell_exist(x + 1, y + 1) and arr[x + 1][y + 1] == 'mine':
                count += 1
            if cell_exist(x, y - 1) and arr[x][y - 1] == 'mine':
                count += 1
            if cell_exist(x, y + 1) and arr[x][y + 1] == 'mine':
                count += 1
            if cell_exist(x - 1, y - 1) and arr[x - 1][y - 1] == 'mine':
                count += 1
            if cell_exist(x - 1, y) and arr[x - 1][y] == 'mine':
                count += 1
            if cell_exist(x - 1, y + 1) and arr[x - 1][y + 1] == 'mine':
                count += 1
            return count

    def show(self):
        a = []
        for i in range(self.n):
            a.append([self.n] * self.n)

        for i in range(len(a)):
            for j in range(len(a)):
                if not self.pole[i][j].fl_open:
                    a[i][j] = '#'
                else:
                    if self.pole[i][j].mine:
                        a[i][j] = 9
                    # boom
                    else:
                        a[i][j] = self.pole[i][j].around_mines
        print(*a, sep='\n')


pole_game = GamePole(10, 12)
for i in range(0, 10):
    for j in range(0, 10):
        pole_game.pole[i][j].fl_open = True
pole_game.show()


class Cell:
    def __init__(self, around_mines, mine, fl_open=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = fl_open


class GamePole:
    def __init__(self, N, M):
        self.pole = []
        self.n = N
        self.m = M
        self.arr_show = []
        self.init()

    def init(self):
        amount_mine = self.m
        arr_mine = []
        for i in range(self.n):
            self.pole.append([])
            arr_mine.append(['x'] * self.n)
            self.arr_show.append([self.n] * self.n)

        while amount_mine > 0:
            choice_1 = randint(0, len(self.pole) - 1)
            choice_2 = randint(0, len(self.pole) - 1)

            if arr_mine[choice_1][choice_2] == 'mine':
                continue
            else:
                arr_mine[choice_1][choice_2] = 'mine'
                amount_mine -= 1

        for i in range(self.n):
            for j in range(self.n):
                mine = False
                if arr_mine[i][j] == 'mine':
                    mine = True
                self.pole[i].append(
                    Cell(self.around_mine_m(i, j, arr_mine), mine))

    @staticmethod
    def around_mine_m(x, y, arr_mine):
        def cell_exist(x, y):
            if not (x >= 0 and y >= 0):
                return False
            try:
                arr_mine[x][y]
                return True
            except IndexError:
                return False

        arr_coord = [[x + 1, y - 1], [x + 1, y], [x + 1, y + 1], [x, y - 1], [x, y + 1], [x - 1, y - 1], [x - 1, y],
                     [x - 1, y + 1]]

        if not arr_mine[x][y] == 'mine':
            count = 0
            for i in arr_coord:
                if cell_exist(i[0], i[1]) and arr_mine[i[0]][i[1]] == 'mine':
                    count += 1
            return count

    def show(self):
        for i in range(len(self.arr_show)):
            for j in range(len(self.arr_show)):
                if not self.pole[i][j].fl_open:
                    self.arr_show[i][j] = '#'
                else:
                    if self.pole[i][j].mine:
                        self.arr_show[i][j] = 9
                    else:
                        self.arr_show[i][j] = self.pole[i][j].around_mines
        print(*self.arr_show, sep='\n')


pole_game = GamePole(10, 12)
for i in range(0, 10):
    for j in range(0, 10):
        pole_game.pole[i][j].fl_open = True
pole_game.show()


class Cell:
    def __init__(self, around_mines, mine, fl_open=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = fl_open


class GamePole:
    def __init__(self, N, M):
        self.pole = []
        self.n = N
        self.m = M
        self.arr_show = []
        self.init()

    def init(self):
        amount_mine = self.m
        arr_mine = []
        for i in range(self.n):
            self.pole.append([])
            arr_mine.append([False] * self.n)
            self.arr_show.append([self.n] * self.n)

        while amount_mine > 0:
            choice_1 = randint(0, len(self.pole) - 1)
            choice_2 = randint(0, len(self.pole) - 1)

            if arr_mine[choice_1][choice_2]:
                continue
            else:
                arr_mine[choice_1][choice_2] = True
                amount_mine -= 1

        for i in range(self.n):
            for j in range(self.n):
                mine = False
                if arr_mine[i][j]:
                    mine = True
                self.pole[i].append(
                    Cell(self.around_mine_m(i, j, arr_mine), mine))

    @staticmethod
    def around_mine_m(x, y, arr_mine):
        def cell_exist(x, y):
            if not (x >= 0 and y >= 0):
                return False
            try:
                arr_mine[x][y]
                return True
            except IndexError:
                return False

        arr_coord = [[x + 1, y - 1], [x + 1, y], [x + 1, y + 1], [x, y - 1], [x, y + 1], [x - 1, y - 1], [x - 1, y],
                     [x - 1, y + 1]]

        if not arr_mine[x][y]:
            count = 0
            for i in arr_coord:
                if cell_exist(i[0], i[1]) and arr_mine[i[0]][i[1]]:
                    count += 1
            return count

    def show(self):
        for i in range(len(self.arr_show)):
            for j in range(len(self.arr_show)):
                if not self.pole[i][j].fl_open:
                    self.arr_show[i][j] = '#'
                else:
                    if self.pole[i][j].mine:
                        self.arr_show[i][j] = 9
                    else:
                        self.arr_show[i][j] = self.pole[i][j].around_mines
        print(*self.arr_show, sep='\n')


pole_game = GamePole(10, 12)
for i in range(0, 10):
    for j in range(0, 10):
        pole_game.pole[i][j].fl_open = True
pole_game.show()


class AbstractClass:
    def __new__(self):
        return 'Ошибка: нельзя создавать объекты абстрактного класса'


class SingletonFive:
    amount = 0
    five_obj = []

    def __new__(cls, *args, **kwargs):
        if cls.amount < 5:
            cls.amount += 1
            return super().__new__(cls)
        else:
            return cls.five_obj[-1]

    def __init__(self, name):
        self.name = name
        self.five_obj.append(self)


objs = [SingletonFive(str(n)) for n in range(10)]
print(*objs, sep='\n')

TYPE_OS = 1  # 1 - Windows; 2 - Linux


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


class Dialog:
    def __new__(cls, *args, **kwargs):
        if TYPE_OS == 1:
            a = super().__new__(DialogWindows)
        else:
            a = super().__new__(DialogLinux)
        a.__setattr__('name', args[0])
        return a


onj = Dialog('123')
print(type(onj.name))


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def clone(self):
        return Point(self.x, self.y)


pt = Point(1, 2)
pt_clone = pt.clone()


class Factory:
    @staticmethod
    def build_sequence():
        return []

    @staticmethod
    def build_number(string):
        return float(string)


class Loader:
    def parse_format(self, string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


ld = Loader()
res = ld.parse_format("4, 5, -6.5", Factory())

print(res)


class TextInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self, name, size=10):
        if self.check_name(name):
            self.name = name
        self.size = size

    def get_html(self):
        return f'<p class="login">{self.name}: <input type="text" size={self.size} />'

    @classmethod
    def check_name(cls, name):
        if name.strip(cls.CHARS_CORRECT) == '' and 3 <= len(name) <= 50:
            return True
        else:
            raise ValueError('некорректное имя поля')


class PasswordInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self, name, size=10):
        if self.check_name(name):
            self.name = name
        self.size = size

    def get_html(self):
        return f'<p class="password">{self.name}: <input type="text" size={self.size} />'

    @classmethod
    def check_name(cls, name):
        if name.strip(cls.CHARS_CORRECT) == '' and 3 <= len(name) <= 50:
            return True
        else:
            raise ValueError('некорректное имя поля')


class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()

CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
CHARS_CORRECT = CHARS + CHARS.upper() + digits

stre = 'qweasd'

print()

if stre.strip(CHARS_CORRECT) == '1':
    print(True)


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @staticmethod
    def check_card_number(number):
        return True if re.match(r'\d{4}-\d{4}-\d{4}-\d{4}', number) != None else False

    @staticmethod
    def check_name(name):
        return True if re.match(r'^[A-Z]+\s[A-Z]+$', name) != None else False


print(CardCheck.check_card_number("1234-5678-9012-0000"))


class Video:
    def create(self, name):
        self.name = name

    def play(self):
        print(f'воспроизведение видео {self.name}')


class YouTube:
    videos = []

    @classmethod
    def add_video(cls, video):
        cls.videos.append(video)

    @classmethod
    def play(cls, video_indx):
        cls.videos[video_indx].play()


v1 = Video()
v2 = Video()

v1.create('Python')
v2.create('Python ООП')

YouTube.add_video(v1)
YouTube.add_video(v2)

YouTube.play(0)
YouTube.play(1)


class AppStore:
    lst_app = []

    @classmethod
    def add_application(cls, app) -> None:
        cls.lst_app.append(id(app))

    @classmethod
    def remove_application(cls, app) -> None:
        cls.lst_app.pop(cls.lst_app.index(id(app)))

    @staticmethod
    def block_application(app) -> None:
        app.blocked = True

    @classmethod
    def total_apps(cls) -> int:
        return len(cls.lst_app)


class Application:
    def __init__(self, name, blocked=False) -> None:
        self.name = name
        self.blocked = blocked


class Viber:
    lst_msgs = {}
    lst_id = []
    total = 0

    @classmethod
    def add_message(cls, msg: object) -> None:
        cls.lst_msgs[id(msg)] = msg
        cls.lst_id.append(id(msg))
        cls.total += 1

    @classmethod
    def remove_message(cls, msg: object) -> None:
        del cls.lst_msgs[id(msg)]
        cls.lst_id.pop(cls.lst_id.index(id(msg)))
        cls.total -= 1

    @staticmethod
    def set_like(msg):
        msg.fl_like = not msg.fl_like

    @classmethod
    def show_last_message(cls, num):
        for i, j in zip(range(num), cls.lst_id):
            print(cls.lst_msgs[j].text)

    @classmethod
    def total_messages(cls):
        return cls.total


class Message:
    def __init__(self, text: str, fl_like=False) -> None:
        self.text = text
        self.fl_like = fl_like


num = 5
lst_id = [12312312, 12313212, 123123123, 1231231233]

for i, j in zip(range(num), lst_id):
    print(i, j)


class Server:
    ip_server = 0

    def __init__(self) -> None:
        self.buffer = []
        self.ip = Server.ip_server

    def __new__(cls, *args, **kwargs) -> object:
        cls.ip_server += 1
        return super().__new__(cls, *args, **kwargs)

    @classmethod
    def __del__(cls) -> None:
        cls.ip_server -= 1

    @staticmethod
    def send_data(data: object) -> None:
        Router.buffer.append(data)

    def get_data(self) -> list:
        return self.buffer

    def get_ip(self) -> int:
        return self.ip


class Router:
    buffer = []
    linked_servers_ip = {}
    linked_servers_a = []

    @classmethod
    def link(cls, server: object) -> None:
        cls.linked_servers_a.append(id(server))
        cls.linked_servers_ip[server.get_ip()] = server

    @classmethod
    def unlink(cls, server: object) -> None:
        del cls.linked_servers_ip[server.get_ip()]
        cls.linked_servers_a.pop(cls.linked_servers_a.index(server.get_ip()))

    @classmethod
    def send_data(cls) -> None:
        for i in cls.buffer:
            cls.linked_servers_ip[i.ip].buffer.append(i)
        cls.buffer = []


class Data:
    def __init__(self, data: str, ip: int) -> None:
        self.data = data
        self.ip = ip


router = Router()
sv_from = Server()
router.link(sv_from)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
router.send_data()
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()


class Clock:
    def __init__(self, time=0):
        self.__time = time

    def set_time(self, tm):
        if self.check_time(tm):
            self.__time = tm

    def get_time(self):
        return self.__time

    @staticmethod
    def check_time(tm):
        return True if (isinstance(tm, int) and 0 <= tm < 100000) else False


clock = Clock(4530)


class Money:
    def __init__(self, money: int) -> None:
        self.__money = money

    def set_money(self, money: int) -> None:
        if self.__check_money(money):
            self.__money = money

    def get_money(self) -> int:
        return self.__money

    def add_money(self, mn: object) -> None:
        self.__money += mn.get_money()

    @staticmethod
    def __check_money(money: int) -> bool:
        return True if (isinstance(money, int) and money >= 0) else False


mn_1 = Money(10)
mn_2 = Money(20)
mn_1.set_money(100)
mn_2.add_money(mn_1)
m1 = mn_1.get_money()  # 100
m2 = mn_2.get_money()  # 120


class Book:
    def __init__(self, author, title, price):
        self.__author = author
        self.__title = title
        self.__price = price

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_price(self, price):
        self.__price = price

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_price(self):
        return self.__price


class Line:
    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def set_coords(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_coords(self):
        return self.__x1, self.__y1, self.__x2, self.__y2

    def draw(self):
        print(self.__x1, self.__y1, self.__x2, self.__y2)


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_coords(self):
        return self.__x, self.__y


class Rectangle:
    def __init__(self, *args):
        if len(args) == 2:
            self.__sp = args[0]
            self.__ep = args[1]
        elif len(args) == 4:
            self.__sp = Point(args[0], args[1])
            self.__ep = Point(args[2], args[3])

    def set_coords(self, sp: object, ep: object):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return self.__sp, self.__ep

    def draw(self):
        print(
            f'Прямоугольник с координатами: ({self.__sp.__x}, {self.__sp.__y}) ({self.__ep.__x}, {self.__ep.__y})')


rect = Rectangle(0, 0, 20, 34)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if self.head is None:
            self.head = obj
            return

        last = self.head

        while last.get_next():
            last = last.get_next()
        last.set_next(obj)
        obj.set_prev(last)
        self.tail = obj

    def remove_obj(self):
        last = self.tail
        prev = last.get_prev()
        prev.set_next = None
        self.tail = prev

    def get_data(self):
        lst1 = []
        last = self.head
        lst1.append(last.get_data())
        while last.get_next():
            last = last.get_next()
            lst1.append(last.get_data())
        return lst1


class ObjList:
    def __init__(self, data):
        self.__next = None
        self.__prev = None
        self.__data = data

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data


ob = ObjList("данные 1")

lst = LinkedList()
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))
res = lst.get_data()
print(res)

print(LinkedList.self_dict, sep='\n')
print(lst.lst_obj[0])


class EmailValidator:
    CHARS_CORRECT = ascii_lowercase + ascii_lowercase.upper() + digits + '_'

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def check_email(cls, email):
        if not cls.__is_email_str(email):
            return False
        if len(email.strip('..')) != len(email):
            return False
        return True if (
            re.match(r'^(?!.*[\.][\.])[a-zA-Z0-9_]{1,100}@(?=.*[\.])[a-zA-Z0-9_.]{1,50}$', email)) else False

    @staticmethod
    def __is_email_str(email):
        return True if (isinstance(email, str)) else False

    @classmethod
    def get_random_email(cls):
        return ''.join([choice(cls.CHARS_CORRECT) for i in range(0, randrange(2, 100))]) + '@gmail.com'


print(EmailValidator.check_email("sc_lib@list.ru"))
print(EmailValidator.check_email("sc_lib@list_ru"))  # False

print(EmailValidator.get_random_email())


class Money:
    def __init__(self):
        self.__money = 0

    def set_money(self, value):
        self.__money = value

    def get_money(self):
        return self.__money

    money = property(get_money, set_money)


class Car:
    def __init__(self):
        self.__model = ''

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if self.validate_model(model):
            self.__model = model

    @staticmethod
    def validate_model(model):
        return True if (isinstance(model, str) and 2 <= len(model) <= 100) else False


class WindowDlg:
    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width
        self.__height = height

    def show(self):
        print(f'{self.__title}: {self.__width}, {self.__height}')

    def set_window(self, width, height):
        i = False
        if self.validate_length(width):
            self.__width = width
            i = True
        if self.validate_length(height):
            self.__height = height
            i = True
        if i:
            self.show()

    @staticmethod
    def validate_length(value):
        return True if (0 <= len(value) <= 10000) else False


class WindowDlg:
    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width
        self.__height = height

    def show(self):
        print(f'{self.__title}: {self.__width}, {self.__height}')

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if self.validate_length(value):
            self.__width = value
            self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if self.validate_length(value):
            self.__height = value
            self.show()

    @staticmethod
    def validate_length(value):
        return bool(isinstance(value, int) and 0 <= value <= 10000)


class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        if isinstance(value, StackObj) or value is None:
            self.__next = value


class Stack:
    def __init__(self):
        self.top = None

    def push(self, obj):
        if self.top is None:
            self.top = obj
        else:
            item = self.top
            while item.next:
                item = item.next
            item.next = obj

    def pop(self):
        if self.top:
            if not self.top.next:
                self.top = None
            else:
                item = self.top
                while item.next:
                    item = item.next
                    if not item.next.next:
                        item.next = None

    def get_data(self):
        lst = []
        if self.top:
            item = self.top
            lst.append(item.data)
            while item.next:
                item = item.next
                lst.append(item.data)
        return lst


st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.pop()
res = st.get_data()
print(res)


def pop(self):
    if self.top:
        if not self.top.next:
            self.top = None
        else:
            i = 0
            item = self.top
            while item.next:
                item = item.next
                if not item.next.next and i == 0:
                    item.next = None
                    i += 1


class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        if isinstance(value, StackObj) or value == None:
            self.__next = value

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value


class Stack:
    def __init__(self):
        self.top = None

    def push(self, obj):
        if self.top == None:
            self.top = obj
        else:
            current = self.top
            while current.next != None:
                current = current.next
            current.next = obj

    def pop(self):
        current = self.top
        while current.next.next is not None:
            current = current.next
        current.next = None

    def get_data(self):
        current = self.top
        e = []
        while current != None:
            e.append(current.data)
            current = current.next
        return e


st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.pop()


T = TypeVar('T', int, float)


IF = TypeVar('IF', int, float)


class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x: IF = 0, y: IF = 0) -> None:
        if self.validate_coord(x):
            self.__x = x
        else:
            self.__x = 0
        if self.validate_coord(y):
            self.__y = y
        else:
            self.__y = 0

    @property
    def x(self) -> IF:
        return self.__x

    @x.setter
    def x(self, value: IF) -> None:
        if self.validate_coord(value):
            self.__x = value

    @property
    def y(self) -> IF:
        return self.__y

    @y.setter
    def y(self, value: IF) -> None:
        if self.validate_coord(value):
            self.__y = value

    @classmethod
    def validate_coord(cls, value: IF) -> bool:
        return bool(isinstance(value, (int, float)) and cls.MIN_COORD <= value <= cls.MAX_COORD)

    @staticmethod
    def norm2(vector: 'RadiusVector2D') -> IF:
        return vector.x ** 2 + vector.y ** 2


class TreeObj:
    def __init__(self, indx, value=None):
        self.indx = indx
        self.value = value
        self.__left = None
        self.__right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, value):
        self.__left = value

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, value):
        self.__right = value


class DecisionTree:
    @classmethod
    def predict(cls, root: object, x: list) -> str:
        if x[0] == 1:
            x.pop(2)
        else:
            x.pop(1)

        for i in x:
            if i == 1:
                root = root.left
            else:
                root = root.right
        return root.value

    @classmethod
    def add_obj(cls, obj, node=None, left=True) -> None:
        if node:
            if left:
                node.left = obj
            else:
                node.right = obj
        return obj


root = DecisionTree.add_obj(TreeObj(0))
v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)

x = [1, 1, 0]
res = DecisionTree.predict(root, x)  # будет программистом
print(res)


class PathLines:
    def __init__(self, *args):
        if len(args) != 0:
            self.lines = [*args]
        else:
            self.lines = []

    def get_path(self):
        return self.lines

    def get_length(self):
        def set_values(self: object, i: int):
            return self.lines[i].x, self.lines[i].y

        c_sum = 0
        for i in range(len(self.lines)):
            if i == 0:
                x0, y0 = 0, 0
            x1, y1 = set_values(self, i)
            c_sum += sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)
            x0, y0 = set_values(self, i)

        return c_sum

    def add_line(self, line):
        self.lines.append(line)


class LineTo:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = PathLines(LineTo(10, 20), LineTo(10, 30))
dist = p.get_length()
print(dist)


class PhoneBook:
    phone_list = []

    @classmethod
    def add_phone(cls, phone):
        cls.phone_list.append(phone)

    @classmethod
    def remove_phone(cls, indx):
        cls.phone_list.pop(indx)

    @classmethod
    def get_phone_list(cls):
        return cls.phone_list


class PhoneNumber:
    def __init__(self, number: int, fio: str):
        self.number = number
        self.fio = fio


p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Иванов"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()


class FloatValue:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.validate_value(value):
            setattr(instance, self.name, value)
        else:
            raise TypeError(
                "Присваивать можно только вещественный тип данных.")

    @staticmethod
    def validate_value(value):
        return bool(isinstance(value, float))


class Cell:
    value = FloatValue()

    def __init__(self, value):
        self.value = value


class TableSheet:
    def __init__(self, N, M):
        self.cells = []
        numbers = [float(i) for i in range(1, 16)]
        for i in range(N):
            a = []
            for j in range(M):
                a.append(Cell(numbers[0]))
                numbers.pop(0)
            self.cells.append(a)


table = TableSheet(5, 3)

class StringValue:
    def __init__(self, validator: object) -> None:
        self.validator = validator

    def __set_name__(self, owner, name) -> None:
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.validator.validate(value):
            setattr(instance, self.name, value)


class ValidateString:
    def __init__(self, min_length=3, max_length=100):
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, string):
        return bool(isinstance(string, str) and self.min_length <= len(string) <= self.max_length)


class RegisterForm:
    login = StringValue(validator=ValidateString())
    password = StringValue(validator=ValidateString())
    email = StringValue(validator=ValidateString())

    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email

    def get_fields(self):
        return [self.login, self.password, self.email]

    def show(self):
        print('<form>', f'Логин: {self.login}', f'Пароль: {self.password}', f'Email: {self.email}', '</form>', sep='\n')
        

from typing import TypeVar, Any

IF = TypeVar('IF', int, float)


class StringValue:
    def __init__(self, min_length: int = 2, max_length: int = 50) -> None:
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, owner: object, name: str) -> None:
        self.name = '_' + name

    def __get__(self, instance: object, owner: object) -> Any:
        return getattr(instance, self.name)

    def __set__(self, instance: object, value: str) -> None:
        if isinstance(value, str) and self.min_length <= len(value) <= self.max_length:
            setattr(instance, self.name, value)


class PriceValue(StringValue):
    def __init__(self, max_value: IF = 1000):
        self.max_value = max_value

    def __set__(self, instance: object, value: IF) -> None:
        if isinstance(value, (int, float)) and 0 <= value <= self.max_value:
            setattr(instance, self.name, value)


class SuperShop:
    goods = []

    def __init__(self, name: str) -> None:
        self.name = name

    @classmethod
    def add_product(cls, product: object) -> None:
        cls.goods.append(product)

    @classmethod
    def remove_product(cls, product: object) -> None:
        cls.goods.pop(cls.goods.index(product))


class Product:
    name = StringValue()
    price = PriceValue()

    def __init__(self, name: str, price: IF) -> None:
        self.name = name
        self.price = price
        

class Bag:
    def __init__(self, max_weight: int) -> None:
        self.max_weight = max_weight
        self.__things = []

    @property
    def things(self) -> list:
        return self.__things

    def add_thing(self, thing: object) -> None:
        if self.get_total_weight() + thing.weight <= self.max_weight:
            self.__things.append(thing)

    def remove_thing(self, indx: int) -> None:
        self.__things.pop(indx)

    def get_total_weight(self) -> int:
        return sum([i.weight for i in self.__things])


class Thing:
    def __init__(self, name: str, weight: float) -> None:
        self.name = name
        self.weight = weight


bag = Bag(1000)
bag.add_thing(Thing("Книга по Python", 100))
bag.add_thing(Thing("Котелок", 500))
bag.add_thing(Thing("Спички", 20))
bag.add_thing(Thing("Бумага", 100))
w = bag.get_total_weight()
for t in bag.things:
    print(f"{t.name}: {t.weight}")
    

from typing import Any


class Descriptor:
    def __init__(self, name: str) -> None:
        self.name = name

    def __set_name__(self, owner: object, name: str) -> None:
        self.name = self.name

    def __get__(self, instance: object, owner: object) -> Any:
        return getattr(instance, self.name)

    def __set__(self, instance: object, value: str) -> None:
        setattr(instance, self.name, value)


class TVProgram:
    def __init__(self, name: str) -> None:
        self.name = name
        self.items = []

    def add_telecast(self, tl: object) -> None:
        self.items.append(tl)

    def remove_telecast(self, indx) -> None:
        self.items = [i for i in self.items if i.uid != indx]


class Telecast:
    # __id = Descriptor('uid')
    # __name = Descriptor('name')
    # __duration = Descriptor('duration')

    def __init__(self, id: int, name: str, duration: int) -> None:
        self.__id = id
        self.__name = name
        self.__duration = duration

    @property
    def uid(self) -> None:
        return self.__id

    @uid.setter
    def uid(self, value: int) -> None:
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value):
        self.__duration = value


pr = TVProgram("Первый канал")
pr.add_telecast(Telecast(1, "Доброе утро", 10000))
pr.add_telecast(Telecast(2, "Новости", 2000))
pr.add_telecast(Telecast(3, "Интервью с Балакиревым", 20))
for t in pr.items:
    print(f"{t.name}: {t.duration}")
    

class Book:
    dic = {"title": str, "author": str, "pages": int, "year": int}

    def __init__(self, title: str = '', author: str = '', pages: int = 0, year: int = 0) -> None:
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        if self.dic[key] != type(value):
            raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self, key, value)


book = Book('Python ООП', 'Сергей Балакирев', 123, 2022)


from typing import TypeVar, Any

IF = TypeVar('IF', int, float)


class Shop:
    def __init__(self, name: str) -> None:
        self.name = name
        self.goods = []

    def add_product(self, product: object) -> None:
        self.goods.append(product)

    def remove_product(self, product: object) -> None:
        self.goods.pop(self.goods.index(product))


class Product:
    id = 0

    def __init__(self, name: str, weight: IF, price: IF) -> None:
        self.id = self.id
        self.name = name
        self.weight = weight
        self.price = price

    def __new__(cls, *args, **kwargs) -> object:
        cls.id += 1
        return super().__new__(cls)

    def __setattr__(self, key: str, value: Any) -> None:
        if (key == 'id' and isinstance(value, int)) or (key == 'name' and isinstance(value, str)) or (
                key in ['weight', 'price'] and isinstance(value, (int, float)) and value >= 0):
            object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __delattr__(self, item: str) -> None:
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        object.__delattr__(self, item)