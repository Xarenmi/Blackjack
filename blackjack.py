import random
import sys

discarded = []

# Correct when trows double 'A' and takes default value 22 + Add more players? 
class Card:

  def __init__(self):
    self.info = self.trow_card()
    self.index = self.info[0]
    self.name = self.info[1][0]
    self.points = self.info[1][1]


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
    13:['K', 10]
    }

    card = index.get(temp_index)
    discarded.append(temp_index)
    return [temp_index, card] 



class Player:

  def __init__(self):
    self.type = 'PLAYER'
    self.name = ''
    self.game = []
    self.points = []
    self.update_cards()

  def update_cards(self):
    card_one = Card()
    card_two = Card()
    self.game = [card_one.name, card_two.name]
    self.points = [card_one.points, card_two.points]

  def a_checker(self):
    a_position = []
    for x in range(len(self.game)):
      if self.game[x] == 'A':
        a_position.append(x)

    if not a_position:
      return [False]
    else:
      return [True, a_position]    


  def extra_cards(self): 

      print(self.game)
      
      while sum(self.points) < 21:
        more_cards = input('Want a card? [y/n]')
        
        if more_cards == 'y' or more_cards == 'Y':
          new_card = Card()
          self.game.append(new_card.name)
          self.points.append(new_card.points)
          a_check = self.a_checker()
          if a_check[0] == True:
            for x in a_check[1]:
              if sum(self.points) > 21:
                self.points[x] = 1
          print(self.game)
                
        
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

  def update_cards(self):
    card_one = Card()
    card_two = Card()
    self.game = [card_one.name, card_two.name]
    self.points = [card_one.points, card_two.points]

  def a_checker(self):
    a_position = []
    for x in range(len(self.game)):
      if self.game[x] == 'A':
        a_position.append(x)

    if not a_position:
      return [False]
    else:
      return [True, a_position]    


  def extra_cards(self): 

      while sum(self.points) < 12:
        new_card = Card()
        self.game.append(new_card.name)
        self.points.append(new_card.points)
        a_check = self.a_checker()
        if a_check[0] == True:
          for x in a_check[1]:
            if sum(self.points) > 21:
              self.points[x] = 1
        

      if sum(self.points) < 18 and discarded.count(13) >= 2 and discarded.count(12) >= 2 and discarded.count(11) >= 2 and discarded.count(10) >= 2 and discarded.count(9) >= 2 and discarded.count(8) >= 2:  
        new_card = Card()
        self.game.append(new_card.name)
        self.points.append(new_card.points)
        a_check = self.a_checker()
        if a_check[0] == True:
          for x in a_check[1]:
            if sum(self.points) > 21:
              self.points[x] = 1



def game():

      player = Player()
      player.extra_cards()
      house = House()
      house.extra_cards()

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

      print('''
      ----------------------
      {player} 
      {p_game}: {p_points}

      {house}
      {h_game}: {h_points}
      ----------------------
      {round}
      '''.format(p_game = player.game, player = name , p_points = sum(player.points), h_game = house.game, house = house.name, h_points = sum(house.points), round = winnerwinnerchickendinner))



name = input('Type your name: ').upper()
winnerwinnerchickendinner = ""

while len(discarded) < 53:
  if len(discarded) > 48:
    discarded.clear()

  keep_going = input('BET? [y/n]')

  if keep_going == 'n' or keep_going == 'N':
    print('''
      LEAVING THE TABLE
    ----------------------''')
    sys.exit()
    
  elif keep_going == 'y' or keep_going == 'Y':
    game()

# Note: print(Player()) <-- Returns none since there's nothing to return, so it's better --> Player() as long as it prints by itself