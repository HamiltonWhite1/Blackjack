import random
from black_jack_classes import Deck
import time

GAME = Deck
deck = GAME.shuffle_the_deck()
print("Welcome to the table. Let's get started")
PLAYING = True
hands = 0
while PLAYING:
    cards = GAME.dealer(deck)
    player_cards = GAME.player(cards)
    dealer_cards = GAME.dealer_plays(cards)
    if sum(dealer_cards) > 21:
        print("Dealer bust!")
        PLAYING = False
    elif sum(dealer_cards) == 21:
        print("Dealer Blackjack!")
        PLAYING = False
    if sum(player_cards) > 21:
        print("Player bust!")
        PLAYING = False
    elif sum(player_cards) == 21:
        print("Player Blackjack!")
        PLAYING = False
    else:
        HIT_OR_QUIT = True
        while HIT_OR_QUIT:
            HITTING = True
            while HITTING:
                hit_or_quit = input(f"Player, these are your cards {player_cards}. Would you like to hit, or quit? H/Q: ").upper()
                if hit_or_quit == "Q":
                    HITTING = False
                elif hit_or_quit == "H":
                    player_cards.append(random.randint(1,13))
                    print(f"Your new cards are: {player_cards}")
                if sum(player_cards) > 21:
                    HITTING = False
            HIT_OR_QUIT = False
    hands += 1
    if sum(player_cards) < 21 and sum(player_cards) > sum(dealer_cards):
        print(f"Player wins with {sum(player_cards)}")
    else:
        print(f"Dealer wins with {sum(dealer_cards)}")
    break
print(f"There were {hands} hands of Blackjack dealt before the winner was declared.")

