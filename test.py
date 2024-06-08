import bisect
import datetime
import json
import queue
import random
import threading
import time
from asyncio import AbstractEventLoop
from dataclasses import dataclass

import numpy as np
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


def timer(func: callable) -> Callable:
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        print(f"Time: {((end - start) / 1) * 100}", f"Memory: {sys.getsizeof(result)}", sep='\n')
        return result

    return wrapper


from random import choice
from dataclasses import dataclass
from datetime import date
from typing import Generator
from itertools import groupby, product
from enum import Enum, IntEnum, unique, auto
import string
from functools import singledispatchmethod

import re
from abc import ABC
from functools import total_ordering
from dataclasses import dataclass, field
from rstr import xeger

# class Regex:
#     """
#     class for get string by regex
#     """
#     _pattern = r'([а-я]\s)\.([а-я]\s)\.([а-я])'
#     @classmethod
#     def get_result(cls, data: str) -> None:
#         result = re.sub(cls._pattern, "ФИО", data)
#         print(result)
#
# Regex.get_result(input())

from copy import deepcopy

from copy import deepcopy
from pandas import Series, Index, DataFrame
# class Regex:
#     def __init__(self) -> None:
#         self.pattern = r'(\d+):([a-z\d]+):([a-z\d]+)'
#         self.result = []
#     def __call__(self, data: list[str]) -> list[tuple[str, ...]]:
#         for i in data:
#             if re.findall(self.pattern, i, re.I):
#                 self.result.append(re.findall(self.pattern, i, re.I))
#         return self.result
# Regex(sys.stdin)

from copy import deepcopy

from copy import deepcopy

from copy import deepcopy

from random import randint
# from random import choice

from collections import defaultdict


def func(a, b, c) -> dict[int]:
    """
    test function
    :param a:
    :param b:
    :param c:
    :return:
    """


# from pandas import read_excel
#
# dt = read_excel('~/AllCombinations.xlsx')
# dt = dt.set_index(dt.columns[0])
# n = dt.apply(lambda row: row.to_dict(), axis=1).tolist()
# for i in n:
#     a = i['comment'].split()
#     print(a[0], a[1], a[2])
#     break

# n = {'test':1, '2':45}
# m = list(n.items())
# print(dict(m))

import argparse
#
# values = argparse.ArgumentParser(description='Пример парсинга значений из консоли')
# values.add_argument('--test', help='test value', default='123')
# args = values.parse_args()
# print(args.test)
from abc import ABC, abstractmethod
# class ArgsParser(ABC):
#     @abstractmethod
#     def add_arguments(self):
#         pass
#     @abstractmethod
#     def parse_arguments(self):
#         pass
#
# class Parser(ArgsParser):
#     def __init__(self, **kwargs):
#         self._parametrs = kwargs
#         self.args = argparse.ArgumentParser(description='get values from console')
#     def add_arguments(self):
#         for key, value in self._parametrs.items():
#             self.args.add_argument(key, help=f'get values by {key}', default=value)
#
#     def parse_arguments(self):
#         parser = self.args.parse_args()
#         for key in self._parametrs.keys():
#             print(parser.__dict__[key[2:]])
#
#
# parser = Parser(**{'--test':123, '--main':'python'})
# parser.add_arguments()
# parser.parse_arguments()

import pandas as pd
#
# def color_negative(val):
#     color = 'white'
#     if isinstance(val, int):
#         color = 'red' if val < 0 else 'black'
#         return f"color: {color}"
#     else:
#         return "background-color: blue"
#
# df = pd.read_excel('~/AllCombinations.xlsx')
# print(df.to_string())
#
# styled_df = df.style.applymap(color_negative)
# styled_df.to_excel('~/Downloads/output.xlsx', index=False)

# import sys, os
#
# while True:
#     sys.stdout.write('Введите два числа и операцию по аналогии с калькулятором (+, -, *, /): ' + os.linesep)
#     user_input = sys.stdin.readline().strip()
#
#     if user_input == 'exit':
#         break
#
#     try:
#         result = eval(user_input)
#         sys.stdout.write(f"Результат операции: {result}" + os.linesep)
#     except Exception as e:
#         sys.stdout.write(f"Ошибка: {e}" + os.linesep)

