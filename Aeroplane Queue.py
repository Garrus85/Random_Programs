""" Airport Simulator"""

import time
import random

class Plane():

    """ Creates the aeroplanes which will land at the airport.
    id - is the flight reference number
    fuel - ow many minutes the plane has left to continue flying """

    def __init__(self, id, fuel):
        self.id = id
        self.fuel = fuel

    def __str__(self):
        return f'Plane {self.id} has {self.fuel} minutes of fuel remaining'

    def plane_id(self):
        return self.id

    def use_fuel(self, time):
        self.fuel -= time

    def get_fuel(self):
        return self.fuel


class Airport():

    """ Te airport which will handle the planes coming in to land.
    landing_queue: ses a queue system to register incoming planes.
    landing_time: how many minutes it takes a plane to land from circling queue
    emergency_runway - kept incase a plane will run out of fuel before their turn to land """

    def __init__(self, name):
        self.name = name
        self.landing_queue = []
        self.emergency_runway = []
        self.landing_time = 7

    def __str__(self):
        return f'{self.name} airport'

    def enqueue(self, plane):
        self.landing_queue.insert(0, plane)

    def dequeue(self):
        landed = self.landing_queue.pop()
        for plane in self.landing_queue:
            plane.use_fuel(self.landing_time)
        return landed

    def landing_queue_size(self):
        return len(self.landing_queue)

    def isEmpty(self):
        return self.landing_queue == []

    def is_critical(self):
        is_critical = False
        self.landing_queue.sort(key=lambda x: x.fuel, reverse=True)
        time_passed = 0
        for plane in self.landing_queue:
            time_passed += self.landing_time
            if plane.get_fuel() < time_passed:
                is_critical = True
        return is_critical

    def emergency(self):
        print("--EMERGENCY--")
        time.sleep(1)
        plane = self.landing_queue.pop()
        self.emergency_runway.append(plane)
        print(f'Plane {plane.id} has landed on the emergency runway!')
        time.sleep(2)

    def emergency_list(self):
        return len(self.emergency_runway)

    def disaster(self):
        pass


def new_arrival(airport):

    """Create an id for a new plane"""

    id_contains = "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
    id = ""
    for _ in range(6):
        idx = random.randint(0, 34)
        character = id_contains[idx]
        id += character

    """Create the planes remaining fuel time before needing to land"""
    fuel = random.randint(5, 50)
    plane_arrived = Plane(id, fuel)
    print(plane_arrived)
    time.sleep(1)
    airport.enqueue(plane_arrived)


def airport_landing(airport):
    """The program mechanics to land planes safely"""

    while airport.isEmpty() == False:
        planes_in_queue = airport.landing_queue_size()
        print(f'There are {planes_in_queue} plane(s) in the queue to land \n')
        time.sleep(2)

        emergency = airport.is_critical()
        if emergency == True:
            airport.emergency()
            if not airport.isEmpty():
                landing_plane = airport.dequeue()
        else:
            landing_plane = airport.dequeue()
        print(f'Plane {landing_plane.plane_id()} has landed')
        time.sleep(2)
        """check if a new plane has arrived at the airport"""
        plane_inbound = random.randint(0, 100)
        if plane_inbound >= 50:
            new_arrival(airport)

    print(f'{airport} landing queue is empty')
    time.sleep(1)
    no_of_emergencies = airport.emergency_list()
    print(f'There was {no_of_emergencies} emergency landings today!')


def main():
    azeroth_airport = Airport("Azeroth")

    for _ in range(1, random.randint(1, 10)):
        new_arrival(azeroth_airport)

    airport_landing(azeroth_airport)


if __name__ == "__main__":
    main()

# Testing
#print(Glasgow.sorted_queue())
#print(Glasgow.is_critical())
#print(Glasgow.landing_queue_size())    PASS
#print(Glasgow.isEmpty())               PASS
#print(Glasgow.dequeue())               PASS
