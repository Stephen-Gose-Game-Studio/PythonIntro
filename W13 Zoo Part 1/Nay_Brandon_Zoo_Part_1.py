###############################################################################
# Brandon Nay
# Zoo Part 1
###############################################################################


class Animal:
    def __init__(self, animal_type, age, color, legs):
        self.animal_type = animal_type
        self.age = age
        self.color = color
        self.legs = legs

    def __str__(self):
        return "\nANIMAL:    {}\n" \
               "AGE:       {}\n" \
               "COLOR:     {}\n" \
               "LEGS:      {}\n".format(self.animal_type,
                                        self.age,
                                        self.color,
                                        self.legs)

    def make_noise(self):
        pass


'''Subclasses'''


class Reptile(Animal):
    def __init__(self, animal_type, age, color, legs, scales):
        super().__init__(animal_type, age, color, legs)
        self.scales = scales

    def __str__(self):
        return super().__str__() + "SCALES:    {}".format(self.scales)


class Mammal(Animal):
    def __init__(self, animal_type, age, color, legs, hibernate):
        super().__init__(animal_type, age, color, legs)
        self.hibernate = hibernate

    def __str__(self):
        return super().__str__() + "HIBERNATE: {}".format(self.hibernate)


class Insect(Animal):
    def __init__(self, animal_type, age, color, legs, wings):
        super().__init__(animal_type, age, color, legs)
        self.wings = wings

    def __str__(self):
        return super().__str__() + "WINGS:     {}".format(self.wings)


###############################################################################

zoo = [Reptile('Snake', 2, 'Orange', 0, True),
       Reptile('Gecko', 12, 'Brown', 4, False),
       Mammal('Bear', 7, 'Black', 4, True),
       Mammal('Deer', 4, 'Amber', 4, False),
       Insect('Spider', 1, 'Black', 8, 0),
       Insect('Dragonfly', 1, 'Green', 6, 4)]

for x in zoo:
    print(x)