# TODO test todo task
# import pandas as pd
# from bs4 import BeautifulSoup
# text = """<p data-rtc-uid="19d62a05-9a7b-4756-a984-f4c579a4cc04"><br data-rtc-uid="86ebc166-799e-40f5-997b-4c6774924f21"></p><table class="relative-table mce-item-table" style="border-collapse: collapse; width: 845px; height: unset;" data-rtc-uid="8993c052-35a0-4fcd-b162-8f2c19a48819" data-widthmode="wide" data-lastwidth="845px" id="mce_1"><colgroup data-rtc-uid="93565d29-183a-457d-947a-4af3b4079c6f"><col data-rtc-uid="58f04697-3166-4e8e-837d-91103545cf4c" style="width: 485px;"><col data-rtc-uid="e134c6ec-0619-4100-a1fa-14d3d6445738" style="width: 129px;"><col data-rtc-uid="27a842a8-4fef-4568-bc97-465467bb08bf" style="width: 167px;"><col data-rtc-uid="a3735680-91c2-4386-8a4f-7f0d6597df17" style="width: 62px;"></colgroup><tbody data-rtc-uid="5f20fd1c-543a-4db0-a1ab-3be018d02396"><tr data-rtc-uid="e0f0fd28-9321-4b37-8d13-7d82c62c8a19" style="height: 52.7917px;"><td data-rtc-uid="d19e583f-23cd-470d-8019-5d56d65285f4" style="height: 52.7917px;">Transactions</td><td data-rtc-uid="7007d4f3-d717-4dce-9171-f1a6672ff64b" style="height: 52.7917px;">% в профиле</td><td data-rtc-uid="249909d2-3bc8-4d9e-bbd0-49152c2b0448" style="height: 52.7917px;">Интенсивность(o/ч)</td><td data-rtc-uid="5db08dc4-3fcf-46e9-87cb-a0265c2ed817" style="height: 52.7917px;">SLA</td></tr><tr data-rtc-uid="b04afb8a-ade5-4de8-b904-84e8f05af1ad" style="height: 52.7917px;"><td data-rtc-uid="6abac2b0-76ca-48a9-84ef-4c836b8cb0ec" style="height: 52.7917px;"><p data-rtc-uid="cde0c2d5-e918-48ab-8f67-98696d78d88d">PUT/search/api/v1/person_preferences/tabs/{var}<br data-rtc-uid="91999b52-ea52-4256-9f9b-562a18e4cf1b"></p></td><td data-rtc-uid="de8410ad-7433-41d3-9c15-854b8f9faba9" style="height: 52.7917px;">7.14</td><td data-rtc-uid="0d911489-18c5-4924-86d8-ef47fc0bb12c" style="height: 52.7917px;">555428</td><td data-rtc-uid="697af051-8ade-4c20-82cd-0127658bfad3" style="height: 52.7917px;">0.5</td></tr><tr data-rtc-uid="20e536b1-8959-416e-ad3e-d39adde93b07" style="height: 33.3333px;"><td data-rtc-uid="509dee36-2861-4609-986d-0bc8cfe53252" style="height: 33.3333px;"><p data-rtc-uid="cde0c2d5-e918-48ab-8f67-98696d78d88d">GET/admin/source/{var}<br data-rtc-uid="30f48a34-e729-4eac-af54-a2bf0df3c0e1"></p></td><td data-rtc-uid="c685ff88-7cf4-4be4-901d-5f96c6af1fa3" style="height: 33.3333px;"><span style="color: #232431;" data-rtc-uid="9e2894df-fa23-40e4-a56c-4e0b417fac4d">7.14</span></td><td data-rtc-uid="33a9be77-703e-4149-8ef1-c9fd6a9cb581" style="height: 33.3333px;"><span style="color: #232431;" data-rtc-uid="4b5129c4-c3f2-403b-bf57-372e87aad7bc">555428</span></td><td data-rtc-uid="ba685ace-8fbf-4d1a-9604-8ea4b29d6a2e" style="height: 33.3333px;"><span style="color: #232431;" data-rtc-uid="44810d14-1831-4e70-93ca-e48e8bb52849">0.5</span></td></tr></tbody></table>"""
# result = pd.read_html("""<p data-rtc-uid="19d62a05-9a7b-4756-a984-f4c579a4cc04"><br data-rtc-uid="86ebc166-799e-40f5-997b-4c6774924f21"></p><table class="relative-table mce-item-table" style="border-collapse: collapse; width: 845px; height: unset;" data-rtc-uid="8993c052-35a0-4fcd-b162-8f2c19a48819" data-widthmode="wide" data-lastwidth="845px" id="mce_1"><colgroup data-rtc-uid="93565d29-183a-457d-947a-4af3b4079c6f"><col data-rtc-uid="58f04697-3166-4e8e-837d-91103545cf4c" style="width: 485px;"><col data-rtc-uid="e134c6ec-0619-4100-a1fa-14d3d6445738" style="width: 129px;"><col data-rtc-uid="27a842a8-4fef-4568-bc97-465467bb08bf" style="width: 167px;"><col data-rtc-uid="a3735680-91c2-4386-8a4f-7f0d6597df17" style="width: 62px;"></colgroup><tbody data-rtc-uid="5f20fd1c-543a-4db0-a1ab-3be018d02396"><tr data-rtc-uid="e0f0fd28-9321-4b37-8d13-7d82c62c8a19" style="height: 52.7917px;"><td data-rtc-uid="d19e583f-23cd-470d-8019-5d56d65285f4" style="height: 52.7917px;">Transactions</td><td data-rtc-uid="7007d4f3-d717-4dce-9171-f1a6672ff64b" style="height: 52.7917px;">% в профиле</td><td data-rtc-uid="249909d2-3bc8-4d9e-bbd0-49152c2b0448" style="height: 52.7917px;">Интенсивность(o/ч)</td><td data-rtc-uid="5db08dc4-3fcf-46e9-87cb-a0265c2ed817" style="height: 52.7917px;">SLA</td></tr><tr data-rtc-uid="b04afb8a-ade5-4de8-b904-84e8f05af1ad" style="height: 52.7917px;"><td data-rtc-uid="6abac2b0-76ca-48a9-84ef-4c836b8cb0ec" style="height: 52.7917px;"><p data-rtc-uid="cde0c2d5-e918-48ab-8f67-98696d78d88d">PUT/search/api/v1/person_preferences/tabs/{var}<br data-rtc-uid="91999b52-ea52-4256-9f9b-562a18e4cf1b"></p></td><td data-rtc-uid="de8410ad-7433-41d3-9c15-854b8f9faba9" style="height: 52.7917px;">7.14</td><td data-rtc-uid="0d911489-18c5-4924-86d8-ef47fc0bb12c" style="height: 52.7917px;">555428</td><td data-rtc-uid="697af051-8ade-4c20-82cd-0127658bfad3" style="height: 52.7917px;">0.5</td></tr><tr data-rtc-uid="20e536b1-8959-416e-ad3e-d39adde93b07" style="height: 33.3333px;"><td data-rtc-uid="509dee36-2861-4609-986d-0bc8cfe53252" style="height: 33.3333px;"><p data-rtc-uid="cde0c2d5-e918-48ab-8f67-98696d78d88d">GET/admin/source/{var}<br data-rtc-uid="30f48a34-e729-4eac-af54-a2bf0df3c0e1"></p></td><td data-rtc-uid="c685ff88-7cf4-4be4-901d-5f96c6af1fa3" style="height: 33.3333px;"><span style="color: #232431;" data-rtc-uid="9e2894df-fa23-40e4-a56c-4e0b417fac4d">7.14</span></td><td data-rtc-uid="33a9be77-703e-4149-8ef1-c9fd6a9cb581" style="height: 33.3333px;"><span style="color: #232431;" data-rtc-uid="4b5129c4-c3f2-403b-bf57-372e87aad7bc">555428</span></td><td data-rtc-uid="ba685ace-8fbf-4d1a-9604-8ea4b29d6a2e" style="height: 33.3333px;"><span style="color: #232431;" data-rtc-uid="44810d14-1831-4e70-93ca-e48e8bb52849">0.5</span></td></tr></tbody></table>""")[0]
# # print(result.to_string())
# soup = BeautifulSoup(text, 'html.parser')
#
# values = [element.get_text() for element in soup.find_all(text=True) if element.strip()]
# print(values)
# # Убираем специальные символы из текстовых значений
# cleaned_values = [re.sub(r'[^\x00-\x7F]+', '', value) for value in values]
#
# # Заменяем старые значения на очищенные в исходном HTML
# for old_value, new_value in zip(values, cleaned_values):
#     text = text.replace(old_value, new_value)
#
# print(text)

