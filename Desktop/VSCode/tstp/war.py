from random import shuffle


class Card:   #creates object for the portion of the cards
    suits = ["spades", "hearts", "diamonds", "clubs"] #variable listing the different types of suits in a deck of cards
    values = [None, None, '2', '3', '4', '5', '6', '7', '8', '10', #variable listing the numbers present in a deck of cards. notice the 2 "None",
     'Jack', 'Queen', 'King', 'Ace'] #they are there to take place of index 0 and 1 in the list. since a deck of cards starts at 2. 

    def __init__(self, v, s) -> None:  #method to initiate the class Card
        self.value = v  #instance variable for value and suit
        self.suit = s 

    def __lt__ (self, c2):  #magic method "less than"
        if self.value < c2.value:
            return True         #using the if statement, if the value of the card is less than the other return true
        if self.value == c2.value: #using the if statement, if the value of the card is equal to the other, proceed and check suit
            if self.suit < c2.suit: #checking suit using if statement, if the suit is less/weaker than the other 
                return True   
            else:
                return False
        return False

    def __gt__(self, c2):
        if self.value > c2.value:  ##using the if statement, if the value of the card is more than the other 
                return True
        if self.value == c2.value: #using the if statement, if the value of the card is equal to the other, proceed and check suit
            if self.suit > c2.suit: #checking suit using if statement, if the suit is greater/stronger than the other
                return True
            else:
                return False
        return False

    def __repr__(self) : #method used to return the object in a string
        v = self.values[self.value] + " of " + self.suits[self.suit]  #the string that is to returned. using the values inside the [values] list
        return v            # and the values inside the [suits]list. parameter is the intance variable of the card class initiation method called

class Deck: #creates object that defies the deck of card
    def __init__(self) -> None: #initiates the Deck class/object
        self.cards = []  #open list for cards
        for i in range (2,15): # range sets the index (i) from 2 to 15 because there is 14 different values in a deck, and 0 and 1 are nonexisitent
            for j in range (4): #range sets the index (j) to 4 because there is 4 different suits 
                self.cards.append(Card(i,j))  #.append function adds the ranced to the open list 
        shuffle(self.cards) #tool to shuffle info inside the list
    
    def rm_card(self): #method used to remove cards from deck during the games
        if len(self.cards) == 0: #when the length of the list is 0 it goes back up the program
            return
        return self.cards.pop()  #.pop function removes info from list
        
class Player:  #creates object for the portion of the player
    def __init__(self,name) -> None: 
        self.wins = 0 #instance variable to keep track how many rounds a player has won
        self.card = None #instance variable that represent the card the player is currently holding 
        self.name = name #instance variable that keeps track of players name

class Game: #creates object for the actual game portion
    def __init__(self) -> None:
        name1 = input("p1 name ") #input function to type in players name
        name2 = input("p2 name ")
        self.deck = Deck() # created new object Deck and stores it in instance variable 
        self.p1 = Player(name1) #creates new object Player using the names from the inputs above 
        self.p2 = Player(name2)

    def wins(self,winner): #method to annouce the winner fo the round
        w = "{} wins this round"
        w = w.format(winner) #.format funtion adds the name of the player who won the round
        print(w)

    def draw(self, p1n, p1c, p2n, p2c): #method that draws the cards
        d = "{} drew {}  {} drew {}" #instance variables are player 1 name then card and player 2 name and card
        d = d.format(p1n, p1c, p2n, p2c) #.format functions adds the instance variables to their corresponding index
        print (d)

    def play_game(self): #method that starts the game
        cards = self.deck.cards #variable storing Deck object and list of cards
        print("beginning War!")
        while len(cards) >= 2: #loop saying while the number of cards is greater than 2, keep looping
            m = "q to quit." + "Any key to play:" #variable storing strings 
            response = input(m) #input function using variable (m)^^
            if response == 'q':
                break
            p1c = self.deck.rm_card() #variable storing Deck object and remove card method
            p2c = self.deck.rm_card()
            p1n = self.p1.name #variable storing name of player
            p2n = self.p2.name
            self.draw (p1n, p1c, p2n, p2c) #draws card accord to the method draw from above
            if p1c > p2c:
                self.p1.wins += 1 # if statement saying if player 1 card greater, add 1 win to the wins instance variable
                self.wins(self.p1.name) #fills in the the name of the player into the wins method
            else: 
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1, self.p2) #variable storing the winner with its parameters being both players 

        print("War is over. {} wins".format(win))

    def winner(self, p1, p2): #method to call the winner out
        if p1.wins > p2.wins: #if the number of wins from player 1 is greater than player 2 
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "It was a tie!" 

game = Game()
game.play_game()         


        
        


        
        
                
        
        