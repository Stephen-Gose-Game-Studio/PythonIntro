###############################################################################
# Brandon Nay
# Zoo Part 1
###############################################################################
# For this assignment, you will add functionality to your Zoo project Part 1
# where you implemented encapsulation and inheritance. In this part of the
# project, you will be implementing the makeNoise function and adding
# polymorphism.
#
# Add polymorphism to your parent and child classes (subclasses) by adding
# __str__ functions. The __str__ function should print the parent attributes as
# well as the unique child attributes.
###############################################################################


class Animal:
    def __init__(self, animal_type, sound, age, color, legs):
        self.animal_type = animal_type  # str
        self.sound = sound              # str
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

    # The makeNoise() function of the Animal class will need to be overridden
    # in each subclass. The makeNoise function will need to print the sound the
    # animal makes to the screen.
    def make_noise(self):
        print('--------{}'.format(self.sound))


###############################################################################


class Reptile(Animal):
    def __init__(self, animal_type, sound, age, color, legs, scales):
        super().__init__(animal_type, sound, age, color, legs)
        self.scales = scales

    def __str__(self):
        return super().__str__() + "SCALES:    {}".format(self.scales)


class Mammal(Animal):
    def __init__(self, animal_type, sound, age, color, legs, hibernate):
        super().__init__(animal_type, sound, age, color, legs)
        self.hibernate = hibernate

    def __str__(self):
        return super().__str__() + "HIBERNATE: {}".format(self.hibernate)


class Insect(Animal):
    def __init__(self, animal_type, sound, age, color, legs, wings):
        super().__init__(animal_type, sound, age, color, legs)
        self.wings = wings

    def __str__(self):
        return super().__str__() + "WINGS:     {}".format(self.wings)


###############################################################################

# All instantiated Animal objects should be stored in the Zoo list.
zoo = [Reptile('Snake', 'Hisss', 2, 'Orange', 0, True),
       Reptile('Gecko', '*Licking Noise*', 12, 'Brown', 4, False),
       Mammal('Bear', "GRRR I'm a bear", 7, 'Black', 4, True),
       Mammal('Deer', 'HONK', 4, 'Amber', 4, False),
       Insect('Spider', '*Tap Dancing*', 1, 'Black', 8, 0),
       Insect('Dragonfly', 'Buzz Buzz', 1, 'Green', 6, 4)]

# Traverse the Zoo list using a loop and have each animal polymorphically print
# its attributes and call the makeNoise function.
for x in zoo:
    print(x)
    x.make_noise()
