from BlackJack.BlackJackClasses.black_jack_classes import Card
from BlackJack.BlackJackClasses.black_jack_classes import Deck
from BlackJack.BlackJackClasses.black_jack_classes import Hand
from BlackJack.BlackJackClasses.black_jack_classes import Chips
from IPython.display import clear_output
from random import shuffle

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}

playing = True


def take_bet(chips):

    while True:

        try:
            user_bet = int(
                input(f'Please wager some chips. Available chips: {chips.total} \n'))
        except:
            clear_output()
            print('Sorry, please input a digit')
        else:
            if chips.total >= user_bet:
                clear_output()
                chips.bet = user_bet
                break
            else:
                clear_output()
                print(f'Not enough chips. Available chips: {chips.total} \n')


def hit(deck, hand):

    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop

    while True:
        user_choice = input('Hit or Stand: \n').upper()

        if user_choice in ['HIT', 'STAND', 'H', 'S']:
            if user_choice == 'HIT' or user_choice == 'H':
                hit(deck, hand)
                break
            else:
                playing = False
                break
        else:
            print("Please input 'HIT' or 'STAND': \n")


def show_some(player, dealer):

    clear_output()

    print("Player's hand:")
    for _ in range(len(player.cards)):
        print(player.cards[_])

    print(f'Player hand value: {player.value}')

    print("Dealer's hand:")
    print(dealer.cards[0])


def show_all(player, dealer):

    clear_output()

    print("Player's hand:")
    for _ in range(len(player.cards)):
        print(player.cards[_])

    print(f'Player hand value: {player.value}')

    print("Dealer's hand:")
    for _ in range(len(dealer.cards)):
        print(dealer.cards[_])

    print(f'Dealer hand value: {dealer.value}')


def player_busts(chips):
    print('PLAYER BUST!')
    chips.lose_bet()
    print(f"Player's chips: {chips.total}")


def player_wins(chips):
    print('Player WINS!')
    chips.win_bet()
    print(f"Player's chips: {chips.total}")


def dealer_busts(chips):
    print('DEALER BUST!')
    chips.win_bet()
    print(f"Player's chips: {chips.total}")


def dealer_wins(chips):
    print('DEALER WINS!')
    chips.lose_bet()
    print(f"Player's chips: {chips.total}")


def push(chips):
    print('PUSHED')
    print(f"Player's chips: {chips.total}")


def play_a_hand(deck, player, dealer, chips):
    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player)

        # Show cards (but keep one dealer card hidden)
        show_some(player, dealer)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player.value > 21:
            show_all(player, dealer)
            player_busts(chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player.value <= 21:
        while dealer.value <= 17:
            hit(deck, dealer)

        # Show all cards
        show_all(player, dealer)

        # Run different winning scenarios
        if dealer.value > 21:
            dealer_busts(chips)
        elif dealer.value > player.value:
            dealer_wins(chips)
        elif dealer.value < player.value:
            player_wins(chips)
        elif dealer.value == player.value:
            push(chips)


def new_deal(deck, player, dealer):
    # Create & shuffle the deck, deal two cards to each player
    deck.shuffle_deck()

    for _ in range(2):
        hit(game_deck, new_player_hand)
        hit(game_deck, dealer_hand)


new_game = True
while new_game:
    clear_output()
    # Print an opening statement
    print('Welcome to Clarence Palace, where the House always wins!')

    # Set up the Player's chips
    new_player_chips = Chips()

    play_hand = True
    while play_hand:

        game_deck = Deck(suits, ranks, values)
        new_player_hand = Hand()
        dealer_hand = Hand()

        new_deal(game_deck, new_player_hand, dealer_hand)

        # Prompt the Player for their bet
        take_bet(new_player_chips)

        # Show cards (but keep one dealer card hidden)
        show_some(new_player_hand, dealer_hand)

        # Play a hand
        play_a_hand(game_deck, new_player_hand, dealer_hand, new_player_chips)

        if new_player_chips.total == 0:
            break
        else:
            while True:
                # Ask to play again
                play_another_hand = input(
                    'Would you like to play another hand? Yes or No: \n').upper()

                if play_another_hand in ['YES', 'NO', 'Y', 'N']:
                    if play_another_hand == 'YES' or play_another_hand == 'Y':
                        playing = True
                        break
                    else:
                        play_hand = False
                        break
                else:
                    print("Please input 'YES' or 'NO': ")

    while True:
        # Ask to play again
        play_another_game = input(
            'Would you like to start a new game? Yes or No: \n').upper()

        if play_another_game in ['YES', 'NO', 'Y', 'N']:
            if play_another_game == 'YES' or play_another_game == 'Y':
                playing = True
                break
            else:
                new_game = False
                break
        else:
            print("Please input 'YES' or 'NO': \n")
