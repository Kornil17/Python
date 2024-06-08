import json
from  dataclasses import dataclass
#
#
# class Test:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __repr__(self):
#         return f"Things: {self.__dict__}"
#
# a = Test(1, 3)
# print(a)
#
# @dataclass
# class Test:
#     '''class Test'''
#     x: int = 0
#     y: int = 1
# a = Test(5, 5)
# print(a)

# @dataclass
# class Test:
#     x: int = 0
#     y: int = 0
#
#     def __add__(self, other):
#         return self.x + other
#
# a = Test(1)
# a3 = Test(2)
# a2 = a + a3
# print(a2)


# class Test:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def gt(self):
#         print("class Test")
#         return self.x
#
# class Test2(Test):
#     def __init__(self, x, y, z, q):
#         super().__init__(x, y)
#         self.z = z
#         self.q = q
#
#     def gt(self):
#         print("class Test2")
#         return self.x
#
# a = Test(1, 2)
# b = Test2(3, 5, 4, 6)
# print(a.__dict__)
# print(b.__dict__)
# print(a.gt())
# print(b.gt())

#
# import sys
# print(sys.getsizeof(list(range(10000))))
# print(sys.getsizeof(range(10000)))
# print(sys.getsizeof(10000 * 'b'))
# print(sys.getsizeof(tuple(range(10000))))

# from contextlib import contextmanager
#
#
# @contextmanager
# def context_manager():
#     num = 2077
#     yield lambda: num
#     num += 1
#
#
# with context_manager() as manager:
#     print(manager())
# print(manager())
# import urllib.parse
# x = 'https://lk-test.egais.ru/lk-conductor/dashboard/conductor/info/infoWithPagination?filter=%5B%22isProcessed%22,%22=%22,%22true%22%5D&page=0&size=20'
# # print(urllib.parse.unquote('%5B%22isProcessed%22,%22=%22,%22true%22%5D&page=0&size=20'))
#
# print(urllib.parse.unquote('%5B%22isProcessed%22,%22=%22,%22false'))




# class Cat:
#     name = NonEmptyString('name')
#
#     def __init__(self, name):
#         self.name = name
#
#
# cat = Cat('Кемаль')
#
# cat.name
# cat.name = 'Роджер'
# del cat.name

# class PositiveNumber:
#     def __set_name__(self, cls, attr):
#         self._attr = attr
#
#     def __get__(self, obj, cls):
#         return obj.__dict__[self._attr]
#
#     def __set__(self, obj, value):
#         if type(value) in (int, float) and value > 0:
#             obj.__dict__[self._attr] = value
#         else:
#             raise ValueError('Некорректное значение')
#
# class Cat:
#     age = PositiveNumber()
#     name = PositiveNumber()
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# cat = Cat(2, 1)
# print(cat.__dict__)
# cat.name
# cat.name = 'Роджер'
# del cat.name
# cat.age
# cat.age = 'Роджер'
# del cat.age
import requests

# def send_card():
#     headers = {
#         'accept': 'text/plain'
#         # requests won't add a boundary if this header is set when you pass files=
#         # 'Content-Type': 'multipart/form-data',
#     }
#
#     files = {
#         'dueCard': (None, '0.LQAL.2P3KT.'),
#         'dueDocgroup': (None, '0.LLHZ.LLMU.LYY4.2RUOK.2RUOT.'),
#         'aIsnDelivery': (None, '1033658'),
#         'duePersonExe': (None, '0.LVIP.M3PQ.2T78C.'),
#         'aAnnotat': (None, 'test'),
#         'aNote': (None, 'test'),
#     }
#
#     try:
#         print(files)
#         card = requests.post('http://10.10.5.202:5005/api/AddRCWithFileAndSig', headers=headers, files=files)
#         print(f'get status code - {card.text}')
#     except Exception as ex:
#         print(ex)
#         raise ex
# if __name__ == "__main__":
#     send_card()
# import requests
#
#     headers = {
#         'accept': 'text/plain'
#     }
#
#     files = {
#         'dueCard': (None, '0.LQAL.2P3KT.'),
#         'dueDocgroup': (None, '0.LLHZ.LLMU.LYY4.2RUOK.2RUOT.'),
#         'aIsnDelivery': (None, '1033658'),
#         'duePersonExe': (None, '0.LVIP.M3PQ.2T78C.'),
#         'aAnnotat': (None, 'test'),
#         'aNote': (None, 'test'),
#     }
#
#     response = requests.post('http://10.10.5.202:5005/api/AddRCWithFileAndSig', headers=headers, files=files)
#     print(response.text)
#
# import requests
#
# headers = {
#     'accept': 'text/plain'
# }
#
# files = {
#     'dueCard': '0.LQAL.2P3KT.',
#     'dueDocgroup': '0.LLHZ.LLMU.LYY4.2RUOK.2RUOT.',
#     'aIsnDelivery': '1033658',
#     'duePersonExe': '0.LVIP.M3PQ.2T78C.',
#     'aAnnotat': 'test',
#     'aNote': 'test',
# }
#
# response = requests.post('http://10.10.5.202:5005/api/AddRCWithFileAndSig', headers=headers, files=files)
# print(response.text)

