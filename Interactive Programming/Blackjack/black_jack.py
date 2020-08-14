# Mini-project #6 - Blackjack MIT PROJEKT

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
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


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
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)


# define hand class

class Hand:
    def __init__(self):
        self.cards=[]

    def __str__(self):
        s="Cards in hand: "
        for card in self.cards:
            s += str(card)+ ", "
        return s

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        value=0
        aces=False

        for card in self.cards:
            rank=card.get_rank()
            if rank=='A':
                aces=True
            value += VALUES[rank]

        if aces and value<=11:
            value +=10

        return(value)

    def draw(self, canvas, pos):
        for card in self.cards:
            n=self.cards.index(card)
            card.draw(canvas, [pos[0]+(n+0.5*n)*CARD_SIZE[0], pos[1]])

# define deck class

class Deck:
    def __init__(self):
        deck=[Card(suit,rank) for suit in SUITS for rank in RANKS]
#        deck=[]
 #       for suit in SUITS:
  #          for rank in RANKS:
   #             card=Card(suit,rank)
    #            deck.append(card)
        self.cards=deck

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        if len(self.cards)>0:
            card=self.cards[-1]
            self.cards.pop(-1)
            return(card)
        else:
            print "No cards in deck"

    def add_card_to_top_of_deck(self,card):
        if card not in self.cards:
            self.cards.append(card)
        else:
            print "Card already in deck"

    def __str__(self):
        s="Cards in deck: "
        for card in self.cards:
            s += str(card)+ ", "
        return s

#define event handlers for buttons
def deal():
    global outcome, in_play
    global deck, player_hand, dealer_hand, score

    if in_play:
        for card in player_hand.cards:
            deck.add_card_to_top_of_deck(card)
        for card in dealer_hand.cards:
            deck.add_card_to_top_of_deck(card)
        deck.shuffle

        #print len(deck.cards)
        player_hand=Hand()
        dealer_hand=Hand()
        score -= 1
        outcome= "Dealer won. Hit or stand?"


    else:
        deck=Deck()
        deck.shuffle()
        outcome="          Hit or stand?"



    player_hand=Hand()
    dealer_hand=Hand()

    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())

    print "player hand: ",player_hand
    print "dealer hand: ", dealer_hand

    in_play = True

def hit():
    global outcome, in_play

    if not in_play:
        return()

    if player_hand.get_value()<=21:
        player_hand.add_card(deck.deal_card())
        outcome = "        Hit or stand?"
        print ""
        print "player hand: ", player_hand
        print "value of player hand: ", player_hand.get_value()
        if player_hand.get_value()>21:
            #print "You have busted"
            outcome = "Dealer won. New deal?"
            in_play=False
def stand():
    global score, outcome, in_play

    if not in_play:
       # print "not in play"
        return()

    if player_hand.get_value()>21:
        #print "You have busted, so you cannot stand"
        outcome= "Dealer won. New deal?"
        in_play=False

    else:
        while dealer_hand.get_value()<17:
            dealer_hand.add_card(deck.deal_card())
        print ""
        print "final dealer_hand: ", dealer_hand
        print "value", dealer_hand.get_value()
        if dealer_hand.get_value()>21:
            print "Dealer busted"
            score +=1
            print score
            outcome ="Player won. New deal?"
        else:
            if player_hand.get_value()>dealer_hand.get_value():
                print "player won"
                score +=1
                print "score: ", score
                outcome ="Player won. New deal?"
            else:
                print "dealer won"
                score -= 1
                print "score: ", score
                outcome ="Dealer won. New deal?"
        in_play=False

# draw handler
def draw(canvas):

    player_hand.draw(canvas,[50,450])
    dealer_hand.draw(canvas,[50,50])

    canvas.draw_text("Blackjack", [242,240],25,"Black")
    canvas.draw_text("Player", [250,588],25, "White")
    canvas.draw_text("Dealer", [250,30],25, "White")

    canvas.draw_text("Score: "+str(score), [250,270],25, "Black")
    canvas.draw_text(outcome, [170,400],25, "White")

    if in_play:
        canvas.draw_image(card_back,CARD_BACK_CENTER, CARD_BACK_SIZE, (50+CARD_BACK_CENTER[0],50+CARD_BACK_CENTER[1]), CARD_BACK_SIZE)

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()
