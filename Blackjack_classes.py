import random

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace")
values = {"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":10,"Queen":10,"King":10,"Ace":11}

class Card():

        def __init__(self,suit,rank):
            self.suit = suit
            self.rank = rank
            self.value = values[rank]
        
        def __str__(self):
            return self.rank + " of " + self.suit

class Deck():

    def __init__(self):
        self.deck = []

        for suit in suits:
            for rank in ranks:
                #Card object creation and appended into the list
                new_card = Card(suit,rank)
                self.deck.append(new_card)
    
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

    def __str__(self):
        cards =""
        for card in self.deck:
            cards += "\n" + card.__str__()
        return cards
    

class Player():
    
    def __init__(self,name):
        self.name = name
        self.hand = []
        self.value = 0
        self.aces = 0

    def add_card(self,new_card):
            self.hand.append(new_card)
            self.value += values[new_card.rank]
            if new_card.rank == "Ace":
                self.aces+=1

    def ace_adjust_hand(self):
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

    def __str__(self):
        return f"{self.name} has {len(self.hand)} cards"

# Testing Classes/methods

# new_deck = Deck()
# new_deck.shuffle()
# p1 = Player("p1")
# p1.add_card(new_deck.deal_hand())
# for x in p1.hand:
#     print(x)
# p1.add_card(new_deck.deal())
# print(p1.hand[-1])