from collections import UserList


# class NumberList(UserList):
#     def __init__(self, it=[]):
#         if len(it) == 0:
#             super().__init__(it)
#         else:
#             super().__init__(self._validate(i) for i in it)
# 
#     @staticmethod
#     def _validate(value):
#         if isinstance(value, (int, float)):
#             return value
#         raise TypeError('Элементами экземпляра класса NumberList должны быть числа')
# 
#     def __add__(self, other):
#         if isinstance(other, list):
#             return NumberList(self.data + other)
#         elif isinstance(other, NumberList):
#             return NumberList(self.data + other.data)
#         return NotImplemented
# 
#     def __iadd__(self, other):
#         self.data += self.validate(other)
#         return self
#     def __setitem__(self, i, item):
#         if not isinstance(item, int):
#             raise TypeError('Элементами экземпляра класса NumberList должны быть числа')
#         self.data[i] = item
# 
# 
#     def insert(self, index, item):
#         self.data.insert(index, self._validate(item))
# 
#     def append(self, item):
#         self.data.append(self._validate(item))
# 
#     def extend(self, other):
#         self.data.extend(self._validate(other) for item in other)
# 
# n = NumberList([1, 2, 3])
# 
# try:
#     n[1] = '5'
# except TypeError as e:
#     print(e)
# from datetime import datetime
# from abc import ABC, abstractmethod
# class Date(ABC):
#     def __init__(self, year, month, day):
#         self.year = year
#         self.month = month
#         self.day = day
#     def iso_format(self):
#         return datetime(self.year, self.month, self.day).strftime("%Y-%m-%d")
#     @abstractmethod
#     def format(self):
#         pass
#
# class USADate(Date):
#     def format(self):
#         return datetime(self.year, self.month, self.day).strftime("%m-%d-%Y")
# class ItalianDate(Date):
#     def format(self):
#         return datetime(self.year, self.month, self.day).strftime("%d/%m/%Y")
#
#
# usadate = USADate(2023, 4, 6)
#
# print(usadate.format())
# print(usadate.iso_format())
#
# italiandate = ItalianDate(2023, 4, 6)
#
# print(italiandate.format())
# print(italiandate.iso_format())
# from abc import ABC, abstractmethod
# class Arithmetic(ABC):
#     def __init__(self, iterable=None):
#         if iterable == None:
#             self.iterable = []
#         else:
#             self.iterable = iterable
#     def add(self, n):
#         self.iterable.append(n)
#     @abstractmethod
#     def result(self):
#         pass
#     def clear(self):
#         self.iterable.clear()
#     def validate(self):
#         return len(self.iterable) > 0
#
# class MinStat(Arithmetic):
#     def result(self):
#         if self.validate():
#             return min(self.iterable)
#         else:
#             return None
# class MaxStat(Arithmetic):
#     def result(self):
#         if self.validate():
#             return max(self.iterable)
#         else:
#             return None
# class AverageStat(Arithmetic):
#     def result(self):
#         if self.validate():
#             return sum(self.iterable) / len(self.iterable)
#         else:
#             return None
#
# minstat = MinStat()
# maxstat = MaxStat()
# averagestat = AverageStat()
#
# print(minstat.result())
# print(maxstat.result())
# print(averagestat.result())

