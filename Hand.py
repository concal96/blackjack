'''
Hand Class
'''

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        values[card.rank]
        self.value += values[card.rank]
        
        #track aces
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        #if total value > 21 and i still have an ace:
        # change the ace to have a value of 1 instead of 11
        while self.value > 21 and self.aces: #TRUE ONLY IF NOT ZERO - TRUTHYNESS
            self.value -= 10
            self.aces -= 1