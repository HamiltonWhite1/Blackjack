import random

class Deck:
    def __init__(self, number_of_decks, num_of_shuffles):
        self.number_of_decks = number_of_decks
        self.num_of_shuffles = num_of_shuffles
    
    def shuffle_the_deck():
        new_deck = [{"Clubs": None}, {"Diamonds": None }, {"Hearts": None }, {"Spades": None }]
        card_suite = []
        while len(card_suite) < 13:
            for i in range(14):
                new_card = random.randint(1, 13)
                if new_card in card_suite:
                    continue
                else:
                    card_suite.append(new_card)
        random.shuffle(card_suite)
        new_deck[0]["Clubs"] = card_suite
        new_deck[1]["Diamonds"] = card_suite
        new_deck[2]["Hearts"] = card_suite
        new_deck[3]["Spades"] = card_suite 
        return new_deck

    def player(cards):
        player_cards = cards[0]
        print(f"Player, your cards are {player_cards}")
        return player_cards

    def dealer_plays(cards):
        dealer_cards = cards[1]
        print("Dealer has their cards")
        return dealer_cards

    def dealer(the_deck):
        player_cards = []
        dealer_cards = []
        suites = ["Clubs", "Hearts", "Spades", "Diamonds"]
        while len(player_cards) < 2:
            rand_suite = random.choice(suites)
            rand_card = random.randint(0, 13)
            for i in the_deck:
                try:
                    player_cards.append(i[rand_suite][rand_card])
                except:
                    continue
        while len(dealer_cards) < 2:
            rand_suite = random.choice(suites)
            rand_card = random.randint(0, 13)
            for i in the_deck:
                try:
                    dealer_cards.append(i[rand_suite][rand_card])
                except:
                    continue
        return player_cards, dealer_cards