# df = DataFrame(columns=["Название системы", "Процентная нагрузка", "Результат"], data=[("Платежи", "250", 100), ("Переводы", "500", 100), ("Баланс", "1000", 100)])
#
# html_text = ''
# with open('text_replace.html', 'r', encoding='UTF8') as f:
#     html_text = f.read()
#
# with open('result_replace.html', 'w', encoding='UTF8') as f:
#     html_text = html_text.replace('%%%pivot_table%%%', df.to_html())
#     f.write(html_text)

# import asyncio
# async def func1():
#     for i in range(5):
#         print(f"func1 - {i}")
#         await asyncio.sleep(randint(1, 5))
#
# async def func2():
#     for i in range(5):
#         print(f"func2 - {i}")
#         await asyncio.sleep(randint(1, 5))
#
# # Создаем цикл событий asyncio
# loop = asyncio.get_event_loop()
#
# # Запускаем асинхронные функции
# tasks = [
#     asyncio.ensure_future(func1()),
#     asyncio.ensure_future(func2())
# ]
#
# # Запускаем обе задачи параллельно
# loop.run_until_complete(asyncio.gather(*tasks))
#
# # Завершение цикла событий
# loop.close()

# from sys import stdout
# class Singleton:
#     _instances = {}
#
#     def __new__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             cls._instances[cls] = super(Singleton, cls).__new__(cls, *args, **kwargs)
#         return cls._instances[cls]
#
#
# class UpperCase(type):
#     def __new__(cls, name, bases, dct):
#         attrs = {name.upper(): value for name, value in dct.items() if not name.startswith("_")}
#         other_attrs = {name: value for name, value in dct.items() if name.startswith("_")}
#         attrs.update(other_attrs)
#         return super().__new__(cls, name, bases, attrs)
# class Other(metaclass=UpperCase):
#     bar = True
#     def __init__(self, name):
#         self.name = name
#
# other_instance = Other("Dima")
# other_instance2 = Other("Oleg")
#
# singleton = Singleton()
#
# singleton.other_instance = other_instance
# singleton.other_instance2 = other_instance2
#
# stdout.write(f"first -> {singleton.other_instance.name}, second -> {singleton.other_instance2.name}")
import os
# print(os.name)
# print(os.environ)
# print(os.getlogin())
# print(os.getpid())
# print(os.uname())
# print(os.getcwd())
# print(os.listdir(path="."))
# print(*os.walk(".", topdown=True))
# print(os.path)
# print(os.path.abspath("."))
# print(os.path.basename(os.path.abspath(".")))
# print(os.path.dirname(os.path.abspath(".")))
# print(os.path.relpath(os.path.abspath(".")))
# print(os.path.split(os.path.abspath("./API")))
# print(os.path.join(os.path.abspath("./API"), "../KAFKA/my_kafka.py"))


# files = []
#
#
# def recurs_find_files(path):
#
#     if os.path.isfile(path) and os.path.basename(path).endswith(".py") and not os.path.basename(path).startswith("_"):
#         files.append((os.path.basename(path), os.path.abspath(path)))
#         return path
#     elif os.path.isdir(path) and "lib" not in path:
#         for file in os.listdir(path):
#             if not file.startswith("."):
#                 full_path = os.path.join(path, file)
#                 recurs_find_files(full_path)
#     return files
#
# # print(*recurs_find_files(os.path.abspath(".")), sep="\n")
# print(*recurs_find_files("/home"), sep="\n")

# import requests
# from requests.adapters import HTTPAdapter
# from requests.packages.urllib3.util.retry import Retry
#
# session = requests.session()
#
# retry_strategy = Retry(
#     total=5,
#     backoff_factor=1,
#     status_forcelist=[500, 400],
#     allowed_methods=["GET", "POST"]
# )
# adapter = HTTPAdapter(max_retries=retry_strategy)
#
# session.mount("http://", adapter)
# session.mount("https://", adapter)
# response = session.get("http://localhost:8000/retry")
# print(response.status_code)


# from concurrent.futures import ThreadPoolExecutor
# import time
#
#
# # Функция, которая будет выполняться в потоке для обработки данных
# def process_data(data):
#     # Здесь можно добавить вашу логику обработки данных
#     print(f"Processing data: {data}")
#     # Добавим небольшую задержку для демонстрационных целей
#     time.sleep(1)
#     return f"Processed {data}"
#
#
# # Функция для обработки данных в нескольких потоках
# def process_data_in_parallel(data_list):
#     with ThreadPoolExecutor() as executor:
#         # Запускаем обработку данных в нескольких потоках
#         # map() автоматически распределяет задачи по доступным потокам
#         results = executor.map(process_data, data_list, timeout=2)
#
#     # Преобразуем результаты выполнения задач в список
#     processed_data = list(results)
#     return processed_data
#
#
# # Пример использования
# if __name__ == "__main__":
#     data_to_process = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     processed_data = process_data_in_parallel(data_to_process)
#     print("Processed data:", processed_data)

# import threading
# import queue
# from concurrent.futures import ThreadPoolExecutor
# data = queue.Queue()
#
# def worker(data):
#     current_thread_name = threading.current_thread().name
#     print(f"Текущий поток: {current_thread_name}")
#     time.sleep(2)
#     print(f"Поток {current_thread_name} получил данные ->{data}")
#
#
# datas = [1, 2, 3]
#
# with ThreadPoolExecutor(max_workers=3) as executor:
#     results = executor.map(worker, datas)
#     print(executor._max_workers)
#
# for result in results:
#     print(result)

# import multiprocessing
# import queue
# data = queue.Queue()
#
# def worker():
#     print(f"Процесс {multiprocessing.Process.name} начал свою работу")
#     d = data.get()
#     print(f"Процесс {multiprocessing.Process.name} получил данные {d}")
#     return random.randint(1, 2)
# th = []
# for i in range(3):
#     process = multiprocessing.Process(target=worker, name=f"Process_{i}")
#     th.append(process)
#     process.start()
#
# for i in range(3):
#     data.put(i)
#
# for i in th:
#     i.join()