# class Queue:
#     def __init__(self, pairs=None):
#         if pairs == None:
#             self.queue = []
#         if isinstance(pairs, list):
#             self.queue = pairs
#         elif isinstance(pairs, dict):
#             self.queue = []
#             for key, value in pairs.items():
#                 self.queue.append((key, value))
#     def add(self, pairs):
#         for index, pair in enumerate(self.queue):
#             if pairs[0] == pair[0]:
#                 self.queue.pop(index)
#         self.queue.append((pairs[0], pairs[1]))
#     def pop(self):
#         if len(self.queue) == 0:
#             raise KeyError('Очередь пуста')
#         return self.queue.pop(0)
#     def __str__(self):
#         return f"Queue({self.queue})"
#     def __len__(self):
#         return len(self.queue)
# queue = Queue()
#
# try:
#     queue.pop()
# except KeyError as error:
#     print(error)
# from enum import Enum
# class Weekday(Enum):
#     MONDAY = 0
#     TUESDAY = 1
#     WEDNESDAY = 2
#     THURSDAY = 3
#     FRIDAY = 4
#     SATURDAY = 5
#     SUNDAY = 6
# 
# 
# class NextDate:
#     def __init__(self, today, weekday, after_today):
#         self.today = today
#         self.weekday = weekday
#         self.after_today = after_today
#     def date(self):
#         pass
#     def days_until(self):
#         pass
# first: int = 1
# with open('api_reception.logs', 'r') as f:
#     n = f.read()
#     print(f"Количество символов в логах - {len(n)}")
#
# with open('api_recept.logs', 'r') as f:
#     n = f.read()
#     print(f"Количество символов логов в файле - {len(n)}")
# with open('base64.txt', 'r') as f:
#     n = f.read()
#     print(f"Количество символов строки BASE64 в УТМ - {len(n)}")
# with open('base64_2.txt', 'r') as f:
#     n = f.read()
#     print(f"Количество символов строки BASE64 в файле - {len(n)}")

import functools
# class MaxCallsException(Exception):
#     pass
# def limited_calls(count):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             nonlocal count
#             if count <= 0:
#                 raise MaxCallsException('Превышено допустимое количество вызовов')
#             else:
#                 count -= 1
#                 return func(*args, **kwargs)
#
#         return wrapper
#     return decorator
# class limited_calls(MaxCallsException):
#     def __init__(self, n):
#         self.n = n
#     def __call__(self, func):
#         def wrapper(a, b):
#             if self.n <= 0:
#                 raise MaxCallsException('Превышено допустимое количество вызовов')
#             self.n -= 1
#             return func(a, b)
#         return wrapper
# @limited_calls(3)
# def add(a, b):
#     return a + b
# print(add(1, 2))
# print(add(3, 4))
# print(add(5, 6))
# print(add(1, 2))
import functools
# def takes_numbers(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         for i in args:
#             if not isinstance(i, (int|float)):
#                 raise TypeError('Аргументы должны принадлежать типам int или float')
#         for value in kwargs.values():
#             if not isinstance(value, (int|float)):
#                 raise TypeError('Аргументы должны принадлежать типам int или float')
#         return func(*args, **kwargs)
#     return wrapper

# class returns:
#     def __init__(self, n):
#         self.n = n
#     def __call__(self, func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             value = func(*args, **kwargs)
#             if self.n != type(value):
#                 raise TypeError
#             return value
#         return wrapper

