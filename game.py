# AlPHA is the creator of this script and this script is made with love.
# If you want to use this script, please give me credit.
# And don't forget to have fun.
# Thank you.
# AlPHA

from time import sleep
print("""
.------..------..------..------..------.     .------..------..------..------.
|B.--. ||L.--. ||A.--. ||C.--. ||K.--. |.-.  |J.--. ||A.--. ||C.--. ||K.--. |
| :(): || :/\: || (\/) || :/\: || :/\: ((5)) | :(): || (\/) || :/\: || :/\: |
| ()() || (__) || :\/: || :\/: || :\/: |'-.-.| ()() || :\/: || :\/: || :\/: |
| '--'B|| '--'L|| '--'A|| '--'C|| '--'K| ((1)) '--'J|| '--'A|| '--'C|| '--'K|
`------'`------'`------'`------'`------'  '-'`------'`------'`------'`------'
\n\n\n""")
sleep(3)
import random as r
from os import system

global num_of_decks
suits = {'S': '\u2660',
         'C': '\u2663',
         'H': '\u2665',
         'D': '\u2666'}

class Cards:
    def __init__(self, nod):
        card_num = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'J', 'Q', 'K']
        suits = ['S', 'C', 'H', 'D']
        self.deck = ([(idx, jdx) for idx in suits for jdx in card_num])
        self.deck = self.deck * nod
        r.shuffle (self.deck)

    def reshuffle_deck(self, nod):
        input ("Deck about to finish. Reshuffling deck. Press any key to continue..")
        self.__init__ (nod)


class Hands:
    def __init__(self, player_onhand=pow (2, 25), is_dealer=False):
        self.dealer_hand = is_dealer
        self.cards = []
        self.value = 0
        self.ace = False
        self.player_current_balance = player_onhand
        self.bet = 0

    def win_bet(self):
        self.player_current_balance += self.bet

    def lose_bet(self):
        self.player_current_balance -= self.bet

    def add_card(self, card):
        self.cards.append (card)
        if card[1] == 'A':
            if not self.ace and (self.value + 11 <= 21):
                self.value = self.value + 11
                self.ace = True
            else:
                self.value = self.value + 1
        else:
            if type (card[1]) == int:
                self.value = self.value + card[1]
            else:
                self.value = self.value + 10
            if self.value > 21 and self.ace:
                self.value -= 10
                self.ace = False

    def print_card(self, card_suit, pos=1):
        s = ""
        for _ in card_suit:
            s = s + "\t ________"
        print (s.rjust (pos))
        s = ""
        for idx, jdx in card_suit:
            if jdx == 10:
                s = s + "\t| {0}     |".format (jdx)
            else:
                s = s + "\t| {0}      |".format (jdx)
        print (s.rjust (pos))
        s = ""
        for _ in card_suit:
            s = s + "\t|        |"
        print (s.rjust (pos))
        s = ""
        for idx, jdx in card_suit:
            s = s + "\t|   {0}    |".format (suits[idx])
        print (s.rjust (pos))
        s = ""
        for _ in card_suit:
            s = s + "\t|        |"
        print (s.rjust (pos))
        s = ""
        for idx, jdx in card_suit:
            if jdx == 10:
                s = s + "\t|     {0} |".format (jdx)
            else:
                s = s + "\t|      {0} |".format (jdx)
        print (s.rjust (pos))
        s = ""
        for _ in card_suit:
            s = s + "\t|________|"
        print (s.rjust (pos))

    def show_card(self, hide=False):
        if self.dealer_hand:
            if hide:
                print ('Dealer'.rjust (60))
                self.print_card ([self.cards[0]])
            else:
                print ('Dealer (Total: {0})'.format (self.value).rjust (60))
                self.print_card (self.cards)
            for idx in range (4): print ('')
        else:
            print ('Player (Total: {0})'.format (self.value).rjust (60))
            self.print_card (self.cards)
            print ('Bet Amount: {0}'.format (self.bet).rjust (60))


def clear_screen():
    system ('cls')


def validate_number(p_text):
    while True:
        try:
            p_num = int (input (p_text))
        except ValueError:
            print ("Sorry, please enter a number")
        else:
            return p_num


def take_bet(player_hand):
    while True:
        player_hand.bet =validate_number('How many chips you want to bet: ')
        if player_hand.bet > player_hand.player_current_balance:
            print ("Sorry, you cannot bet more than {0}".format (player_hand.player_current_balance))
        else:
            clear_screen ()
            break


def select_play_deck():
    global num_of_decks
    print ("How may decks you want to play with \n")
    num_of_decks = validate_number ("Choose from number 1 to 4: ")
    while num_of_decks not in range (1, 5):
        clear_screen ()
        num_of_decks = int (input ("Invalid Selection. Please select from number 1 to 4: "))
    clear_screen ()


print ('Welcome to Black Jack\n'.rjust (50))
select_play_deck ()
card = Cards (num_of_decks)

player_opening_balance = 100
play = 'Y'
while play in ("Y", "y"):
    dealer = Hands (is_dealer=True)
    player = Hands (player_opening_balance)
    take_bet (player)

    if len (card.deck) <= 7:
        card.reshuffle_deck (num_of_decks)
    for idx in range (2):
        player.add_card (card.deck.pop ())
        dealer.add_card (card.deck.pop ())
    dealer.show_card (True)
    player.show_card ()

    response = 2
    while response != 1:
        print ('')
        try:
            response = int (input ('Do you want to Stay(1) or hit(2)?: '))
            if response == 2:
                player.add_card (card.deck.pop ())
            system ('cls')
            dealer.show_card (True)
            player.show_card ()
            if player.value == 21:
                input ('Your Total is 21. Stay at 21. Dealer Turn. Press any key to continue')
                break
            elif player.value > 21:
                break
        except:
            print ('Please enter correct number')
            response = 0
    while dealer.value < 17 and player.value < 22:
        system ('cls')
        dealer.show_card (False)
        player.show_card ()
        print ('')
        print ('Dealer cards total is {0}. Dealer Turn to Pick the card \n'.format (dealer.value))
        input ('Press any key to continue...')
        dealer.add_card (card.deck.pop ())
    system ('cls')
    dealer.show_card (False)
    player.show_card ()


    if player.value > 21:
        player.lose_bet ()
        print ('Dealer has {0} and You have {1}. Dealer WON!!'.format (dealer.value,
                                                                       player.value))
    elif dealer.value > 21:
        player.win_bet ()
        print (
            'You has {0} and Dealer have {1}. You WON!! CONGRATS'.format (player.value, dealer.value))
    elif dealer.value > player.value:
        player.lose_bet ()
        print ('Dealer has total of {0} for cards. Dealer Won!!'.format (dealer.value))
    elif player.value > dealer.value:
        player.win_bet ()
        print ('You has total of {0} for cards. Dealer has total of {1} for cards. You Won!! CONGRATS' \
               .format (player.value, dealer.value))
    else:
        print ("Both you have dealer have same total. It's a Tie.")
    print ('')
    player_opening_balance = player.player_current_balance
    print ("You have {0} chips in hand. \n".format (player_opening_balance))
    if player_opening_balance == 0:
        input ()
        play = 'N'
    else:
        play = input ('Do You want to play More? Yes (Y) or No (N)')
    clear_screen ()
else:
    print ("Thanks for playing with us. You have {0} chips in your hand. \n".format (player_opening_balance))
    input ("Press any key to exist...")