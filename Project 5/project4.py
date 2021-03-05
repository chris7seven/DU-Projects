# Christopher Seven
# This project constructs a dice game between the user and the computer. The user picks how many dice, and the number of sides of the dice. As well, the user can bet money on each round.
# The game ends when the player cashes out or their money reaches 0/
import random

# Constructing the dice class.
class dice:
    def __init__(self, sides):
        self.sides = sides
        self.dicevalue = self.roll()
        self.value = 0

    # The dice is rolled, and then the value is stored for the comparisons.
    def roll(self):
        self.value = random.randint(1, self.sides)
        return self.value

    # The following are the magic comparison operators.
    def __str__(self):
        return str(self.dicevalue)

    def __eq__(self, other):
        return self.sides == other.sides

    def __ne__(self, other):
        return self.dicevalue != other.dicevalue

    def __lt__(self, other):
        return self.dicevalue < other.dicevalue

    def __gt__(self, other):
        return self.dicevalue > other.dicevalue

    def __le__(self, other):
        return self.dicevalue <= other.dicevalue

    def __ge__(self, other):
        return self.dicevalue >= other.dicevalue

    def __add__(self, other):
        return self.dicevalue + other.dicevalue

# The class for the cupofdice, which holds the total dice for each player.
class cupofdice:
    # Constructing a list of dice by appending the dice.
    def __init__(self, numdice, sides):
        self.listdice=[]
        self.numdice = numdice
        self.sides = sides
        self.sum = 0
        for i in range(0, self.numdice):
            self.listdice.append(dice(sides))

    # Where the dice are rolled, and their sum is computed. This ensures that the dice can be rolled multiple times.
    def cuproll(self):
        for die in self.listdice:
            die.roll()
            self.sum += die.value
        return self.sum

    # Printing out the dice for each player.
    def __str__(self):
        s = "Dice: "
        for dice in self.listdice:
            s += f'{dice} '
        s += "Sum: "
        s += str(self.sum)
        return s

    # Magic comparison methods.
    def __eq__(self, other):
        return self.sum == other.sum

    def __ne__(self, other):
        return self.sum != other.sum

    def __gt__(self, other):
        if self.sum > other.sum:
            return True

    def __lt__(self, other):
        if self.sum < other.sum:
            return True

    def __le__(self, other):
        return self.sum <= other.sum

    def __ge__(self, other):
        return self.sum >= other.sum


def main():
    # Starting cash is $100.
    cash = 100
    print("Welcome to a dice game.")
    numdice = int(input("How many dice would you like to roll?"))
    numsides = int(input("How many sides would you like the dice to have?"))
    # Establishing the cashout value before using it in the while loop.
    cashout = None
    # The loop runs until the player says yes to cashing out or runs out of money.
    while cashout != "y" or cash <= 0:
        bet = int(input("How much would you like to bet?"))
        # Establishing the player and computer dice, then rolling them.
        playerdice = cupofdice(numdice, numsides)
        playerdice.cuproll()
        computerdice = cupofdice(numdice, numsides)
        computerdice.cuproll()

        # Printing out player and computer dice.
        print("You rolled: ")
        print(playerdice)
        print("The computer rolled: ")
        print(computerdice)

        # Using the magic comparison operator in order to determine who wins.
        if playerdice > computerdice:
            print("You won! :)")
            cash += bet
        elif playerdice < computerdice:
            print("You lost. :(")
            cash -= bet
        else:
            print("You tied. Your bet has been refunded.")
        print("Your new cash amount is " + str(cash))
        cashout = input("Would you like to cash out? (y/n)")
    print("Game over. Your final cash amount was " + str(cash))
main()