# from sqlalchemy import Boolean, Date, DateTime, Float, Integer, String, Text, Numeric, Time, create_engine
# from sqlalchemy.orm import declarative_base, Mapped, mapped_column, sessionmaker, as_declarative, declared_attr
# from typing import Optional
# from datetime import date, datetime
# engine = create_engine(
#     url='postgresql://{username}:{password}@{host}:{port}/{db_name}',
#     echo=True
# )
# Session = sessionmaker(bind=engine)
#
# # Создание базового класса, более новый подход declarative_base()
# @as_declarative()
# class Base:
#     @declared_attr
#     def __tablename__(cls):
#         return cls.__name__.lower()
# class Example(Base):
#     """
#     Пример модели таблицы
#     :param id: Уникальный индентификатор
#     :type: int
#     """
#     __tablename__ = "example"
#
#     id: Mapped[int] = mapped_column(primary_key=True, type_=Integer, nullable=False, index=True, unique=True, autoincrement=True, doc="Уникальный индентификатор")
#     string_col: Mapped[str] = mapped_column(type_=String, nullable=False, index=True, unique=False, default='default_value')
#     int_col: Mapped[int] = mapped_column(type_=Integer, nullable=True, index=False, unique=False, default=None)
#     float_col: Mapped[float] = mapped_column(type_=Float, nullable=False, index=True, unique=False, default=0.0)
#     boolean_col: Mapped[bool] = mapped_column(type_=Boolean, nullable=False, index=True, unique=False, default=False)
#     date_col: Mapped[date] = mapped_column(type_=Date, nullable=False, index=True, unique=False, default=datetime.date.today())
#     datetime_col: Mapped[datetime] = mapped_column(type_=DateTime, nullable=False, index=True, unique=False, default=datetime.datetime.now())
#     time_col: Mapped[time] = mapped_column(type_=Time, nullable=False, index=False, unique=False, default=datetime.time())
#     text_col: Mapped[str] = mapped_column(type_=Text, nullable=False, index=False, unique=True, default='default_text')

# import threading
# from threading import Thread
#
#
# def summ(a, b):
#     print(threading.current_thread().name)
#     print(threading.current_thread().is_alive())
#     print(a + b)
#
#
# class UserThread(Thread):
#
#     def init(self, group=None, target=None, name=None,
#                  args=(), kwargs=None, daemon=None):
#         super().init(group=None, target=None, name=None,
#                  args=(), kwargs=None, daemon=None)
#         self.active = False
#
#     def run(self):
#         try:
#             print(f"Я запустил работу функции {self._target.__name__}")
#             self.active = True
#             self._target(*self._args, **self._kwargs)
#         except Exception as error:
#             raise Exception(error)
#
#
# usthr = UserThread(target=summ, name="Test", args=(1, 2))
# print(usthr.__dict__, dir(usthr), sep='\n')
# usthr.run()


# from flask import Flask
# from prometheus_client import Gauge, generate_latest, CONTENT_TYPE_LATEST, push_to_gateway, CollectorRegistry
# app = Flask(__name__)
#
# registry = CollectorRegistry()
# threads = Gauge("threads_metric", "Threads", labelnames=["name"], registry=registry)
# q = queue.Queue()
# def func():
#     while True:
#         for i in range(1):
#             t = threading.Thread(name=f"Thread_func - {random.randint(1, 3)}", daemon=True)
#             q.put(t.name)
#             t.start()
#         print(threading.current_thread().name)
#         currents = {t: random.randint(1, 10) for t in q.queue}
#         for key, value in currents.items():
#             threads.labels(name=key).set(value=value)
#         push_to_gateway(gateway="localhost:9091", job="myjob", registry=registry)
#         time.sleep(5)
#         while not q.empty():
#             q.get_nowait()
#
# # @app.route('/metrics')
# # def metrics():
# #     print(q.queue)
# #     currents = {t: random.randint(1, 10) for t in q.queue}
# #     for key, value in currents.items():
# #         threads.labels(name=key).set(value=value)
# #     return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}
#
#
# if __name__ == '__main__':
#     t = threading.Thread(target=func, name="FuncThread", daemon=True)
#     print(threading.active_count(), threading.enumerate(), sep='\n')
#     t.start()
#     app.run(host="localhost", port=7777)
# import asyncio
# async def func():
#     print("Start func")
#     time.sleep(5)
#     print("End func")
#
# async def main():
#     print("Start process")
#     asyncio.create_task(func())
#     print("Hey baby")
#
#
# asyncio.run(main())

# # Пример тестирования с помощью моков
# def get_joke():
#     url = "https://api.chucknorris.io/jokes/random"
#     try:
#         response = requests.get(url=url, timeout=10)
#         response.raise_for_status()
#         joke = response.json()["value"]
#         return joke
#     except requests.exceptions.Timeout:
#         return "No jokes"
#     except requests.exceptions.ConnectionError:
#         return "No jokes"
#     except requests.exceptions.HTTPError:
#         return "No jokes"
#
# def len_joke():
#     joke = get_joke()
#     return len(joke)
#
# print(len_joke())
#
# import unittest
# from unittest.mock import patch, MagicMock
#
# class TestLenJoke(unittest.TestCase):
#     @patch("test.get_joke")
#     def test_len_joke(self, mock_get_joke):
#         mock_get_joke.return_value = "one"
#         result = len_joke()
#         self.assertEquals(result, 3)
#     @patch("test.requests")
#     def test_get_joke(self, mock_requests):
#         mock_response = MagicMock()
#         mock_response.status_code = 200
#         mock_response.json.return_value = {"value": "hello world"}
#         mock_requests.get.return_value = mock_response
#         self.assertEquals(get_joke(), "hello world")
#
#
#     @patch("test.requests.get")
#     def test_exception_get_joke(self, mock_requests):
#         mock_requests.side_effect = requests.exceptions.Timeout("Seems the server is down")
#         self.assertEqual(get_joke(), "No jokes")
#
#     @patch("test.requests.get")
#     def test_exception_raise_status_get_joke(self, mock_requests_get):
#         mock_requests_get.side_effect = requests.exceptions.HTTPError("status code not 200")
#         self.assertEquals(get_joke(), "No jokes")