# @decorator(add)
# def add(a, b):
#     return a + b
# decorator = returns(int)
# add = decorator(add)
#
# try:
#     print(add('1', '2'))
# except Exception as error:
#     print(type(error))
from json import dump
from pprint import pprint
# from uuid import uuid4
# request = dict({"id":"58e62bf3-3bf8-454a-8649-2ad2167165b7","serviceId":"lic-reestr","requestId":"7e86a82e-3120-43e3-9e69-8c8c72c7fade","requestType":"EPGU","xsltId":10,"responseId":"d686e07b-51b9-49f7-afca-d2f0221ce712","messageId":"ebcdc2bd-5704-11ee-83a2-2ec0795265b9","requestContent":{"epgu":{"orderID":"74457799","department":"100000012571","serviceCode":"60011489","targetCode":"60011489-1","statementDate":"2023-09-19"},"applicant":{"ul":{"fullName":"Общество с ограниченной ответственностью \"СИМЭНЕРГО\"","shortName":"ООО \"СИМЭНЕРГО\"","lastName":"","firstName":"","patronymic":"","ogrn":"","inn":"7714698320","kpp":""},"address":"","email":"test@gmail.com","phone":""},"agent":{"lastName":"","FirstName":"","Patronymic":"","documentId":{"serial":"","number":"","issuerName":"","issuerCode":"","issueDate":""},"dateOfBirth":"","email":"","phone":""},"extract":{"licenseNumber":"34РПА0006984","issueDate":""}},"requestTimestamp":"2023-09-19T18:55:32.269+0300","updateTimestamp":"2023-09-19T18:55:32.520+0300","kafkaPartition":0,"kafkaOffset":0,"route":"IN","attachmentPath":"/mnt/leveler/storage/2023-09-19/ebcdc2bd-5704-11ee-83a2-2ec0795265b9/Application.zip","state":"OUTGOING","archivedStatus":"true","queuedStatus":"true"})
# request['id'] = str(uuid4())
# request['requestId'] = str(uuid4())
# request['responseId'] = str(uuid4())
# request['messageId'] = str(uuid4())
# # pprint(request)
# print(request)
# class Vector:
#     def __init__(self, *args):
#         self.coords = args
#     def __str__(self):
#         return f"{self.coords}"
#     def __eq__(self, other):
#         if isinstance(other, Vector):
#             return self.coords == other.coords
#         elif not isinstance(other, Vector):
#             return self.coords == other
#         return NotImplemented
#
#     def __lt__(self, other):
#         if isinstance(other, Vector):
#             return self.coords < other.coords
#         elif not isinstance(other, Vector):
#             return self.coords < other
#         return NotImplemented
#     def __add__(self, other):
#         if len(self.coords) !=  len(other):
#             return 'Векторы должны иметь равную длину'
#         elif len(self.coords) ==  len(other) and isinstance(other, Vector):
#             summ = tuple()
#             for i in range(len(self.coords)):
#                 summ += (self.coords[i] + other.coords[i],)
#             return Vector(summ)
#         elif len(self.coords) ==  len(other) and not isinstance(other, Vector):
#             summ = tuple()
#             for i in range(len(self.coords)):
#                 summ += (self.coords[i] + other[i],)
#             return Vector(summ)
#         return NotImplemented
#
#     def __radd__(self, other):
#         return self.__add__(other)
#     def __sub__(self, other):
#         if len(self.coords) != len(other):
#             return 'Векторы должны иметь равную длину'
#         elif len(self.coords) == len(other) and isinstance(other, Vector):
#             summ = tuple()
#             for i in range(len(self.coords)):
#                 summ += (self.coords[i] - other.coords[i],)
#             return Vector(summ)
#         elif len(self.coords) == len(other) and not isinstance(other, Vector):
#             summ = tuple()
#             for i in range(len(self.coords)):
#                 summ += (self.coords[i] - other[i],)
#             return Vector(summ)
#         return NotImplemented
#     def __rsub__(self, other):
#         return self.__sub__(other)
#     def __mul__(self, other):
#         if len(self.coords) != len(other):
#             return 'Векторы должны иметь равную длину'
#         elif len(self.coords) == len(other) and isinstance(other, Vector):
#             return Vector(self.coords * other.coords)
#         elif len(self.coords) == len(other) and not isinstance(other, Vector):
#             return Vector(self.coords * other)
#         return NotImplemented
#     def __rmul__(self, other):
#         return self.__mul__(other)
#     def __len__(self):
#         return len(self.coords)
#
# vector1 = Vector(1, 2, 3)
# vector2 = Vector(3, 4, 5)
# vector3 = Vector(5, 6, 7, 8)
#
# print(vector1 + vector2)
# print(vector1 - vector2)
# print(vector1 * vector2)
# print(vector1 == Vector(1, 2, 3))
# print(vector1 == Vector(4, 5, 6))
# print(vector1 != vector2)
# vector5 = vector1 + vector2
# vector4 = vector1 - vector2
# print(type(vector5))
# print(type(vector4))

