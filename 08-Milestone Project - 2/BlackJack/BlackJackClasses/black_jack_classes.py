from random import shuffle


class Card:

    def __init__(self, suit, rank, values):
        self.suit = suit
        self.rank = rank
        self.value = values[self.rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:

    def __init__(self, suits, ranks, values):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank, values))

    def shuffle_deck(self):
        shuffle(self.deck)

    def deal(self):
        return self.deck.pop(0)

    def __str__(self):
        card_list = ''
        for card in self.deck:
            card_list += f'{str(card)}\n'

        return card_list


class Hand():

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        if self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:

    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet
