import deck
import random
import time


def deal(my_deck):
    card1 = deck.deal_card(my_deck)
    card2 = deck.deal_card(my_deck)
    card3 = deck.deal_card(my_deck)
    card4 = deck.deal_card(my_deck)
    player_hand = [card1,card3]
    dealer_hand = [card2,card4]
    return player_hand, dealer_hand
    """
    This function should receive a list representing the deck of cards as the input
    It should create two seperate lists representing the hand of player and dealer
    It should list the player hand and the showing card of the dealer hand
    It should return both lists
    """
    
hand1,hand2 = deal(deck.my_deck)

def hand_value(hand):
    value = 0
    ace_counter = 0
    for card in hand:
        if card in ['J','Q','K']:
            value = value + 10
        elif card =='A':
            value = value + 11
            ace_counter = ace_counter + 1
        else:
            value = value + card
    while value > 21 and ace_counter > 0:
        value = value - 10
        ace_counter -= 1
    return value

player_hand_value = hand_value(hand1)
dealer_hand_value = hand_value(hand2)

print(f"Your hand : {hand1} - {player_hand_value}")
print(f"Dealer's hand : {hand2} - {dealer_hand_value}")

"""
    This function should receive a list representing a hand
    It should return value of the hand as an integer.
    - (2 - 10) are worth their presented value
    - J, Q, K are worth 10
    - A is worth 11, but drops to 1 if the hand is over 21
    """
    


def hit(my_deck, hand):
    hit_card = deck.deal_card(my_deck)
    hand.append(hit_card)
    value = hand_value(hand)
    print(f"Your new card is {hit_card}")
    print(f"New hand is {hand} - {value}")
    if value > 21:
        print("Bust !")
        return True
    else:
        return False
    """
    Receives 2 lists as inputs
    - The first list represents the deck of cards
    - The second represents a hand
    The function should take an item from the deck and add it to the hand
    It should use the hand_value() function to check if the the hand busted (went over 21)
    It should display the new hand value
    It should return a boolean value indicating if the hand busted.
    """
    


def get_action():
    user_action = input("Do you want to hit or stay?")
    while user_action != "hit" and user_action != "stay":
        print(f"{user_action} is an invalid input")
        user_action = input("Do you want to hit or stay?")
    return user_action
    """
    This function shoudl prompt the user to hit or stay.
    We can add an input validation loop to make sure a valid choice was provided
    We should return "hit" or "stay"
    """
    


def dealer_action(my_deck, dealer_hand):
    while hand_value(dealer_hand) < 17:
        hit(my_deck, dealer_hand)
    """
    This function should 2 lists as input
    - The first input should represent the deck of cards
    - The second list should represent the dealers hand
    The dealer should always hit if their hand is less than 17
    The dealer should always stay if their hand is greater than or equal to 17
    The hand_value() function can be used to check the value of the hand
    """
    
def get_winner(player_hand, dealer_hand):
    player_score = hand_value(player_hand)
    dealer_score = hand_value(dealer_hand)
    if player_score > 21:
        return "Dealer"
    elif dealer_score > 21:
        return "Player"
    elif player_score > dealer_score:
        return "Player"
    elif dealer_score > player_score:
        return "Dealer"
    else:
        return "Tie !"
    """
    This function should receive 2 lists as input representing the player's hand and the dealer's hand
    It should return either "player" or "dealer" depending on who had the better hand.
    """



def round(my_deck):
    if len(my_deck) < 10:
        print("cards are low, Deck will be reset.")
        my_deck = deck.shuffle()
    player_hand, dealer_hand = deal(my_deck)
    player_action = get_action()
    bust = False
    while player_hand == "hit" and not bust:
        bust = hit(my_deck,player_hand)
        if not bust:
            player_action = get_action()
    if not bust:
        dealer_action(my_deck, dealer_hand)
    print(get_winner(player_hand,dealer_hand), "wins!")

    """
    The round should receive a list representing a deck as input
    If the deck is getting low, we should reshuffle.
    The deal() function should be called to create lists representing player and dealer hands
    The program should display the players hand value
    The program should call the get_action() function to determine if the player will hit or stay
    If they choose to hit, the hit() function should be called
    Finally, the get_winner function should be called to determine who won and display the winner of the hand.
    """


def main():
    my_deck = deck.shuffle()
    play_again = True
    while play_again:
        round(my_deck)
        another_round = input("Would you like to play again? ( Y / N )")
        if another_round in ['n','N']:
            play_again = False
    """
    Use the deck module to create a shuffled deck
    Setup a loop that runs the round() until the user chooses to quit
    """
    
    

main()

