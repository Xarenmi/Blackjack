import random
import sys

discarded = []
repeated = []

print("""
     _______   ___            __       ______   __   ___   
    |   _   \ |   |          /  \     /  _   \ |  | /   )    
    (. |_)   )||  |         /    \   (♦ ( \___)(♠ |/   /      
    |♠     \/ |♣  |        /  /\  \  |  |      |     _/         
    (|  _  /\ \   |___    / ♥ __'  \ |  |   _  (   _  \      
    |  |_)  ♦)(     ♥ \  /   /  \   \(   \_) \ |♣ | \  \   
    (_______/  \_______)(___/    \___)\_______)(__|  \__)
                      ___      __       _____    __   ___
                     |   |    /  \     /  _   \ |  | /   ) 
                     ||  |   /    \   (♦ ( \___)(♠ |/   /  
                     |♥  |  /  /\  \  |  |      |     _/   
                  ___|   | / ♣ __'  \ |  |   _  (   _  \   
                 /  ♦    )/   /  \   \(   \_) \ |♣ | \  \  
                (_______/(___/    \___)\_______)(__|  \__)
                                            BY: XARENMI


""")


class Card:

    def __init__(self):
        self.info = self.trow_card() #tira una nueva carta
        self.index = self.info[0] #guarda el key del diccionario
        self.name = self.info[1][0] 
        self.points = self.info[1][1]
        self.type = self.get_type()
        self.structure = self.card_patronus()

    def trow_card(self):
        temp_index = random.randint(1, 13)
        for x in range(52): 
            if discarded.count(temp_index) <= 3:
                break

            else:
                temp_index = random.randint(1, 13)

        index = {
            1:['A', 11],
            2:['2', 2],
            3:['3', 3],
            4:['4', 4],
            5:['5', 5],
            6:['6', 6],
            7:['7', 7],
            8:['8', 8],
            9:['9', 9],
            10:['10', 10],
            11:['J', 10],
            12:['Q', 10],
            13:['K', 10],
            }

        card = index.get(temp_index)
        discarded.append(temp_index)
        return [temp_index, card] 

    def get_type(self):  
        t_type = random.randint(1,4)
        c_type = 'none'
        if t_type == 1:
            c_type = '♠'
        elif t_type == 2:
            c_type = '♥'
        elif t_type == 3:
            c_type = '♣'
        else:
            c_type = '♦'

        actual_card = self.name + c_type

        while actual_card in repeated:
            t_type = random.randint(1,4)
            if t_type == 1:
                c_type = '♠'
            elif t_type == 2:
                c_type = '♥'
            elif t_type == 3:
                c_type = '♣'
            else:
                c_type = '♦'

            actual_card = self.name + c_type

        repeated.append(actual_card)
        return c_type
        

    def card_patronus(self):

        card_structure = []

        top = ' ╔═════════╗ '
        ntany = ' ║{name}        ║ '.format(name = self.name)
        nt10 = ' ║{name}     {type} ║ '.format(name = self.name, type = self.type)
        s1 = ' ║         ║ ' #nothing
        s2 = ' ║    {type}    ║ '.format(type = self.type) #1center
        s3 = ' ║  {type}      ║ '.format(type = self.type) #1totheleft
        s4 = ' ║  {type}   {type}  ║ '.format(type = self.type) #2narrow
        s5 = ' ║ {type}     {type} ║ '.format(type = self.type) #2wide
        s6 = ' ║  {type} {type} {type}  ║ '.format(type = self.type) #3narrow
        s7 = ' ║ {type}  {type}  {type} ║ '.format(type = self.type) #3wide
        s8 = ' ║      {type}  ║ '.format(type = self.type) #1totherigth
        s9 = ' ║ {type} {type} {type} {type} ║ '.format(type = self.type) #4inarow
        nbtany = ' ║        {name}║ '.format(name = self.name)
        nbt10 = ' ║ {type}     {name}║ '.format(type = self.type, name = self.name)
        bottom = ' ╚═════════╝ '

        card_structure.append(top)

        if self.name == 'A' or self.name == 'J' or self.name == 'Q' or self.name == 'K':
            card_structure.append(ntany)
            card_structure.append(s1)
            card_structure.append(s2)
            card_structure.append(s1)
            card_structure.append(nbtany)
            
        elif self.name == '10':
            card_structure.append(nt10)
            card_structure.append(s7)
            card_structure.append(s5)
            card_structure.append(s7)
            card_structure.append(nbt10)
            
        elif self.name == '9':
            card_structure.append(ntany)
            card_structure.append(s7)
            card_structure.append(s7)
            card_structure.append(s7)
            card_structure.append(nbtany)

        elif self.name == '8':
            card_structure.append(ntany)
            card_structure.append(s6)
            card_structure.append(s9)
            card_structure.append(s6)
            card_structure.append(nbtany)
            
        elif self.name == '7':
            card_structure.append(ntany)
            card_structure.append(s4)
            card_structure.append(s6)
            card_structure.append(s4)
            card_structure.append(nbtany)

        elif self.name == '6':
            card_structure.append(ntany)
            card_structure.append(s4)
            card_structure.append(s4)
            card_structure.append(s4)
            card_structure.append(nbtany)
            
        elif self.name == '5':
            card_structure.append(ntany)
            card_structure.append(s4)
            card_structure.append(s2)
            card_structure.append(s4)
            card_structure.append(nbtany)

        elif self.name == '4':
            card_structure.append(ntany)
            card_structure.append(s4)
            card_structure.append(s1)
            card_structure.append(s4)
            card_structure.append(nbtany)
            
        elif self.name == '3':
            card_structure.append(ntany)
            card_structure.append(s8)
            card_structure.append(s2)
            card_structure.append(s3)
            card_structure.append(nbtany)

        elif self.name == '2':
            card_structure.append(ntany)
            card_structure.append(s2)
            card_structure.append(s1)
            card_structure.append(s2)
            card_structure.append(nbtany)

        card_structure.append(bottom)
        return card_structure



