import random
import weakref


# One tick is one day
DAY = 1
MONTH = 28
MONTHS_PER_YEAR = 13
YEAR = 364

class Person(object):
    """
    age (int): age in ticks
    """

    def __init__(self, town, name, sex, birthday):
        self.alive = True
        self.town = weakref.proxy(town)
        self.name = name
        self.sex = sex
        self.birthday = birthday

    @property
    def pronoun_nom(self):
        """Returns the nominative pronoun"""
        return {
                'M': 'he',
                'F': 'she',
                }.get(self.sex, 'it')
    @property
    def pronoun_acc(self):
        """Returns the accusative pronoun"""
        return {
                'M': 'him',
                'F': 'her',
                }.get(self.sex, 'it')

    @property
    def pronoun_poss_adj(self):
        """Returns the accusative pronoun"""
        return {
                'M': 'his',
                'F': 'her',
                }.get(self.sex, 'its')

    @property
    def pronoun_poss(self):
        """Returns the accusative pronoun"""
        return {
                'M': 'his',
                'F': 'hers',
                }.get(self.sex, 'its')

    @property
    def pronoun_reflex(self):
        """Returns the reflexive or intensive pronoun"""
        return {
                'M': 'himself',
                'F': 'herself',
                }.get(self.sex, 'itself')

    def tick(self, date):
        if (date - self.birthday)%YEAR == 0:
            print("{} is having a birthday! {} is now {} years old".format(
                self.name, self.pronoun_nom.capitalize(), (date-self.birthday)/YEAR))

        pass


class Town(object):
    """A Town has Person objects. A Town has resources. A Town has material
    and manufactured goods."""

    def __init__(self):
        self.people = set()
        self.date = 0

        # Adam and Eve
        self.people.add(Person(self, 'Adam', 'M', self.date - YEAR*20))
        self.people.add(Person(self, 'Eve', 'F', self.date - YEAR*20))

    def tick(self):
        # Each tick is one day
        self.date += 1
        for person in self.people:
            person.tick(self.date)

town = Town()
