# class MROHelper:
#     @staticmethod
#     def len(cls):
#         return len(cls.mro())
#     @staticmethod
#     def class_by_index(cls, n=0):
#         return cls.mro()[n]
#     @staticmethod
#     def index_by_class(child, parent):
#         for i in enumerate(child.mro()):
#             if i[1] == parent:
#                 return i[0]
from datetime import datetime
class USADate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day



