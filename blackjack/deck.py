import random

def shuffle():
    deck = []
    face =['A','J','Q','K']
    for _ in range(4):
        for i in range(2,11):
            deck.append(i)
        deck += face
    print('Deck is created.')
    random.shuffle(deck)
    print('Deck is shuffled.')
    return deck
    """
    This function should create a list representing a deck of cards.
    It should shuffle the list and return it.    
    """
    

def deal_card(deck):
    card = deck[0]
    del deck[0]
    return card

    """
    The deal card function should receive a deck as an input.
    It should remove the first item from the list and return it as a card.
    """
    


my_deck = shuffle()
my_card = deal_card(my_deck)