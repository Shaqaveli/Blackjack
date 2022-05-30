############### Blackjack Project #####################

import random
from replit import clear

def initialSetup():
  # Make Deck
  STARTING_DECK={
    "Ace of Clubs":11,
    "Two of Clubs":2,
    "Three of Clubs":3,
    "Four of Clubs":4,
    "Five of Clubs":5,
    "Six of Clubs":6,
    "Seven of Clubs":7,
    "Eight of Clubs":8,
    "Nine of Clubs":9,
    "Ten of Clubs":10,
    "Jack of Clubs":10,
    "Queen of Clubs":10,
    "King of Clubs":10,
    "Ace of Hearts":11,
    "Two of Hearts":2,
    "Three of Hearts":3,
    "Four of Hearts":4,
    "Five of Hearts":5,
    "Six of Hearts":6,
    "Seven of Hearts":7,
    "Eight of Hearts":8,
    "Nine of Hearts":9,
    "Ten of Hearts":10,
    "Jack of Hearts":10,
    "Queen of Hearts":10,
    "King of Hearts":10,
    "Ace of Spades":11,
    "Two of Spades":2,
    "Three of Spades":3,
    "Four of Spades":4,
    "Five of Spades":5,
    "Six of Spades":6,
    "Seven of Spades":7,
    "Eight of Spades":8,
    "Nine of Spades":9,
    "Ten of Spades":10,
    "Jack of Spades":10,
    "Queen of Spades":10,
    "King of Spades":10,
    "Ace of Diamonds":11,
    "Two of Diamonds":2,
    "Three of Diamonds":3,
    "Four of Diamonds":4,
    "Five of Diamonds":5,
    "Six of Diamonds":6,
    "Seven of Diamonds":7,
    "Eight of Diamonds":8,
    "Nine of Diamonds":9,
    "Ten of Diamonds":10,
    "Jack of Diamonds":10,
    "Queen of Diamonds":10,
    "King of Diamonds":10,
  }
  # Make empty starting hands
  EMPTY_PLAYER_HAND={}
  EMPTY_DEALER_HAND={}
  return STARTING_DECK, EMPTY_PLAYER_HAND, EMPTY_DEALER_HAND

# -----------------------------------------------------------------------------------------------------

def drawPhase(current_deck,current_player_hand,current_dealer_hand):
  # Draw a new card for the player and delete that card from the deck. Then do the same for the dealer
  newplayercard=random.choice(list(current_deck))
  current_player_hand[newplayercard]=current_deck[newplayercard]
  current_player_hand[newplayercard]=current_deck[newplayercard]
  del current_deck[newplayercard]
  newdealercard=random.choice(list(current_deck))
  current_dealer_hand[newdealercard]=current_deck[newdealercard]
  del current_deck[newdealercard]
  return current_deck, current_player_hand, current_dealer_hand
  
# -----------------------------------------------------------------------------------------------------

def displayField(current_player_hand, current_dealer_hand):
  clear()
  print("\n\nYour hand is:", end="  ")
  # Convert player hand into a key:value tuples with items() method, create list of items in format card "of value" value ", " for nicer display, unpack that list with * and print the result
  print(*[card + ' of value ' + str(value) + ", " for card,value in current_player_hand.items()])
  # Create a dealer hand with the most recently drawn card hidden
  hidden_dealer_hand=list(current_dealer_hand.items())
  # hidden_dealer_hand[len(hidden_dealer_hand)-1]=["", ""]
  del hidden_dealer_hand[len(hidden_dealer_hand)-1]
  # Print the dealer hand with the most recently drawn card hidden
  print("\nThe dealer hand is:", end=" ")
  print(*[card + " of value " + str(value) + ", " for card,value in hidden_dealer_hand ])
  return

# -----------------------------------------------------------------------------------------------------

def bustCheck(current_player_hand):
  # Add up all the cards in the player's hand
  total=0
  for card,value in current_player_hand.items():
    total+=value
  # If player busted, check for Aces valued at 11 in their hand, and if any are found change the value to 11
  if total>21:
    aceExisted=False
    for card,value in current_player_hand.items():
      if value==11:
        current_player_hand[card]=1
        aceExisted=True
        break
    if not aceExisted and total>21:
      return True
    # Check again if player busted after changing out first Ace
    if bustCheck(current_player_hand):
      return True
    else:
      return False
  elif total<21:
    return False

# -----------------------------------------------------------------------------------------------------

def endGameScreen(playerBust,current_player_hand,current_dealer_hand):
  clear()
  # Print final hands
  print("\n\nYour final hand is:", end="  ")
  print(*[card + ' of value ' + str(value) + ", " for card,value in current_player_hand.items()])
  print("\n\nThe dealer's final hand is:", end="  ")
  print(*[card + ' of value ' + str(value) + ", " for card,value in current_dealer_hand.items()])
  if playerBust==True:
    print("\nYou lose. \nYa Loser")
  else:
    playertotal=0
    for card,value in current_player_hand.items():
      playertotal+=value
    dealertotal=0
    for card,value in current_dealer_hand.items():
      dealertotal+=value
    if (playertotal>dealertotal and dealertotal<21) or (dealertotal>21):
      print("You win I guess")
    elif playertotal==dealertotal:
      print("It's a draw!")

# -----------------------------------------------------------------------------------------------------

def gameLoop():
  # Set up decks and hands to start game
  current_deck,current_player_hand,current_dealer_hand=initialSetup()
  # Draw two cards for player and for dealer
  for carddraw in range(2):
    current_deck, current_player_hand, current_dealer_hand=drawPhase(current_deck, current_player_hand, current_dealer_hand)
  newRound=True
  while newRound:
    playerBust=bustCheck(current_player_hand)
    displayField(current_player_hand, current_dealer_hand)
    if playerBust:
      newRound=False
      endGameScreen(playerBust,current_player_hand,current_dealer_hand)
    else:
      errorCheck=True
      while errorCheck==True:
        hitMe=input("\nWould you like to draw another card or stay ?\nEnter draw or stay: ").lower()
        if hitMe=="draw":
          current_deck, current_player_hand, current_dealer_hand=drawPhase(current_deck, current_player_hand, current_dealer_hand)
          errorCheck=False
        elif hitMe=="stay":
          errorCheck=False
          newRound=False
          endGameScreen(playerBust, current_player_hand, current_dealer_hand)
        else:
          print("Invalid input")
      
# -----------------------------------------------------------------------------------------------------



gameLoop()
