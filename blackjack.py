import random


def main():
    print("\n" "Welcome to Black Jack !")
    input("Press any key to be dealt a hand.\n")
    round()

def round():
    shuffled_deck = shuffle_deck(make_deck())
    player_hand, dealer_hand = deal_cards(shuffled_deck)
    player_total = player_logic(player_hand, shuffled_deck)
    if player_total > 21:
        print("You Busted ! You Lose !")
    else:
        dealer_total = dealer_logic(dealer_hand, shuffled_deck)
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

def player_logic(hand, deck):
    print(f"You got dealt a(n) {hand[0]} and a(n) {hand[1]} .")
    draw_2cards(hand)
    total = 0
    stay = True
    while total < 22 and stay:
        hit_stay = input("Would you like to hit or stay? ").lower()
        while hit_stay != "hit" and hit_stay != "stay":
            print(hit_stay)
            hit_stay = input("Invalid input. Would you like to hit or stay? ").lower()
        if hit_stay == "hit":
            hit(hand, deck)
            total = get_hand_value(hand)
            if total > 21:
                print("You Busted !")
        else:
            print(f"Your hand is : {get_hand_value(hand)}\n")
            stay = False
    return total

def dealer_logic(hand, deck):
    print(f"The dealer has a(n) {hand[0]} and a(n) {hand[1]} .")
    draw_2cards(hand)
    total = get_hand_value(hand)
    while total < 17:
        print("The dealer hits !")
        hit(hand, deck)
        total = get_hand_value(hand)
    if total > 22:
        print("The dealer busted !")
    else:
        print("The dealer stays !")
        return total
    # stay = True
    # while total < 22 and stay:
    #     if total < 17:
    #         hit(hand, deck)
    #         total = get_hand_value(hand, total)
    #         if total > 21:
    #             print("You Busted !")
    #     else:
    #         print(f" Your hand is : {total}")
    #         stay = False

def hit(hand, deck):
    hand.append(deck.pop())
    if len(hand) == 3:
        draw_3cards(hand)
    elif len(hand) == 4:
        draw_4cards(hand)
    else:
        print("More than 4 cards in hand !")

def get_hand_value(hand):
    total = 0
    for card in hand:
        if card in ["J","Q","K"]:
            total += 10
        elif card == "A":
            total += 1
        elif 1 < card < 11:
            total += card
        else:
            print("Card Not Found !") 
    return total

# will draw the first two cards the user gets
def draw_2cards(hand):
            print(f" _______    _______\n"
                f"| {hand[0]}     |  | {hand[1]}     |\n"
                f"|       |  |       |\n"
                f"|       |  |       |\n"
                f"|     {hand[0]} |  |     {hand[1]} |\n"
                f"|_______|  |_______|\n")

# def draw_3cards(hand): draws 3 cards similar to the draw_2cards() function
def draw_3cards(hand):
            print(f" _______    _______    _______\n"
                f"| {hand[0]}     |  | {hand[1]}     |  | {hand[2]}     |\n"
                f"|       |  |       |  |       |\n"
                f"|       |  |       |  |       |\n"
                f"|     {hand[0]} |  |     {hand[1]} |  |     {hand[2]} |\n"
                f"|_______|  |_______|  |_______|\n")

def draw_4cards(hand):
            print(f" _______    _______    _______    _______\n"
                f"| {hand[0]}     |  | {hand[1]}     |  | {hand[2]}     |  | {hand[3]}     |\n"
                f"|       |  |       |  |       |  |       |\n"
                f"|       |  |       |  |       |  |       |\n"
                f"|     {hand[0]} |  |     {hand[1]} |  |     {hand[2]} |  |     {hand[3]} |\n"
                f"|_______|  |_______|  |_______|  |_______|\n")

main()