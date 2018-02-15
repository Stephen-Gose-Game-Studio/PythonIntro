###############################################################################
# Brandon Nay
# Zoo Part 1
###############################################################################


class Animal:
    def __init__(self, animal_type, age, color, legs):
        self.animal_type = ''
        self.age = 0
        self.color = ''
        self.legs = 0

    def __str__(self):
        print(self.animal_type)
        print(self.age)
        print(self.color)
        print(self.legs)
