#Objective: to understand relationship in between class & class
# is-a (Inheritance)
# has-a (Relation)
# use-a (Dependence)

#Exercise 1: Simple Poker Game
#Rules: 52 Poker Cards without Joker, 4 Players, Each Player get 13 cards, sorted

from enum import Enum #Enum is the function that make spring carry respective value
import random

class Suite(Enum):
    SPADE = 0 #can write in SPADE,HEART,CLUB,DIAMOND = range(4)
    HEART = 1
    CLUB = 2
    DIAMOND = 3

#Test if success
#for suite in Suite:
#   print(f"{suite}:{suite.value}")

class Card:
    def __init__(self, suite, face):
        self.suite = suite
        self.face = face
    def __repr__(self): #__repr__ is another built-in function, to display the intent value
        suites = '♠♥♣♦' # define suites into respective symbol.
        face = ["","A","2","3","4","5","6","7","8","9","10","J","Q","K"] #make 0="" because 1 have to be A
        return f"{suites[self.suite.value]}{face[self.face]}"

    def __lt__(self, other): # __lt__ = less than, same goes __ge__ = greater equal,etc
        if self.face == other.face: #compare card face value
            return self.suite.value > other.suite.value
        return self.face < other.face

#testing
#card1 = Card(Suite.HEART, 13)
#print(card1)

class Poker: #Inherit from Card
    def __init__(self):
        self.cards = [Card(suite,face)
                      for suite in Suite
                      for face in range(1,14)] #This is to set up all cards
        self.current = 0 #record card position

    def shuffle(self):
        self.current = 0
        random.shuffle(self.cards) #shuffle is built-in function

    def deal(self):
        card = self.cards[self.current]  #card = cards position for return purpose
        self.current += 1 #when deck = 52, current = 0, so +1 when each deal
        return card

    def has_next(self):
        return self.current < len(self.cards) #return when current card less than total cards


poker = Poker() #define poker
poker.shuffle() #define shuffle

class Player:
    def __init__(self,name):
        self.name = name
        self.cards = [] #for append card get purpose
    def get_one(self,card):
        self.cards.append(card)
    def arrange(self):
        self.cards.sort()

players = [Player("NG"),Player("ZF"),Player("ZiYong"),Player("BM")] #create players list
for _ in range(13):
    for player in players:
        player.get_one(poker.deal())

for player in players:
    player.arrange()
    print(f"{player.name}: {player.cards}")