# import re
# txt = 'python.ru'
# print(re.findall(r'\b[a-zA-Z]+\.[a-zA-Z]+\b', txt))
# import re
# class DomainException:
#     exception = 'Недопустимый домен, url или email'
#
# class Domain:
#     def __init__(self, name, flag=0):
#         if flag == 0:
#             if self.validate_name(name):
#                 self.domain = name
#             else:
#                 print(DomainException.exception)
#         elif flag == 1:
#             if self.validate_url_name(name):
#                 self.domain = name
#             else:
#                 print(DomainException.exception)
#         elif flag == 2:
#             if self.validate_email_name(name):
#                 self.domain = name
#             else:
#                 print(DomainException.exception)
#
#     @classmethod
#     def from_url(cls, name):
#         return cls(name, 1)
#     @classmethod
#     def from_email(cls, name):
#         return cls(name, 2)
#     @staticmethod
#     def validate_name(n):
#         return len(re.findall(r'\b[a-zA-Z]+\.[a-zA-Z]+\b', n)) == 1
#
#     @staticmethod
#     def validate_url_name(n):
#         return len(re.findall(r'\b[a-z]{,5}\b', n)) != 0
#     @staticmethod
#     def validate_email_name(n):
#         return True

# t = Domain('python.ru')
# u = Domain('rere')
# k = Domain.from_url('http')
# # d = Domain.from_email('l.c')
# print(k.domain)
# print(t.domain, k.domain, d.domain, sep='\n')
# from math import sqrt
# from functools import total_ordering
# @total_ordering
# class Vector:
#     def __init__(self, *args):
#         self.coords = args
#     def __str__(self):
#         for cord in self.coords:
#             return f"{cord}"
#     def __eq__(self, other):
#         if isinstance(other, Vector):
#             if not self.length(self.coords, other.coords):
#                 raise ValueError ('Векторы должны иметь равную длину')
#             return self.coords == other.coords
#         elif not isinstance(other, Vector):
#             if not self.length(self.coords, other):
#                 raise ValueError ('Векторы должны иметь равную длину')
#             return self.coords == other
#         return NotImplemented
#
#     def __lt__(self, other):
#         if isinstance(other, Vector):
#             if not self.length(self.coords, other.coords):
#                 raise ValueError ('Векторы должны иметь равную длину')
#             return self.coords < other.coords
#         elif not isinstance(other, Vector):
#             if not self.length(self.coords, other):
#                 raise ValueError ('Векторы должны иметь равную длину')
#             return self.coords < other
#         return NotImplemented
#     def __add__(self, other):
#         if isinstance(other, Vector):
#             if not self.length(self.coords, other.coords):
#                 raise ValueError ('Векторы должны иметь равную длину')
#             # return Vector(tuple((map(sum, zip(self.coords, other.coords)))))
#             return Vector(self.result(self.coords, other.coords, '+'))
#         elif not isinstance(other, Vector):
#             if not self.length(self.coords, other):
#                 raise ValueError ('Векторы должны иметь равную длину')
#             # return Vector(tuple((map(sum, zip(self.coords, other)))))
#             return Vector(self.result(self.coords, other, '+'))
#         return NotImplemented
#
#     def __radd__(self, other):
#         return self.__add__(other)
#     def __sub__(self, other):
#         if isinstance(other, Vector):
#             if not self.length(self.coords, other.coords):
#                 raise ValueError ('Векторы должны иметь равную длину')
#             # return Vector(tuple((map(sum, zip(self.coords, other.coords)))))
#             return Vector(self.result(self.coords, other.coords, '-'))
#         elif not isinstance(other, Vector):
#             if not self.length(self.coords, other):
#                 raise ValueError ('Векторы должны иметь равную длину')
#             # return Vector(tuple((map(sum, zip(self.coords, other)))))
#             return Vector(self.result(self.coords, other, '-'))
#         return NotImplemented
#     def __rsub__(self, other):
#         return self.__sub__(other)
#     def __mul__(self, other):
#         if isinstance(other, Vector):
#             if not self.length(self.coords, other.coords):
#                 raise ValueError ('Векторы должны иметь равную длину')
#             # return Vector(tuple((map(sum, zip(self.coords, other.coords)))))
#             return sum(self.result(self.coords, other.coords, '*'))
#         elif not isinstance(other, Vector):
#             if not self.length(self.coords, other):
#                 raise ValueError ('Векторы должны иметь равную длину')
#             # return Vector(tuple((map(sum, zip(self.coords, other)))))
#             return (self.result(self.coords, other, '*'))
#         return NotImplemented
#     def __rmul__(self, other):
#         return self.__mul__(other)
#     def norm(self):
#         result = 0
#         for coord in self.coords:
#             result += coord**2
#         return sqrt(result)
#     @staticmethod
#     def length(a, b):
#         return len(a) == len(b)
#     @staticmethod
#     def result(a, b, key):
#         result = list()
#         for first, second in zip(a, b):
#             if key == '+':
#                 result.append(first + second)
#             elif key == '-':
#                 result.append(first - second)
#             elif key == '*':
#                 result.append(first * second)
#         return tuple(result)
#
# vector1 = Vector(1, 2, 3)
# vector2 = Vector(5, 6, 7, 8)
#
# try:
#     print(vector1 == vector2)
# except ValueError as e:
#     print(e)

