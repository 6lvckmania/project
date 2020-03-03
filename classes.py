import random
import itertools

class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit   
    
    def __str__(self):
        return self.number + self.suit

class DeckOfCards:
    def __init__(self):
        self.list1 = []
        number1 = ("2","3","4","5","6","7","8","9","10","J","Q","K","A")
        suit1 = ("\u2660","\u2665","\u2666","\u2663")
        for suit,number in itertools.product(suit1,number1):
            self.list1.append(Card(suit, number))

    def shuffle(self):
        random.shuffle(self.list1)  

    def getrand(self):
        try:
            return str(random.choice(self.list1))
        except IndexError:
            self.__init__()
            return "!!!There are no cards, get random again!!!"

    def pop(self):
        try:
            return str(self.list1.pop())
        except IndexError:
            self.__init__()
            return "!!!There are no cards, pop again!!!"
    
    def index(self, value):
        if not self.list1:
            self.__init__()
            return "!!!there are no cards, type index again!!!"
        try:
            return str(self.list1[int(value)])
        except IndexError:
            return "!!!your index is out of range!!!"
        except ValueError:
            return "!!!not a number!!!"
            
