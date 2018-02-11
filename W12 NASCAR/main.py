###############################################################################
# Brandon Nay
# NASCAR
###############################################################################

from random import randint


###############################################################################
# Define a class called Car with the following attributes:
#
# Total Odometer Miles
# Speed in miles per hour
# Driver Name
# Sponsor
# The total odometer miles and speed should be initialized to zero.
###############################################################################
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

        self.avg_speed = (self.avg_speed + self.speed) / 2

###############################################################################


# Create a list of 20 unique vehicles with random driver and sponsor names.
def register_drivers():
    driver_list = []
    for x in Drivers:   # x grabs the key, not the value
        # create an obj of class Car with attributes from x and add to list
        driver_list.append(Car(x, Drivers[x]))  # (key, value)->(name, sponsor)
    return driver_list


###############################################################################
# Your main program should simulate the progress of the vehicles in the race.
# Every simulated minute, the vehicles pick a new random speed between 1 and
# 120, and their odometer miles are updated every minute using this equation:
#
# odometer_miles = odometer_miles + speed * time
# Since speed is in miles per hour, time should be in hours as well
# (1 minute is 1/60th of an hour).
#
# The first car to reach 500 miles should be declared the winner by printing
# the driver name and sponsor name.
###############################################################################
def main():
    race_participants = register_drivers()
    lead_driver = Car('joe', 'dirt')   # initial placeholder object
    winner = False
    minutes = 0

    # Begin the race
    while True:
        for x in race_participants:
            x.update_speed()
            if x.odometer >= 500:
                print('\n\n', x.driver_name, 'wins with an average speed of',
                      format(x.avg_speed, '.1f'), 'MPH.\n',
                      'SPONSOR:', x.sponsor)
                winner = 'True'
                break
            elif x.odometer > lead_driver.odometer:
                lead_driver = x    # new driver takes the lead
                continue
            else:
                continue

        minutes += 1

        if winner == 'True':
            break
        else:
            print('Minute', minutes, 'complete!\n',
                  lead_driver.driver_name, 'is in the lead!\n')

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
