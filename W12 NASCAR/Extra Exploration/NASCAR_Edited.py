import csv
from random import randint


class Car:
    def __init__(self, driver_name, sponsor):
        self.odometer = 0
        self.speed = 0
        self.driver_name = driver_name
        self.sponsor = sponsor
        self.avg_speed = []

    def update_speed(self):
        # Every simulated minute, the vehicles pick
        # a new random speed between 1 and 120
        self.speed = randint(1, 120)
        self.avg_speed.append(self.speed)   # add each speed to list

        # and their odometer miles are
        # updated using this equation:
        self.odometer += self.speed / 60

    # average calculation fix: instead of calculating a running average, add
    # every speed to a list (above) and run this function when win condition is
    # met.
    def get_avg_speed(self):
        return sum(self.avg_speed) / len(self.avg_speed)


###############################################################################


# Create a list of 20 unique vehicles with random driver and sponsor names.
def register_drivers():
    driver_list = []
    for x in Drivers:  # x grabs the key, not the value
        # create an obj of class Car with attributes from x and add to list
        driver_list.append(Car(x, Drivers[x]))  # (key, value)->(name, sponsor)
    return driver_list


def main():
    with open('data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        race_participants = register_drivers()
        races = 0

        while races < 1001:
            minutes = 0

            # Begin the race
            while races < 1001:

                for x in race_participants:
                    x.update_speed()
                    if x.odometer >= 500:
                        print(races)
                        print('\n\n', x.driver_name, 'wins')
                        writer.writerow([minutes, x.get_avg_speed()])
                        minutes = 0
                        races += 1
                        race_participants = register_drivers()
                        break
                    else:
                        continue

                minutes += 1

###############################################################################


Drivers = {'AJ Allmendinger': 'Kroger',
           'Alex Bowman': 'Nationwide Insurance',
           'Aric Almirola': 'Smithfield Foods',
           'Austin Dillon': 'Dow Chemicals',
           'BJ McLiod': 'Rick Ware Racing',
           'Brendan Gaughan': 'Beard Oil',
           'Chase Elliot': 'Napa Auto Parts',
           'Clint Bowyer': 'Mobil 1',
           'Daniel Kennington': 'Lordco Auto Parts',
           'Darrel Wallace JR': 'Click n Close',
           'David Ragan': 'Camping World',
           'Erik Jones': 'DeWalt',
           'Jeffrey Earnhardt': 'VRX Simulations',
           'Joey Gase': 'Best Home Furnishings',
           'Kasey Kahne': 'K-LOVE Radio',
           'Kyle Weatherman': 'Rick Ware Racing',
           'Matt Dibenedetto': 'Can-Am',
           'Paul Menard': 'Menards',
           'Ryan Newman': 'Caterpillar',
           'William Byron': 'Axalta'}

main()  # execute
