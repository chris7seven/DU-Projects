# Christopher Seven
# Python software development Project 5 part 2
import itertools
import numpy

# Establishing a list for the suits and the for the values
suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

# Creating an empty list for the deck
deck = []
# Looping through 4 times, this for loop could be as simple as for i in range(0, 4) with same functionality
for i in suits:
    # By using two for loops, we ensure that deck is appending each value in the zipped list, instead of the list of tuples. This way deck will only have tuples in it.
    for n in (list(zip(values, itertools.cycle(suits)))):
        deck.append(n)
    # By using numpy.roll, we essentially rotate the suits list and ensure that there won't be duplicate values in our deck.
    suits = numpy.roll(suits, 1)
print(deck)