# import pandas as pd
#
# # Создадим тестовые датафреймы
# df_test = pd.DataFrame({
#     'Компонент': ['Postgress cluster', 'Postgress cluster', 'Postgress cluster', 'Postgress cluster'],
#     'Имя': ['dp_app1', 'dp_app2', 'dp_app3', 'dp_pay1'],
#     'Server/Pod': [1, 1, 1, None],
#     'Процент нагрузки': [100, 100, 100, 100]
# })
#
# df_prod1 = pd.DataFrame({
#     'Компонент': ['Postgress cluster', 'Postgress cluster', 'Postgress cluster'],
#     'Имя': ['dp_app1', 'dp_app2', 'dp_app3'],
#     'Server/Pod': [1, 1, 1],
#     'Процент нагрузки': [50, 2, 50]
# })
#
# df_prod2 = pd.DataFrame({
#     'Компонент': ['Postgress cluster', 'Postgress cluster'],
#     'Имя': ['dp_app1', 'dp_app2'],
#     'Server/Pod': [1, 1],
#     'Процент нагрузки': [50, 4]
# })
#
# print(df_test)
# # Объединим датафреймы по столбцу "Компонент" с помощью pd.concat
# result = pd.concat([df_test, df_prod1, df_prod2], ignore_index=True).fillna(0)
#
# print(result)
#
# # Добавим столбцы с процентами нагрузки для PROD1 и PROD2
# result['TEST'] = result['Процент нагрузки'].where(result['Имя'].isin(df_prod1['Имя']), 0)
# result['PROD1'] = result['Процент нагрузки'].where(result['Имя'].isin(df_prod1['Имя']), 0)
# result['PROD2'] = result['Процент нагрузки'].where(result['Имя'].isin(df_prod2['Имя']), 0)
#
# # Отсортируем колонки в определенном порядке
# result = result[['Компонент', 'Имя', 'Server/Pod', 'Процент нагрузки', 'TEST',  'PROD1', 'PROD2']].fillna(0)
# print(result)
#
# # Сформируем сводную таблицу с помощью pd.pivot_table
# result = pd.pivot_table(result, values='Процент нагрузки', index='Компонент', columns='Имя', aggfunc='mean')
#
# print(result)

# import asyncio
#
#
# # имитация  асинхронного соединения с некой периферией
# async def get_conn(host, port):
#     class Conn:
#         async def put_data(self):
#             print('Отправка данных...')
#             await asyncio.sleep(2)
#             print('Данные отправлены.')
#
#         async def get_data(self):
#             print('Получение данных...')
#             await asyncio.sleep(2)
#             print('Данные получены.')
#
#         async def close(self):
#             print('Завершение соединения...')
#             await asyncio.sleep(2)
#             print('Соединение завершено.')
#
#     print('Устанавливаем соединение...')
#     await asyncio.sleep(2)
#     print('Соединение установлено.')
#     return Conn()
#
#
# class Connection:
#     # этот конструктор будет выполнен в заголовке with
#     def __init__(self, host, port):
#         self.host = host
#         self.port = port
#
#     # этот метод будет неявно выполнен при входе в with
#     async def __aenter__(self):
#         self.conn = await get_conn(self.host, self.port)
#         return self.conn
#
#     # этот метод будет неявно выполнен при выходе из with
#     async def __aexit__(self, exc_type, exc, tb):
#         await self.conn.close()
#
#
# async def main():
#     async with Connection('localhost', 9001) as conn:
#         send_task = asyncio.create_task(conn.put_data())
#         receive_task = asyncio.create_task(conn.get_data())
#
#         # операции отправки и получения данных выполняем конкурентно
#         await send_task
#         await receive_task
#
#
# asyncio.run(main())

# import asyncio
# import time
# from aiohttp import ClientSession
#
#
# async def get_weather(city):
#     async with ClientSession() as session:
#         url = f'http://api.openweathermap.org/data/2.5/weather'
#         params = {'q': city, 'APPID': '2a4ff86f9aaa70041ec8e82db64abf56'}
#
#         async with session.get(url=url, params=params) as response:
#             weather_json = await response.json()
#             print(f'{city}: {weather_json["weather"][0]["main"]}')
#
#
# async def main(cities_):
#     tasks = []
#     for city in cities_:
#         tasks.append(asyncio.create_task(get_weather(city)))
#
#     for task in tasks:
#         await task
#
#
# cities = ['Moscow', 'St. Petersburg', 'Rostov-on-Don', 'Kaliningrad', 'Vladivostok',
#           'Minsk', 'Beijing', 'Delhi', 'Istanbul', 'Tokyo', 'London', 'New York']
#
# print(time.strftime('%X'))
#
# asyncio.run(main(cities))
#
# print(time.strftime('%X'))


# def wrap_func(*args, **kwargs):
#     print("Возвращаем функцию возврата обертки...")
#     def wrap(func):
#         print("Возвращаем обертку...")
#         print(f"Результат -> {sum(args)}")
#         def wrapper(*args, **kwargs):
#             print("Работает обертка....")
#             result = func(*args, **kwargs)
#             print("Заканчиваем работу обертки...")
#             return result
#         return wrapper
#     return wrap
# @wrap_func(1, 2)
# def func(a, b, c):
#     return a + b + c
#
# # func = wrap(func)
# # func = wrap_func(1, 2)(func)
# print("Вызываем функцию")
# print(func(1, 2, 3))

import flask
import asyncio
import aiohttp

# app = flask.Flask(__name__)
#
# # Асинхронно
#
# async def req():
#     print("Выполняю запрос")
#     async with aiohttp.ClientSession() as session:
#         async with session.get("https://api.chucknorris.io/jokes/random") as response:
#             print(f"Запрос выполнен успешно -> {await response.json()}")
#             await asyncio.sleep(3)
# @app.route("/")
# async def hello():
#     print(time.strftime("%X"))
#     print("Я принимаю и выполняю запрос...")
#     task = asyncio.create_task(req())
#     await task
#     print("Я закончил обработку запроса и возвращаю результат")
#     print(time.strftime("%X"))
#     return "Привет"

# Синхронно
# async def req():
#     print("Выполняю запрос")
#     async with aiohttp.ClientSession() as session:
#         async with session.get("https://api.chucknorris.io/jokes/random") as response:
#             print(f"Запрос выполнен успешно -> {await response.json()}")
#             await asyncio.sleep(3)
# @app.route("/")
# def hello():
#     print(time.strftime("%X"))
#     print("Я принимаю и выполняю запрос...")
#     time.sleep(3)
#     print("Я закончил обработку запроса и возвращаю результат")
#     print(time.strftime("%X"))
#     return "Привет"

# if __name__ == "__main__":
#     app.run(host="localhost", port=7777, threaded=False)

# def simple_gen():
#     while True:
#         x = yield
#         print(f"Получили x={x} и умножили {x * 2}")
#
# gen = simple_gen()
# print(next(gen))
# gen.send(2)
# gen.send(4)

# import fastapi
# import uvicorn
import flask
import asyncio
import aiohttp


#
# app = fastapi.FastAPI()

# Асинхронный код
# async def req():
#     print("Выполняю запрос")
#     async with aiohttp.ClientSession() as session:
#         async with session.get("https://api.chucknorris.io/jokes/random") as response:
#             print(f"Запрос выполнен успешно -> {await response.json()}")
#             await asyncio.sleep(3)
# @app.get("/")
# async def hello():
#     print(time.strftime("%X"))
#     print("Я принимаю и выполняю запрос...")
#     await asyncio.gather(req())
#     print("Я закончил обработку запроса и возвращаю результат")
#     print(time.strftime("%X"))
#     return "Hello"