class Player:

    def __init__(self):
        self.type = 'PLAYER'
        self.name = ''
        self.game = []
        self.points = []
        self.update_cards()
        self.extra_cards()

    def update_cards(self):
        card_one = Card()
        card_two = Card()
        self.game = [card_one, card_two]
        if self.game[0].name == 'A' and self.game[1].name == 'A':
            card_one.points = 1
        self.points = [card_one.points, card_two.points]   


    def printer(self):
        print_deck = []
        for x in range(7):
            patronus_string = ""
            for card in self.game:
                card_patronus = card.card_patronus()
                if len(card_patronus) > x:
                        patronus_string += card_patronus[x]
            print_deck.append(patronus_string)
            
        for y in print_deck:
            print(y)
            

    def a_checker(self):
        a_position = []
        x = 0
        for card in self.game:
            if card.name == 'A':
                a_position.append(x)
            x += 1

        if not a_position:
            return [False]
        else:
            return [True, a_position] 


    def extra_cards(self):
        self.printer()

        while sum(self.points) < 21:
            more_cards = input('Want a card? [y/n]')
            
            if more_cards == 'y' or more_cards == 'Y':
                new_card = Card()
                self.game.append(new_card)
                self.points.append(new_card.points)
                a_check = self.a_checker()
                if a_check[0] == True:
                    for x in a_check[1]:
                        if sum(self.points) > 21:
                            self.points[x] = 1
                self.printer()
                    
            
            elif more_cards == 'n' or more_cards == 'N':
                break
            
            else:
                continue



class House:

    def __init__(self):
        self.type = 'BOT'
        self.name = 'HOUSE'
        self.game = []
        self.points = []
        self.update_cards()
        self.extra_cards()

    def update_cards(self):
        card_one = Card()
        card_two = Card()
        self.game = [card_one, card_two]
        if self.game[0].name == 'A' and self.game[1].name == 'A':
            card_one.points = 1
        self.points = [card_one.points, card_two.points]
    
    def printer(self):
        print_deck = []
        for x in range(7):
            patronus_string = ""
            for card in self.game:
                card_patronus = card.card_patronus()
                if len(card_patronus) > x:
                        patronus_string += card_patronus[x]
            print_deck.append(patronus_string)
            
        for y in print_deck:
            print(y)

    def a_checker(self):
        a_position = []
        x = 0
        for card in self.game:
            if card.name == 'A':
                a_position.append(x)
            x += 1

        if not a_position:
            return [False]
        else:
            return [True, a_position]     


    def extra_cards(self): 

        while sum(self.points) < 12:
            new_card = Card()
            self.game.append(new_card)
            self.points.append(new_card.points)
            a_check = self.a_checker()
            if a_check[0] == True:
                for x in a_check[1]:
                    if sum(self.points) > 21:
                        self.points[x] = 1
        

        if sum(self.points) < 18 and discarded.count(13) >= 2 and discarded.count(12) >= 2 and discarded.count(11) >= 2 and discarded.count(10) >= 2 and discarded.count(9) >= 2 and discarded.count(8) >= 2:  
            new_card = Card()
            self.game.append(new_card)
            self.points.append(new_card.points)
            a_check = self.a_checker()
            if a_check[0] == True:
                for x in a_check[1]:
                    if sum(self.points) > 21:
                        self.points[x] = 1


def game():

    player = Player()
    house = House()

    if sum(player.points) > sum(house.points) and sum(player.points) <= 21:
        winnerwinnerchickendinner = name  + ' WINS'

    elif sum(house.points) > sum(player.points) and sum(house.points) <= 21:
        winnerwinnerchickendinner = 'THE HOUSE WINS'

    elif sum(player.points) > 21 and sum(house.points) < 21: 
        winnerwinnerchickendinner = 'THE HOUSE WINS'

    elif sum(house.points) > 21 and sum(player.points) < 21:
        winnerwinnerchickendinner = name  + ' WINS' 

    elif sum(house.points) == sum(player.points) and sum(house.points) <= 21 and sum(player.points) <= 21:
        winnerwinnerchickendinner = 'IT\'S A TIE'

    elif sum(player.points) > 21 and sum(house.points) > 21:
        winnerwinnerchickendinner = 'BOTH LOSE THE ROUND'

    else:
        print('It seems to be a problem, please try again another time.')
        sys.exit()
    
    def name_string(str1 = name, str2 = house.name):
        max_length = max(len(str1), len(str2))
        str1 = str1.rjust(max_length)
        str2 = str2.rjust(max_length)
        return str1, str2
    
    print('''

    ''')

    player.printer()
    print('''
                  {player} : {p_points}'''.format(player = name_string()[0] , p_points = sum(player.points)))
    
    
    print('''                  {house} : {h_points}
      '''.format(house = name_string()[1], h_points = sum(house.points)))
    house.printer()
     
    print(''' 

       {round}


      '''.format(round = winnerwinnerchickendinner))


name = input('Type your name: ').upper()
winnerwinnerchickendinner = ""

while len(discarded) < 53:
  if len(discarded) > 48:
    discarded.clear()
    repeated.clear()

  keep_going = input('BET? [y/n]')

  if keep_going == 'n' or keep_going == 'N':
    print('''

LEAVING THE TABLE...
      
      
      ''')
    sys.exit()
    
  elif keep_going == 'y' or keep_going == 'Y':
    game()

"""
    * Display result aesthetic
    * If more than 5 cards, print double line
"""


game()