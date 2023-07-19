import random, string
class Generator():
    def first_numbers(self,n):
        first = ""
        for i in range(n):
            if i == 1:
                first += str(0)
            else:
                first += str(random.randint(3, 9))
        return first
    def second_numbers(self,n):
        second = ""
        for i in range(n):
            second += str(random.randint(0, 9))
        return second

    def third_numbers(self,n):
        third = ""
        for i in range(n):
            third += str(random.randint(0, 9))
        return third

    def versions(self,n):
        version = ""
        for i in range(n):
            version += str(random.randint(1, 9))
        return version


    def others(self,n):
        other = ""
        for i in range(n):
            if i in [14,18,23,25,28,33,35,38,40,48,50,52,53,55,62,64,68,76,78,84,87,91,99,100,101,103,106,107,116,118,120,123,125]:
                other += str(random.randint(1, 9))
            else:
                rand = random.choice(string.ascii_letters)
                other += rand.upper()
        return other

br = Generator()
