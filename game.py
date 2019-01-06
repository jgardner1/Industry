#!/usr/bin/env python

class Game(object):

    def __init__(self):
        self.clock = Clock()
        self.objects = set()

    def tick(self):
        # Tick the clock first.
        self.clock.tick()

        # Tick all the objects in the universe
        for obj in self.objects:
            obj.tick(self.clock)

class Clock(object):

    def __init__(self):
        self.ticks = 0

    def tick(self):
        # Each tick represents one minute.
        self.ticks += 1
    
class Person(object):

    def __init__(self, name, birthdate, sex):
        self.name = name
        self.birthdate = birthdate
        self.sex = sex

    def tick(self, clock):
        pass
