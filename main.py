from dataclasses import dataclass


# class Cat:
#     breed: str = "Siam"
#     age: int = "15"
#
#
# print(getattr(Cat, "breed"), getattr(Cat, "age"), end = " ")
# cat_1 = Cat()
# cat_1.age = 17
# print()
# print(getattr(cat_1, "age"), getattr(cat_1, "x", "Error request"))

# class Car:
#     speed: int = 200
#     color: str = "red"
#
# print(Car.speed, Car.color, end = " ")

# class Man:
#     hight: int = 175
#     wieght: int = 65
#     count: int = 150
#
# print(setattr(Man, "count", 150 - 2))
# print(Man.__dict__)

#
# class Summer:
#     def count():
#         print(1 + 1)
#
# Summer.count()
# a = Summer()
# a.count()

# class Dog:
#     def sens(self):
#         print("Hello")
#
# Dog.sens(Dog())
# a = Dog()
# a.sens()

# class Person:
#
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age
#
#     def printed(self):
#         return f"Name - {self.name} and Age - {self.age}"
#
# first_person = Person("Dima", 22)
# second_person = Person("Dasha", 21)
# print(first_person.printed(), second_person.printed(), sep = "\n")

# class T:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def compare(self):
#         return "Ravn" if self.x == self.y or self.x == self.z or self.y == self.z else "Neravn"
#
# t1 = T(1, 2, 3)
# t2 = T(1, 2, 1)
# print(getattr(t1, "z"), getattr(t2, "z"))
# print(t1.compare(), t2.compare())


# class Person:
#     "Класс полученмя имени и возраста человека"
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __del__(self):
#         print(f"Delete {str(self)}")
#     def get_attr(self):
#         print(self.name, self.age, end = " ")
#
#
# obj = Person("Dasha", 21)
# print(obj.__dict__)
# setattr(obj, "color", "Black")
# print(obj.__dict__)
# print(Person.__doc__)
# obj.get_attr()

# class Test:
#     "Метода класса для теста"
#
#     mins = 1
#     maxs = 10
#     @classmethod
#     def validate(cls, arg):
#         return cls.mins <= arg <= cls.maxs
#
#     def __init__(self, x, y):
#         self.x = self.y = 0
#
#         if self.validate(x) and self.validate(y):
#             self.x = x
#             self.y = y
#             print(self.summ(self.x, self.y))
#
#
#     @staticmethod
#     def summ(x, y):
#         return x + y
#
#
# obj = Test(1, 10)
# print(obj.validate(5))
# print(obj.summ(5, 5))


# class Test:
#     "Тестовый метод класса"
#
#
#     def __check_value(self, value):
#         return isinstance(value, int) or isinstance(value, str)
#
#
#     def set_cor(self, x, y):
#         if self.__check_value(x) and self.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             raise ValueError("Error value")
#
#     def get_cor(self):
#         return self.__x, self.__y
#
#
# obj = Test()
#
# print(obj.set_cor(11, "Hello"))
# print(obj.__dict__)
# print(obj.get_cor())
# print(dir(obj))

# class Test:
#     __attr = {
#         "name":"Dima",
#         "age" : 22
#     }
#
#     def __init__(self):
#         self.__dict__ = self.__attr
#
#
# a = Test()
# print(a.__dict__)
# b = Test()
# print(b.__dict__)
# print(setattr(b, "color", "white"))
# print(b.__dict__)


# class Test:
#     def getattr(self):
#         return self.key
#     def setattr(self, key):
#         self.key = key
#
#
#     def delattr(self,):
#         del self.key
#
# a = Test()
#
# a.setattr("I")
# print(a.getattr())
# a.delattr()
# print(a.__dict__)

# class Test:
#     def __init__(self, x):
#         self.x = x
#
#
# a = Test("1")
# print(a.__dict__)
# print(getattr(a, "x"))
# delattr(a,"x")
# print(a.__dict__)
# setattr(a,"color", "black")
# print(a.__dict__)

# class Counter:
#     "magic method _call_"
#     def __init__(self):
#         self.__counter = 0
#
#     def __call__(self, *args, **kwargs):
#         print(f"call - {self}")
#         self.__counter += 1
#         return self.__counter
#
# c = Counter()
# c2 = Counter()
# res2 = c2()
# c()
# res = c()
# print(res, res2, sep = "\n")

# class StripChars:
#     def __init__(self, chars):
#         self.__chars = chars
#
#     def __call__(self, *args, **kwargs):
#         if not isinstance(args[0], str):
#             raise TypeError("Error")
#         return args[0].strip(self.__chars)
#
# s = StripChars("?/.!, ")
# res = s(" Hello World! ")
# print(res)

# class Soda:
#     "Класс для определения типа газированной воды"
#     def __init__(self, add):
#         if isinstance(add, str):
#             self.__add = add
#         else:
#             self.__add = None
#
#     def show_my_drink(self):
#         if self.__add:
#             print(f"Газировка и {self.__add}")
#         else:
#             print("Обычная Газировка")
#
#     def __repr__(self):
#         return f"{self.__class__}: {self.__add}"
#
#     def __str__(self):
#         return self.__add
#
#
# a = Soda("")
# b = Soda("red")
#
# a.show_my_drink()
# b.show_my_drink()

# class Test:
#     def __init__(self, *args):
#         self.__count = args
#
#     def __repr__(self):
#         return f"{self.__class__}: {self.__count}"
#
#     def __str__(self):
#         return f"{self.__count}"
#
#     def __len__(self):
#         return len(self.__count)
#
#     def __abs__(self):
#         return list(map(abs, self.__count))
#
# a = Test(1, 2, 3)
# print(a.__dict__)
# print(a)
# print(len(a))
# print(abs(a))
# class Clock:
#     __DAY = 86400
#
#     def __init__(self, seconds: int):
#         if not isinstance(seconds, int):
#             raise TypeError("Секунды должны быть целым числом")
#         self.seconds = seconds % self.__DAY
#
#     def get_time(self):
#         s = self.seconds % 60
#         m = (self.seconds // 60) % 60
#         h = (self.seconds // 3600) % 24
#         return f"{self.get_formated(h)}:{self.get_formated(m)}:{self.get_formated(s)}"
#
#     @classmethod
#     def get_formated(self, x):
#         return str(x).rjust(2, "0")
#
# a = Clock(1000)
# print(a.get_time())
# @dataclass
# class Test:
#     "class Test"
#     x: int = 0
#     y: int = 0
#     @classmethod
#     def __add__(self, other):
#         return self.y + other
#
#
# a = Test(1, 5)
# a3 = a + 10
# print(a3)

# @dataclass
# class KgToPounds:
#     "переводим из кг в фунты"
#     __kg: int = 0
#     @classmethod
#     def to_pounds(cls, _kg):
#         print("to_pounds")
#         return cls.__kg * 2.205
#
#     @classmethod
#     def set_kg(cls, value):
#         print("set_kg")
#         cls.__kg = value
#
#
#     @classmethod
#     def get_kg(cls):
#         print("get_kg")
#         return cls.__kg
#     name = property(get_kg, set_kg)
#
# n = KgToPounds(25)
# n.__kg = 50
# print(n.__kg)
# del n.__kg
#