# import urllib.parse as p
# print(p.quote(' '))
# from datetime import date, time, datetime
#
# dates = [date(1793, 8, 23), date(1410, 3, 11), date(804, 11, 12), date(632, 6, 4),
#          date(295, 1, 23), date(327, 8, 24), date(167, 4, 16), date(229, 1, 24),
#          date(1239, 2, 5), date(1957, 7, 14), date(197, 8, 24), date(479, 9, 6)]
#
# times = [time(7, 33, 27), time(21, 2, 10), time(17, 20, 47), time(20, 8, 59),
#          time(12, 42, 56), time(15, 9, 57), time(17, 47, 9), time(9, 40, 2),
#          time(11, 47, 1), time(17, 27, 10), time(17, 55, 40), time(9, 14, 9)]
# # print(*sorted([datetime.combine(x, y) for x in dates for y in times], key=lambda x: x.second), sep='\n')
# datetimes = [datetime.combine(date, time) for date, time in zip(dates, times)]
# print(*sorted(datetimes, key=lambda x: x.second), sep='\n')


from json import loads, dumps

# print(dumps('{"id":"9fdaa271-11cd-4b4f-ac98-c5832b0a1226","serviceId":"brewers-service","requestId":"4b823d83-3d00-41c9-85b3-044c29f928d9","requestType":"EPGU","xsltId":5,"responseId":"910a12dc-7259-4890-8b27-ec7cf19de4cc","messageId":"0fce9894-8e8b-11ee-a1e1-7ac46fb75245","requestContent":{"epgu":{"orderID":"3605242047","department":"10000001087","serviceCode":"60013397","targetCode":"60013397-2","statementDate":"2023-11-29"},"applicant":{"ul":{"fullName":"АКЦИОНЕРНОЕ ОБЩЕСТВО \"ФОРШТАДТСКАЯ ПИВОВАРНЯ\"","shortName":"АО \"ФОРШТАДТСКАЯ ПИВОВАРНЯ\"","lastName":"Сербина","firstName":"Мариана","patronymic":"Валентиновна","ogrn":"1185476101909","inn":"5404083315","kpp":"540401001"},"address":"630108, обл. Новосибирская, р-н. Татарский, г. Татарск, п. Станционный, д. 16/1, офис. 307","email":"serbina-61@mail.ru","phone":"+7(983)5463277"},"changesInRegister":{"subdivisions":[{"productProductionCapacities":[{"kindOfProduct":"пиво","productionCapacity":"711077"},{"kindOfProduct":"пивные напитки","productionCapacity":"7219"},{"kindOfProduct":"сидр","productionCapacity":"3609"}],"address":"656038, Алтайский край, Барнаул г, Промышленная ул, дом № 106","newAddress":"","kpp":"222545001","newKpp":"","certNumbers":"","cadastralNumbers":[]}],"aggregateProductionCapacities":[],"orgInfo":{"fullName":"","kpp":"","address":"","email":""},"duty":{"payment":{"number":"20419","date":"2023-11-29"}}},"appliedDocuments":[{"name":"Схема 2.pdf","businessName":"Схема оснащения основного технологического оборудования автоматическими средствами измерения и учёта объёма готовой продукци","type":"application/pdf","mnemonic":"c46.FileUploadComponent.skhema.3605242047"},{"name":"Схема 3.pdf","businessName":"Схема оснащения основного технологического оборудования автоматическими средствами измерения и учёта объёма готовой продукци","type":"application/pdf","mnemonic":"c46.FileUploadComponent.skhema.3605242047"},{"name":"Схема 1.pdf","businessName":"Схема оснащения основного технологического оборудования автоматическими средствами измерения и учёта объёма готовой продукци","type":"application/pdf","mnemonic":"c46.FileUploadComponent.skhema.3605242047"},{"name":"doc06442320231129073453-2-6.pdf","businessName":"Расчёт производственной мощности основного технологического оборудования","type":"application/pdf","mnemonic":"c44.FileUploadComponent.raschet.3605242047"},{"name":"doc06442320231129073453-1.pdf","businessName":"Документ, подтверждающий необходимость внесения изменений в реестр","type":"application/pdf","mnemonic":"c49.FileUploadComponent.izmeneniya.3605242048"}]},"requestTimestamp":"2023-11-29T07:44:57.018+0300","updateTimestamp":"2023-11-29T07:44:59.048+0300","kafkaPartition":0,"kafkaOffset":0,"route":"IN","attachmentPath":"/mnt/nfs2/leveler/storage/2023-11-29/0fce9894-8e8b-11ee-a1e1-7ac46fb75245/Application.zip","state":"OUTGOING","queuedStatus":true,"archivedStatus":true}',  ensure_ascii=False))