# # Синхронный код
# def req():
#     print("Выполняю запрос")
#     response = requests.get("https://api.chucknorris.io/jokes/random")
#     print(f"Запрос выполнен успешно -> {response.json()['value']}")
#     time.sleep(3)
# @app.get("/")
# def hello():
#     print(time.strftime("%X"))
#     print("Я принимаю и выполняю запрос...")
#     req()
#     print("Я закончил обработку запроса и возвращаю результат")
#     print(time.strftime("%X"))
#     return "Hello"
#
#
# if __name__ == "__main__":
#     uvicorn.run(app=app, host="localhost", port=7777)

# app = flask.Flask(__name__)
# Асинхронный код
# async def req():
#     print("Выполняю запрос")
#     async with aiohttp.ClientSession() as session:
#         async with session.get("https://api.chucknorris.io/jokes/random") as response:
#             print(f"Запрос выполнен успешно -> {await response.json()}")
#             await asyncio.sleep(3)
# @app.route("/")
# async def hello():
#     print(time.strftime("%X"))
#     print("Я принимаю и выполняю запрос...")
#     await asyncio.gather(req())
#     print("Я закончил обработку запроса и возвращаю результат")
#     print(time.strftime("%X"))
#     return "Hello"

# Синхронный код
# def req():
#     print("Выполняю запрос")
#     response = requests.get("https://api.chucknorris.io/jokes/random")
#     print(f"Запрос выполнен успешно -> {response.json()['value']}")
#     time.sleep(3)
# @app.route("/")
# def hello():
#     print(time.strftime("%X"))
#     print("Я принимаю и выполняю запрос...")
#     time.sleep(2)
#     req()
#     print("Я закончил обработку запроса и возвращаю результат")
#     print(time.strftime("%X"))
#     return "Hello"
#
# if __name__ == "__main__":
#     app.run(host="localhost", port=7777)

# Асинхронный код
# async def req():
#     print("Выполняю запрос")
#     async with aiohttp.ClientSession() as session:
#         async with session.get("https://api.chucknorris.io/jokes/random") as response:
#             print(f"Запрос выполнен успешно -> {await response.json()}")
#             await asyncio.sleep(3)
# async def hello():
#     print(time.strftime("%X"))
#     print("Я принимаю и выполняю запрос...")
#     await asyncio.gather(req(), req())
#     print("Я закончил обработку запроса и возвращаю результат")
#     print(time.strftime("%X"))
#     return "Hello"
#
# asyncio.run(hello())

# Синхронный код
# def req():
#     print("Выполняю запрос")
#     response = requests.get("https://api.chucknorris.io/jokes/random")
#     print(f"Запрос выполнен успешно -> {response.json()['value']}")
#     time.sleep(3)
# def hello():
#     print(time.strftime("%X"))
#     print("Я принимаю и выполняю запрос...")
#     time.sleep(2)
#     req()
#     req()
#     print("Я закончил обработку запроса и возвращаю результат")
#     print(time.strftime("%X"))
#     return "Hello"
#
# hello()

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"Result time: {(time.perf_counter() - start):.3f} - Second & MiliSecond")
        return result

    return wrapper


# async def req():
#     try:
#         async with aiohttp.ClientSession() as session:
#             async with session.get("https://api.chucknorris.io/jokes/random") as response:
#                 result = await response.json()
#                 return result["value"]
#     except ConnectionError:
#         raise ConnectionError()
#
# @timer
# async def main():
#     tasks = asyncio.gather(req(), req())
#     result = await tasks
#     print(*result, sep="\n", end=".")
#
# asyncio.run(main())

# def req():
#     try:
#         response = requests.get("https://api.chucknorris.io/jokes/random")
#         return response.json()["value"]
#     except ConnectionError:
#         raise ConnectionError()
#
# @timer
# def main():
#     tasks = [req() for _ in range(2)]
#     print(*tasks, sep="\n", end=".")
#
# main()

# images = [
#     "https://i.pinimg.com/originals/52/28/d8/5228d856819f806ea3aec253e87929ad.jpg",
#     "https://i.ebayimg.com/images/g/vfUAAOSwolhkfwRp/s-l1200.webp",
#     "https://i.imgur.com/ZQMoo9G.jpg"
# ]
# async def save_to_disc(file):
#     with open(f"{random.randint(1, 10)}_image.png", "wb") as f:
#         f.write(file)
#
# async def req():
#     try:
#         async with aiohttp.ClientSession() as session:
#             async with session.get(url=f"{random.choice(images)}") as response:
#                 result = await response.read()
#                 return result
#     except ConnectionError:
#         raise ConnectionError()
# @timer
# async def main():
#     response = await asyncio.gather(req(), req(), req())
#     await asyncio.gather(save_to_disc(response[0]), save_to_disc(response[1]), save_to_disc(response[2]))
#
# asyncio.run(main())

# import flask
# import requests
#
# app = flask.Flask(__name__, template_folder='templates')
#
# @app.route("/")
# def func():
#     return flask.render_template("./eexample.html")
# @app.route("/index")
# def index():
#     url = "https://jsonplaceholder.typicode.com/posts"
#     data = {"title": "My Post", "body": "This is the body of my post", "userId": 1}
#     headers = {"Content-Type": "application/json"}
#
#     response = requests.post(url, headers=headers, data=data)
#     return response.text
#
# if __name__ == "__main__":
#     app.run("localhost", 7777)

# from requests import Session
#
#
# class AsyncRequest(Session):
#     """
#
#     """
#
#     def __init__(
#             self,
#             *args,
#             **kwargs
#     ):
#         super().__init__(*args, **kwargs)
#         self.my_flag = kwargs.get("my_flag", False)
#
#     def request(self, *args, **kwargs):
#         if self.my_flag:
#             print("Hello World!")
#         else:
#             super().request(*args, **kwargs)
#
#
# asr = AsyncRequest(my_flag=True)
# print(asr.my_flag)
# asr.request(method="get", url="http://localhost:7777")


