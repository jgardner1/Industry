import random
import weakref


# One tick is one day
DAY = 1
MONTH = 28
MONTHS_PER_YEAR = 13
YEAR = 364

class Noun(object):
    """Has some functions for determining pronouns and such."""

    def __init__(self, sex):
        self.sex = sex

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


class Person(Noun):
    """
    age (int): age in years
    """

    def __init__(self, town, name, sex, birthday):
        Noun.__init__(self, sex)
        self.alive = True
        self.town = town
        self.name = name
        self.birthday = birthday
        self.age = (self.town.date - self.birthday)//YEAR
        self.pregnant = False
        self.due_date = None


    def tick(self, date):
        if (date - self.birthday)%YEAR == 0:
            self.age = (date - self.birthday)//YEAR
            print("{} is having a birthday! {} is now {} years old".format(
                self.name, self.pronoun_nom.capitalize(), self.age))

        if self.sex == 'F':
            if self.pregnant:
                if date >= self.due_date:
                    print("A new baby is born!")
                    self.pregnant = False
                    self.due_date = None

                    self.town.people.append(Person(
                        town=self.town,
                        name="Baby",
                        sex=random.choice(['M', 'F']),
                        birthday=date))
            else:
                if 14 <= self.age <= 45 and random.random() < 1.0/YEAR:
                    # Due 37-41 weeks from today
                    self.pregnant = True
                    self.due_date = date + int(0.5 + (37 +
                        random.random()*4)*7)
                    print("{} has become pregnant! Due on {}".format(self.name, self.due_date))



class Town(Noun):
    """A Town has Person objects. A Town has resources. A Town has material
    and manufactured goods."""

    def __init__(self, name):
        Noun.__init__(self, 'N')
        self.name = name
        self.people = []
        self.date = 0

        # Adam and Eve
        self.people.append(Person(weakref.proxy(self), 'Adam', 'M', self.date - YEAR*20))
        self.people.append(Person(weakref.proxy(self), 'Eve', 'F', self.date - YEAR*20))

    def tick(self):
        # Each tick is one day
        self.date += 1
        for person in self.people:
            person.tick(self.date)

town = Town('Beginning')

def run_town():
    import time
    while True:
        town.tick()
        time.sleep(0.01)

