#Christopher Seven
#Project 3

import random

#The card game that will be implemented is blackjack. The player will be playing against a dealer, and will be able to decide to hit or stay
#Since the game is blackjack, the suits of each card will not be kept track of, as they will not be used

#A deal function is necessary to pull random cards from the deck to simulate 'dealing' in a casino
def deal(deck):
    #This is a reference from hand to an empty list
    hand = []
    #The deck is shuffled.
    random.shuffle(deck)
    for i in range(0, 2):
        #Here is a reference from card to the last element in list 'deck'
        card = deck.pop()
        hand.append(card)
    return hand

#This function simulatees the act of a dealer "hitting" the hand of the player, by adding an additional card to the player's hand
def hit(hand, deck):
    #Once again, a reference from card to the last element in the list 'deck'
    card = deck.pop()
    hand.append(card)
    return hand

#A function that tallies up the score of a hand to determine if it is winning or not
def score(hand):
    #Reference from score to 0
    score = 0
    #Loop through each card in the hand and assign it a score, which is added to variable score
    for card in hand:
        if card == "J":
            score += 10
        elif card == "Q":
            score += 10
        elif card == "K":
            score += 10
        elif card != "A":
            score += card
        # We want the Ace to be evaluated last, since it has 2 values dependent on the total score
        elif card == "A":
            if score > 10:
                score += 1
            elif score <= 10:
                score += 11
    #The ace must be evaluated again in case the total score goes over 21, and the ace is the first card in the hand
    if "A" in hand and score > 21:
        #Self reference, score points to its own value minus 10
        score = score - 10
    return score

#This function will be used to determine if the player or dealer has struck blackjack in the first 2 cards
def blackjack(playerhand, dealerhand):
    if score(playerhand) == 21:
        print("Blackjack! You win.The dealer's cards were " + str(dealerhand))
        exit()
    if score(dealerhand) == 21:
        print("Blackjack! The dealer wins. The dealer's cards were " + str(dealerhand))
        exit()

#This function determines whether the dealer or player won the match. Multiple cases are included for ties
def winner(playerhand, dealerhand):
    if score(playerhand) == 21 and score(dealerhand) == 21:
        print("Double blackjack! You tie the dealer.")
    elif score(playerhand) == 21:
        print("Blackjack! You win.")
    elif score(dealerhand) == 21:
        print("Blackjack! The dealer wins.")
    elif score(playerhand) > 21 and score(dealerhand) > 21:
        print("You both busted. Unfortunately, the dealer wins.")
    elif score(playerhand) > 21:
        print("You busted. Game over.")
    elif score(dealerhand) > 21:
        print("The dealer busted. You win.")
    elif score(dealerhand) < score(playerhand):
        print("You win!")
    elif score(dealerhand) > score(playerhand):
        print("You lose.")
    elif score(playerhand) == score(dealerhand):
        print("Tie game.")

#This is where the code is actually executed, and the other functions are pulled in
def main():
    #Reference from vals to all possible card values in a deck
    vals = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    #Deck would be considered a deep copy of vals, since changing a element of deck or vals would not modify the other
    deck = vals * 4

    print("Take a seat at the table. Blackjack has now begun.")

    #Reference from dealerhand to 2 cards from the deck
    dealerhand = deal(deck)
    #Reference from playerhand to 2 cards from the deck.
    playerhand = deal(deck)

    print("The dealer's faceup card is " + str(dealerhand[1]))
    print("Your hand is " + str(playerhand))
    blackjack(playerhand, dealerhand)
    #Reference from choice to user input of h or s
    choice = input("Would you like to hit or stay?(h/s)")
    #While the player chooses to keep hitting, they will loop until they choose to stay
    while choice == "h":
        hit(playerhand, deck)
        print("Hit! Your new card is " + str(playerhand[-1]))
        print("Your hand is " + str(playerhand))
        #Same reference as before
        choice = input("Would you like to hit or stay?(h/s)")
    #The dealer will always hit below a score of 17
    while score(dealerhand) < 17:
        print("The dealer hits, adding a card to his hand.")
        hit(dealerhand, deck)

    print("Your hand is " + str(playerhand) + " and your score is " + str(score(playerhand)))
    print("The dealer's hand is " + str(dealerhand) + " and his score is " + str(score(dealerhand)))
    winner(playerhand, dealerhand)

main()
