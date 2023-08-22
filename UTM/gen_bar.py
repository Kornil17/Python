import random
import gen_bar2
from datetime import datetime,timezone


class Bark():
    def barkod(self):
        type = gen_bar2.Generator()
        first = type.first_numbers(3)
        second = type.second_numbers(3)
        third = type.third_numbers(8)
        get_date = str(datetime.now())
        date1 = "".join(get_date[2:8].split("-"))
        date = date1[2:] + date1[:2]
        version = type.versions(3)
        other = type.others(129)
        barks = first + second + third + date + version + other
        return barks



    def get_new(self, number):
        new_bar = list()
        for i in range(number):
            new_bar.append(self.barkod())
        return new_bar



br = Bark()
#print(*br.get_new(4), sep="\n")