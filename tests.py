# class Currency:
#     def __init__(self, value_number, value_name):
#         self.value_number = value_number
#         self.value_name = value_name
#         self.course = {'RUB':90, 'USD':1.1, 'EUR':1}
#     def __str__(self):
#         return f"{self.value_number} {self.value_name}"
#     def change_to(self, name):
#         if name == 'EUR':
#             self.value_number = float(self.value_number / self.course[self.value_name])
#         else:
#             self.value_number = self.value_number * self.course[name]
#         self.value_name = name
#     def get_result(self, other, action):
#         if action == '+':
#             course = float(self.value_number / self.course[self.value_name]) + float(other.value_number / self.course[other.value_name])
#             result = course * self.course[self.value_name]
#             return result
#         elif action == '-':
#             course = float(self.value_number / self.course[self.value_name]) - float(other.value_number / self.course[other.value_name])
#             result = course * self.course[self.value_name]
#             return result
#         elif action == '*':
#             course = float(self.value_number / self.course[self.value_name]) * float(
#                 other.value_number / self.course[other.value_name])
#             result = course * self.course[self.value_name]
#             return result
#         elif action == '/':
#             course = float(self.value_number / self.course[self.value_name]) / float(
#                 other.value_number / self.course[other.value_name])
#             result = course * self.course[self.value_name]
#             return result
#
#     def __add__(self, other):
#         if self.value_name == other.value_name:
#             return Currency(self.value_number + other.value_number, other.value_name)
#         else:
#             return Currency(self.get_result(other, '+'), self.value_name)
#     def __sub__(self, other):
#         if self.value_name == other.value_name:
#             return Currency(self.value_number - other.value_number, other.value_name)
#         else:
#             return Currency(self.get_result(other, '-'), self.value_name)
#     def __mul__(self, other):
#         if self.value_name == other.value_name:
#             return Currency(self.value_number - other.value_number, other.value_name)
#         else:
#             return Currency(self.get_result(other, '*'), self.value_name)
#     def __truediv__(self, other):
#         if self.value_name == other.value_name:
#             return Currency(self.value_number - other.value_number, other.value_name)
#         else:
#             return Currency(self.get_result(other, '/'), self.value_name)
#
# print(Currency(5, 'EUR') + Currency(5, 'EUR'))
# print(Currency(11, 'USD') - Currency(5, 'EUR'))
# print(Currency(5, 'RUB') * Currency(11, 'USD'))
# print(Currency(5, 'USD') / Currency(5, 'EUR'))


# n = bin(5)
# print(sorted(list(map(lambda x: int(x), list(n[2:])))))
# print(input()[::-1][:-1])

from typing import Union, Optional, Any


def choose_plural(amount: Optional[int], declensions: Optional[tuple[str, str, str]]) -> Optional[str]:
    if s >= 0:
        if s == 0:
        print(str(s) + n1)

elif s % 100 >= 10 and s % 100 <= 20:
print(str(s) + n1)
elif s % 10 == 1:
print(str(s) + n2)
elif s % 10 >= 2 and s % 10 <= 4:
print(str(s) + n3)
else:
print(str(s) + n1)