# def func(data):
#     if len(data) <= 2:
#         return data
#     datas = sorted(data.copy(), key=lambda x: x["id"])
#     uniq = []
#     result = []
#     for d in sorted(data, key=lambda x: x["id"]):
#         if d["report_uuid"] not in uniq:
#             uniq.append(d["report_uuid"])
#             result.append(d)
#             del datas[datas.index(d)]
#     return result + func(datas)
# original_array = [
#     {"id": 1, "report_uuid": 123457, "data": []},
#     {"id": 6, "report_uuid": 123457, "data": []},
#     {"id": 2, "report_uuid": 123457, "data": []},
#     {"id": 3, "report_uuid": 123457, "data": []},
#     {"id": 4, "report_uuid": 623456, "data": []},
#     {"id": 5, "report_uuid": 623456, "data": []},
#     {"id": 7, "report_uuid": 723456, "data": []},
#     {"id": 8, "report_uuid": 823456, "data": []},
#     {"id": 9, "report_uuid": 723456, "data": []},
#     {"id": 10, "report_uuid": 923456, "data": []},
# ]
#
# print(*func(original_array), sep="\n")

#
# def sort_duplicates_data(data: list[dict], key: str) -> list[dict]:
#     """
#     Функция изменения порядка очереди
#     :param data: Список словарей с данными по дашбордам
#     :param key: Ключ сортировки списка
#     :return: Отсортированный список
#     """
#     if len(data) <= 2:
#         return sorted(data, key=lambda x: x["id"])
#
#     uniq_report_uuid = set()
#     result = []
#
#     # Идем по отсортированному по id списку
#     for d in sorted(data, key=lambda x: x["id"]):
#
#         # Если нет дубликатов в ключе сортировки
#         if d[key] not in uniq_report_uuid:
#             uniq_report_uuid.add(d[key])
#
#             # Добавляем в результат
#             result.append(d)
#
#     # Удаляем из data уже добавленные в результат элементы
#     remaining_data = [d for d in data if d not in result]
#
#     # Рекурсивно вызываем функцию для оставшихся элементов
#     return result + sort_duplicates_data(remaining_data, key)
#
#
#
# original_array = [
#     {"id": 1, "report_uuid": 123457, "data": []},
#     {"id": 6, "report_uuid": 123457, "data": []},
#     {"id": 2, "report_uuid": 123457, "data": []},
#     {"id": 3, "report_uuid": 123457, "data": []},
#     {"id": 4, "report_uuid": 623456, "data": []},
#     {"id": 5, "report_uuid": 623456, "data": []},
#     {"id": 7, "report_uuid": 723456, "data": []},
#     {"id": 8, "report_uuid": 823456, "data": []},
#     {"id": 9, "report_uuid": 723456, "data": []},
#     {"id": 10, "report_uuid": 923456, "data": []},
# ]
#
# print(*func(original_array, "report_uuid"), sep="\n")
# import selectors
# import socket
# from selectors import SelectorKey
# from typing import List, Tuple
#
# selector = selectors.DefaultSelector()
# server_socket = socket.socket()
# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# server_address = ('127.0.0.1', 8000)
# server_socket.setblocking(False)
# server_socket.bind(server_address)
# server_socket.listen()
# selector.register(server_socket, selectors.EVENT_READ)
#
# while True:
#     events: List[Tuple[SelectorKey, int]] = selector.select(timeout=1)
#     if len(events) == 0:
#         print('Событий нет, подожду еще!')
#     for event, _ in events:
#         event_socket = event.fileobj
#         if event_socket == server_socket:
#             connection, address = server_socket.accept()
#             connection.setblocking(False)
#             print(f"Получен запрос на подключение от {address}")
#             selector.register(connection, selectors.EVENT_READ)
#         else:
#             data = event_socket.recv(1024)
#             print(f"Получены данные: {data}")
#             event_socket.send(data)
# import socket
#
# async def echo(connection: socket, loop: AbstractEventLoop) -> None:
#     try:
#         while data := await loop.sock_recv(connection, 1024):
#             if data == b'boom\n':
#                 raise Exception("Неожиданная ошибка сети")
#             await loop.sock_sendall(connection, data)
#     except Exception as error:
#         await loop.sock_sendall(connection, (str(error) + "\n").encode())
#     finally:
#         connection.close()
#         os.abort()
#
# async def listen_for_connections(server_socket: socket, loop: AbstractEventLoop):
#     while True:
#         connection, address = await loop.sock_accept(server_socket)
#         connection.setblocking(False)
#         print(f"Получен запрос на подключение от {address}")
#         asyncio.create_task(echo(connection, loop))
#
#
# async def main():
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#     server_address = ('127.0.0.1', 8000)
#     server_socket.setblocking(False)
#     server_socket.bind(server_address)
#     server_socket.listen()
#
#     await listen_for_connections(server_socket, asyncio.get_event_loop())
#
# asyncio.run(main())
#
# import asyncio
# import socket
# from types import TracebackType
# from typing import Optional, Type
#
#
# class ConnectedSocket:
#     def __init__(self, server_socket):
#
#         self._connection = None
#         self._server_socket = server_socket
#
#     async def __aenter__(self):
#
#         print('Вход в контекстный менеджер, ожидание подключения')
#         loop = asyncio.get_event_loop()
#         connection, address = await loop.sock_accept(self._server_socket)
#         self._connection = connection
#         print('Подключение подтверждено')
#         return self._connection
#
#     async def __aexit__(self,
#                         exc_type: Optional[Type[BaseException]],
#                         exc_val: Optional[BaseException],
#                         exc_tb: Optional[TracebackType]):
#         print('Выход из контекстного менеджера')
#         self._connection.close()
#         print('Подключение закрыто')
#
#
# async def main():
#     loop = asyncio.get_event_loop()
#
#     server_socket = socket.socket()
#     server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#     server_address = ('127.0.0.1', 8000)
#     server_socket.setblocking(False)
#     server_socket.bind(server_address)
#     server_socket.listen()
#
#     async with ConnectedSocket(server_socket) as connection:
#         data = await loop.sock_recv(connection, 1024)
#         print(data)
#
#
# asyncio.run(main())

# import asyncio
# import aiohttp
# from aiohttp import ClientSession
#
#
# async def fetch_status(session: ClientSession,
#                        url: str) -> int:
#     ten_millis = aiohttp.ClientTimeout(total=.01)
#     async with session.get(url, timeout=ten_millis) as result:
#         return result.status
#
#
# async def main():
#     session_timeout = aiohttp.ClientTimeout(total=1, connect=.1)
#     async with aiohttp.ClientSession(timeout=session_timeout) as session:
#         await fetch_status(session, 'https://example.com')
# asyncio.run(main())

