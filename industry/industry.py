#!/usr/bin/env python3

import random
import math
import weakref

from pprint import pprint

ONE_MINUTE_IN_SECONDS = 60.0
ONE_HOUR_IN_SECONDS = 60.0 * ONE_MINUTE_IN_SECONDS
ONE_DAY_IN_SECONDS = 24.0 * ONE_HOUR_IN_SECONDS
ONE_WEEK_IN_SECONDS = 7.0 * ONE_DAY_IN_SECONDS
ONE_YEAR_IN_SECONDS = 365.0 * ONE_DAY_IN_SECONDS

seconds_per_tick = ONE_DAY_IN_SECONDS

def normal_distribution(x, mu, sigma):
    """Returns the value of the normal distribution at x with average mu and
    std.  dev. of sigma. This is not scaled so that the maximum will be 1.0."""
    return math.exp(-0.5*((x-mu)/sigma)**2)


# See the Life Expectancy google doc.
# This is your chance of dying each year. It is a table. Your life is rolled
# at the birth. It may be modified by life expectancy modifiers.


class Person(object):
    """
    alive (bool): Whether the person is still alive.
    age (int): How old the person is in ticks.
    death_age (int): When the person will die in ticks.
    sex ('M' or 'F'): male or female
    name (str): Name

    job (str): The job of the Person. Should match a job in the job table.

    For females only:
    pregnant (bool): Whether the Person is pregnant
    birth_age (bool): At what age the baby will be born. (None if
        miscarriage_age.)
    miscarriage_age (bool): At what age the baby will miscarry.


    """

    miscarriage_rate = 0.24

    mortality_rate = (
        (0, 10.00),
        (54, 1.50),
        (64, 3.00),
        (74, 4.00),
        (84, 5.00),
        (94, 10.00),
        (109, 20.00),
        (110, 100.00),
    )

    # (% chance, age)
    mortality_table = [ ]
    last_age = 0
    cum_chance = 0
    for age, chance in mortality_rate:
        chance = chance/100.0
        while last_age <= age:
            mortality_table.append(
               (last_age, cum_chance + chance*(1-cum_chance)))
            cum_chance = mortality_table[-1][1]

            last_age += 1
    del age
    del last_age
    del cum_chance

    def __init__(self, age=0.0, sex='M', town=None):
        self.alive = True
        self.pregnant = False
        self.sex = sex
        self.name = {
            'M':'Adam',
            'F':'Eve',
        }[self.sex]
        self.age = 0.0 # Years

        # Roll their death.
        r = random.random()
        for age, cum_chance in self.mortality_table:
            if cum_chance >= r:
                break

        self.death_age = age + random.random()
        print("{} will die at age {}".format(self.name, self.death_age))
        self.life_expectancy = 1.0
        self.job = 'forage'
        self.pregnant_days = -1
        self.inventory = {}
        self.town = weakref.proxy(town)

    def do_forage(self):
        pass

    def get_pregnant(self):
        """Impregnates the person, determining whether it will be a
        miscarriage and what date that will occur, or whether it will be
        carried to term and what date that will occur."""
        if random.random() < self.miscarriage_rate:
            print("It will be a miscarriage, unfortunately.")
            r = random.random()
            if r < 0.50:
                weeks = 4.0 + random.random()*1.0
            elif r < 0.60:
                weeks = 5.0 + random.random()*1.0
            elif r < 0.70:
                weeks = 6.0 + random.random()*2.0
            else:
                weeks = 8.0 + random.random()*4.0
            self.miscarriage_age = self.age + \
                weeks*ONE_WEEK_IN_SECONDS/ONE_YEAR_IN_SECONDS
            self.delivery_age = None

        else:
            print("It will not be a miscarriage, luckily!")
            self.miscarriage_age = None
            self.delivery_age = self.age + random.gauss(39, 1)* \
                ONE_WEEK_IN_SECONDS/ONE_YEAR_IN_SECONDS

    def conception_rate(self):
        """The likelihood of getting pregnant."""
        # This is the birth_rate/miscarriage_rate.
        return self.birth_rate()/(1-self.miscarriage_rate)

    def birth_rate(self):
        """Returns the chance of having a baby that year."""
        if self.age < 12.0 or self.age > 50.0:
            return 0.0

        # The birth rate at age 30 is 50%. It goes down from there, spread out
        # with std. dev. of 5 years.
        return normal_distribution(self.age, 30.0, 5.0)*0.50

    def die(self):
        print("{} has died at age {}".format(
            self.name, math.floor(self.age)))
        self.alive = False

    def tick(self):
        if not self.alive:
            pass

        self.age += tick_length/ONE_YEAR_IN_SECONDS

        if self.job == 'forage':
            self.do_forage()

        # Share surplus with tribe?

        # Do you get pregnant?
        if self.sex == 'F':
            if self.pregnant:
                self.pregnant_days += 1
                if self.miscarriage_age is not None:
                    if self.age >= self.miscarriage_age:
                        print("There was a miscarriage.")
                        self.pregnant = False
                        self.miscarriage_age = None
                        self.delivery_age = None
                elif self.delivery_age is not None:
                    if self.age >= self.delivery_age:
                        print("A new baby is born!")
                        if random.random() < 0.51:
                            sex = 'M'
                        else:
                            sex = 'F'
                        self.town.population.add(Person(
                            age=0,
                            sex=sex,
                            town=self.town))

            elif random.random() < self.conception_rate()/365.0:
                print("A woman conceived")
                self.get_pregnant()

        # Do I die?
        if self.age >= self.death_age * self.life_expectancy:
            self.die()
    

class Town(object):

    def __init__(self):
        self.population = set([
            Person(age=20, sex='F', town=self),
            Person(age=20, sex='M', town=self),
        ])
        self.food = 0.0

        self.assignments = {
            'forage':1.0,
        }

    def tick(self):
        for person in self.population:
            person.tick()

        self.population = {
            person
            for person in self.population
            if not person.dead}
        
t = Town()