# d = {chr(i):i-97 for i in range(97, 97+26)}
# line = '🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩'
# str = 'I love Python =)'
# m = str.upper().maketrans(d)
# r = line.translate(m)
# print(r)

from collections import Counter
from collections import ChainMap

# from base64 import b64decode, b64encode
# original_string = '(Какой-нибудь ещё)'
# encoded_bytes = b64encode(original_string.encode('utf-8'))
# encoded_string = encoded_bytes.decode('utf-8')
# dec = b64decode(encoded_string).decode('utf8')
# print(encoded_string, dec, sep='\n')
from collections import defaultdict

from typing import List, Union, Dict, Any, Callable, Hashable, Iterable, Iterator
from collections import deque
import functools
import sys
from time import perf_counter


def timer(func: callable)->Callable:
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        print(f"Time: {((end - start) / 1) * 100}", f"Memory: {sys.getsizeof(result)}",sep='\n')
        return result
    return wrapper

from random import choice
from dataclasses import dataclass
from datetime import date
from typing import Generator
from itertools import groupby, product
from enum import Enum
import string
from functools import singledispatchmethod

class BasicPlan:
        can_stream = True
        can_download = True
        has_SD = True
        has_HD = False
        has_UHD = False
        num_of_devices = 1
        price = '8.99$'

class SilverPlan(BasicPlan):
        has_HD = True
        num_of_devices = 2
        price = '12.99$'

class GoldPlan(BasicPlan):
        has_HD = True
        has_UHD = True
        num_of_devices = 4
        price = '15.99$'












