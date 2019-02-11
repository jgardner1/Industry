# Design

## Key Features

The player dictates, to some degree, the activities of individuals. These
individuals may or may not comply with the actions proscribed. Generally, they
act independently.

The individuals engage in various behaviors based on their needs. They may
consume goods they have access to or create more. They may buy and sell from
the marketplace.

The economy is extraordinarily complex. There are thousands of components that
go into making anything of decent complexity, and the people will have to
build an economy just to build basic things we take for granted.

## Data Structures

### Person

A person is an individual. They have a name, relationships with other
individuals (family, friend, enemy, etc...) and have various attributes and
skills. They also have needs.

People will try to obtain and satisfy their most immediate needs. When those
are satisfied, they will try to obtain some measure of security for the
future. They will then try to obtain the necessary goods for their loved ones.


Attributes (tend not to change):

* Name
* Birthdate
* Physical Strength (-10 to +10)
* Intellectual Strength
* Emotional Strength
* Relationship Strength

Personality Traits: Affects preferences. Much like the sims, people can have a
few personality traits. Unlike the sims, they can only have 1 or 2 and rarely
3.

Skills: One for each activity, individuals can get more experience with an
activity and get good at it. Or they can be trained or read books or think
about it and get good at it. Combining all of these together leads to the
greatest gains. Skills also have an influene on each other when they are
related. These are generally grouped together so the total skill is the group
skill plus the specialized skill. IE, if I have a 50 in machining, then 20 in
tapping, then my total tapping skill, which is part of machining, is 70. Each
skill is rated 0 to 100, and cannot exceed 100. If a skill is part of a group,
then it will borrow only a certain percentage from that group. IE, in the case
above, if tapping is 70% machining, then the total score is (50*0.7)+20*(0.3)
= 35 + 6 = 41.

State values:
* Health: (0 to 100). 0 is dead, 100 is healthy.
* Energy: (0 to 100). 0 Means they have no energy and must sleep. 100 means
  they are awak.
* Mood: (0 to 100) 0 means depressed and suicidal. 100 means happy.
* Hunger: (0 to 100) 0 is starving, 100 is full.
* Thirst: (0 to 100) 0 is dehydrated, 100 is well-watered.
* Socialization: (0 to 100) 0 is lonely, 100 is surrounded by friends and
  family.

Inventory: What they are carrying on them. They will accumulate things they
can't carry in their local workspace or load them into the machine they are using if it's too much.

Effects: Various conditions that may be long lasting, typically diseases or
such.

### Plan

People have plans. This is a strategy of activities with simple rules. These
rules may be simply "eat some food if hungry." These activities are
prioritized. People will change their plans, either adopting plans that seem
to work well for others or finding new ones.

### Time

Time flows in one hour increments. Each hour, people choose to do an activity,
briefly chosen. Occasionally, an individual will spend time thinking, when
they can make more serious plans.

### Activity

An activity is something an individual might be doing. There is typically
input goods, output goods, and some change in the individual's state.

### Job

Persons can hire each other. They exchange something else for their labor.
They write up labor contracts, and they break them when they no longer want to
fulfill them.

## Technology

Some things are unlocked when the economy is able to satisfy the inputs
necessary. Some things are unlocked only when there are skilled enough people
to do it. There is no separate research activity, just people trying to
develop their skills.

That said, there is a "science" skill, which has several categories. When
unlocked, this allow people unskilled to learn a skill and thus teach it to
others.
