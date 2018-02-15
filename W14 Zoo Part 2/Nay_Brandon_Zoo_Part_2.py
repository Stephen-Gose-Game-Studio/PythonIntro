###############################################################################
# Brandon Nay
# Zoo Part 1
###############################################################################
# For this assignment, you will add functionality to your Zoo project Part 1
# where you implemented encapsulation and inheritance. In this part of the
# project, you will be implementing the makeNoise function and adding
# polymorphism.
###############################################################################


class Animal:
    def __init__(self, animal_type, age, color, legs):
        self.animal_type = animal_type  # str
        self.age = age                  # int
        self.color = color              # str
        self.legs = legs                # int

    # Override class method to print something readable instead of memory loc
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


###############################################################################


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

# Initialize 2 instances of each subclass into a list
zoo = [Reptile('Snake', 2, 'Orange', 0, True),
       Reptile('Gecko', 12, 'Brown', 4, False),
       Mammal('Bear', 7, 'Black', 4, True),
       Mammal('Deer', 4, 'Amber', 4, False),
       Insect('Spider', 1, 'Black', 8, 0),
       Insect('Dragonfly', 1, 'Green', 6, 4)]

# call __str__ for each object in zoo[]
for x in zoo:
    print(x)
