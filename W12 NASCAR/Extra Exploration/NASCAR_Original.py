import csv
from random import randint


class Car:
    def __init__(self, driver_name, sponsor):
        self.odometer = 0
        self.speed = 0
        self.driver_name = driver_name
        self.sponsor = sponsor
        self.avg_speed = 0

    def update_speed(self):
        # Every simulated minute, the vehicles pick
        # a new random speed between 1 and 120
        self.speed = randint(1, 120)

        # and their odometer miles are
        # updated using this equation:
        self.odometer += self.speed / 60

        # suspected problem; inaccurate average calculation over time
        #####################################################
        self.avg_speed = (self.avg_speed + self.speed) / 2  #
        #####################################################

###############################################################################


# Create a list of 20 unique vehicles with random driver and sponsor names.
def register_drivers():
    driver_list = []
    for x in Drivers:  # x grabs the key, not the value
        # create an obj of class Car with attributes from x and add to list
        driver_list.append(Car(x, Drivers[x]))  # (key, value)->(name, sponsor)
    return driver_list


def main():
    # create file to write data to
    with open('data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        race_participants = register_drivers()
        races = 0

        # run 1000 race simulations
        while races < 1000:
            minutes = 0

            # Begin the race
            while races < 1000:

                for x in race_participants:
                    x.update_speed()
                    if x.odometer >= 500:   # win condition
                        print(races)
                        print('\n\n', x.driver_name, 'wins with an avg speed',
                              format(x.avg_speed, '.1f'), 'MPH.\n',
                              'SPONSOR:', x.sponsor)

                        # write time and average speed to csv
                        writer.writerow([minutes, x.avg_speed])

                        # reset time and increment races
                        minutes = 0
                        races += 1

                        # rerun register_drivers() to reset instance variables
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
