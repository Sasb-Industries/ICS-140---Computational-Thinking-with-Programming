import random


def main():
    print("\n" "Welcome to Black Jack !")
    start = input("Press any key to be dealt a hand.")
    round()

def round():
    shuffled_deck = shuffle_deck(make_deck())
    player_hand, dealer_hand = deal_cards(shuffled_deck)
    print(f"You got dealt a(n) {player_hand[0]} and a(n) {player_hand[1]} .")
    draw_2cards(player_hand)
    print(dealer_hand)
    # draw_card(dealer_hand)




def make_deck(): # create deck from scratch
    deck = []
    face_cards = ["A","J","Q","K"]
    for _ in range(4):
        for i in range(2,11):
            deck.append(i)
        deck += face_cards
    return deck # Returns created deck

def shuffle_deck(deck): # takes deck as an input and shuffles contents
    random.shuffle(deck)
    return deck

def deal_cards(deck):
    card1 = deal_single_card(deck)
    card2 = deal_single_card(deck)
    card3 = deal_single_card(deck)
    card4 = deal_single_card(deck)
    return [card1, card2],[card3,card4]

def deal_single_card(deck):
    card = deck[0]
    del deck[0]
    return card

def draw_2cards(hand):
            print(f" _______    _______\n"
                 f"| {hand[0]}     |  | {hand[1]}     |\n"
                 f"|       |  |       |\n"
                 f"|       |  |       |\n"
                 f"|     {hand[0]} |  |     {hand[1]} |\n"
                 f"|_______|  |_______|")
main()