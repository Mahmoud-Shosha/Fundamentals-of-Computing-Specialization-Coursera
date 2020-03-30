# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")

# initialize some useful global variables
in_play = False
outcome = ""
feedback = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10}

# define players hands
player_hand = None
dealer_hand = None
deck = None


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]],
                          CARD_SIZE)


# define hand class
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        str_repr = "Hand contains "
        for card in self.cards:
            str_repr += str(card) + " "
        return str_repr

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        cards_value = 0
        contains_ace = False
        for card in self.cards:
            card_rank = card.get_rank()
            cards_value += VALUES[card_rank]
            if card_rank == "A":
                contains_ace = True
        if contains_ace and (cards_value + 10) <= 21:
            cards_value += 10
        return cards_value

    def draw(self, canvas, pos):
        for i in range(len(self.cards)):
            self.cards[i].draw(canvas, [pos[0] + 1.4 * i * CARD_SIZE[0], pos[1]])


# define deck class
class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        # shuffle the deck
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

    def __str__(self):
        str_repr = "Deck contains "
        for card in self.cards:
            str_repr += str(card) + " "
        return str_repr


# define event handlers for buttons
def deal():
    global outcome, in_play, player_hand, dealer_hand, deck, feedback, score

    deck = Deck()
    deck.shuffle()
    player_hand = Hand()
    dealer_hand = Hand()
    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())

    if in_play:
        score -= 1
        in_play = False
        outcome = "New deal?"
        feedback = "You lose"
    else:
        in_play = True
        outcome = "Hit or stand?"
        feedback = ""

    # print "player:  ", player_hand.get_value()
    # print "dealer:  ", dealer_hand.get_value()


def hit():
    global score, in_play, outcome, feedback
    if in_play:
        player_hand.add_card(deck.deal_card())
        # print "player:  ", player_hand.get_value()
        # print "dealer:  ", dealer_hand.get_value()
        if player_hand.get_value() > 21:
            score -= 1
            in_play = False
            outcome = "New deal?"
            feedback = "You went bust and lose"
            # print "You have busted"

    # if the hand is in play, hit the player

    # if busted, assign a message to outcome, update in_play and score


def stand():
    global score, in_play, outcome, feedback
    if in_play:
        # print "player:  ", player_hand.get_value()
        # print "dealer:  ", dealer_hand.get_value()
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())
        if dealer_hand.get_value() > 21:
            score += 1
            feedback = "You win"
            # print "Dealer has busted"
        elif player_hand.get_value() <= dealer_hand.get_value():
            score -= 1
            feedback = "You lose"
            # print "Dealer wins"
        else:
            score += 1
            feedback = "You win"
            # print "Player wins"
        in_play = False
        outcome = "New deal?"

    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score


# draw handler
def draw(canvas):
    canvas.draw_text("Blackjack", [100, 100], 60, "#52FBF0")
    canvas.draw_text("Score: " + str(score), [440, 100], 30, "black")
    canvas.draw_text("Dealer", [60, 180], 30, "black")
    canvas.draw_text(feedback, [220, 180], 30, "black")
    dealer_hand.draw(canvas, [60, 220])
    canvas.draw_text("Player", [60, 400], 30, "black")
    canvas.draw_text(outcome, [220, 400], 30, "black")
    player_hand.draw(canvas, [60, 440])

    # Dealer hole
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE,
                          [96, 268], CARD_BACK_SIZE)
    # test to make sure that card.draw works, replace with your code below


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

# create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit", hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
deal()
frame.start()

# remember to review the gradic rubric