# import asyncio
# import aiohttp
#
# async def first():
#     print("Start first")
#     async with aiohttp.ClientSession() as session:
#         await asyncio.sleep(randint(1, 3))
#         async with session.get("https://example.com") as response:
#             return response.status
#
# async def second():
#     print("Start second")
#     async with aiohttp.ClientSession() as session:
#         await asyncio.sleep(randint(20, 40))
#         async with session.get("https://example.com") as response:
#             return response.status
# async def func_count():
#     for i in range(1000):
#         await asyncio.sleep(5)
#         print(f"Ready {i}")
# async def main():
#     tasks = [asyncio.create_task(first()), asyncio.create_task(second())]
#     print(20 * 80)
#     for i in range(2):
#         print(i)
#     tas = asyncio.create_task(func_count())
#     for task in asyncio.as_completed(tasks):
#         result = await task
#         print(result)
#     await tas
#
# asyncio.run(main())
# import pandas as pd
# CPU_Limits_df = pd.DataFrame({'POD': ['app', 'app', 'app'], 'Container': ['payg', 'payg', 'payg3'], 'Timestamp': [None, None, None], 'Value': [3, 5, 10]})
# RAM_Limits_df = pd.DataFrame({'POD': ['app'], 'Container': ['payg'], 'Timestamp': [None], 'Value': [5]})
# CPU_df = pd.DataFrame({'POD': ['app'], 'Container': ['payg'], 'Timestamp': [None], 'Value': [10]})
# RAM_df = pd.DataFrame({'POD': ['app'], 'Container': ['payg'], 'Timestamp': [None], 'Value': [15]})
# df_dict = {'CPU_Limits': CPU_Limits_df, 'RAM_Limits': RAM_Limits_df, 'CPU': CPU_df, 'RAM': RAM_df}
#
#
# def transform_data(df_dict):
#     """
#     Transforms the data in the provided dictionaries into a single DataFrame with a multi-level index.
#
#     Args:
#         df_dict (dict): A dictionary where the keys are the metric names and the values are the corresponding DataFrames.
#
#     Returns:
#         pd.DataFrame: A DataFrame with a multi-level index (pod, container, metrics) and the corresponding values.
#     """
#     # Create a list to store the transformed data
#     result = []
#
#     # Iterate over all unique pods and containers
#     for pod in set(sum([df['POD'].tolist() for df in df_dict.values()], [])):
#         for container in set(sum([df['Container'].tolist() for df in df_dict.values()], [])):
#             for metric in df_dict.keys():
#                 # Create a dictionary to store the row data
#                 row = {'pod': pod, 'container': container, 'metrics': metric, 'value': 0}
#
#                 # Get the DataFrame for the current metric, if it exists
#                 df = df_dict.get(metric, None)
#                 if df is not None:
#                     # Check if the current pod and container exist in the DataFrame
#                     mask = (df['POD'] == pod) & (df['Container'] == container)
#                     if mask.any():
#                         row['value'] = df.loc[mask, 'Value'].values[0]
#
#                 # Append the row to the result list
#                 result.append(row)
#
#     # Create a DataFrame from the result list and set the index
#     data = pd.DataFrame(result)
#     data = data.set_index(['pod', 'container', 'metrics'])
#
#     return data

# print(transform_data(df_dict))
# df = pd.DataFrame({'POD': ['app'], 'Container': ['payg', 'payg2', 'payg3'], 'Timestamp': [None], 'Value': [3, 5, 10]})
#
# max_length = max(len(column) for column in df.columns)
# df = df.reindex(columns=df.columns.tolist() + list(range(max_length - len(df.columns))))
# df.fillna(None, inplace=True)
# for key, df in df_dict.items():
#     df["Metrics"] = key
# result = pd.concat(df_dict.values())
# print(result)
# pv = result.pivot_table(index=["POD", "Container", "Metrics"], values="Value", aggfunc=np.sum, fill_value=0)
# t = pv.info
# print(pv)

# from multiprocessing import Process, Value, current_process
#
# def increment_value(shared_val: Value) -> None:
#     print(current_process().name)
#     shared_val.value += 1
#     print(shared_val.value)
# if __name__ == "__main__":
#     integer = Value("i", 0)
#     p = [Process(target=increment_value, args=(integer,)) for _ in range(2)]
#     [i.start() for i in p]
#     [i.join() for i in p]

# from concurrent.futures import ProcessPoolExecutor
# import asyncio
# from multiprocessing import Value
# shared_counter: Value
# def init(counter: Value):
#     global shared_counter
#     shared_counter = counter
# def increment():
#     with shared_counter.get_lock():
#         shared_counter.value += 1
#
# async def main():
#     counter = Value('d', 0)
#     with ProcessPoolExecutor(initializer=init,
#         initargs=(counter,)) as pool:
#         await asyncio.get_running_loop().run_in_executor(pool, increment)
#     print(counter.value)
# if __name__ == "__main__":
#     asyncio.run(main())

# import asyncio
# import asyncpg
# from typing import List, Dict
# from concurrent.futures.process import ProcessPoolExecutor
# product_query = \
# """
# SELECT
# p.product_id,
# p.product_name,
# p.brand_id,
# s.sku_id,187
# pc.product_color_name,
# ps.product_size_name
# FROM product as p
# JOIN sku as s on s.product_id = p.product_id
# JOIN product_color as pc on pc.product_color_id = s.product_color_id
# JOIN product_size as ps on ps.product_size_id = s.product_size_id
# WHERE p.product_id = 100"""
# async def query_product(pool):
#     async with pool.acquire() as connection:
#         return await connection.fetchrow(product_query)
# async def query_products_concurrently(pool, queries):
#     queries = [query_product(pool) for _ in range(queries)]
#     return await asyncio.gather(*queries)
# def run_in_new_loop(num_queries: int) -> List[Dict]:
#     async def run_queries():
#         async with asyncpg.create_pool(host='127.0.0.1',
#                                         port=5432,
#                                         user='postgres',
#                                         password='password',
#                                         database='products',
#                                         min_size=6,
#                                         max_size=6) as pool:
#             return await query_products_concurrently(pool, num_queries)
#     results = [dict(result) for result in asyncio.run(run_queries())]
#     return results
# async def main():
#     loop = asyncio.get_running_loop()
#     pool = ProcessPoolExecutor()
#     tasks = [loop.run_in_executor(pool, run_in_new_loop, 10000) for _ in
#     range(5)]
#     all_results = await asyncio.gather(*tasks)
#     total_queries = sum([len(result) for result in all_results])
#     print(f'Извлечено товаров из базы данных: {total_queries}.')
# if __name__ == "__main__":
#     asyncio.run(main())