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
# Calculate a player's current score
def getScore(hand):
  score=0
  for card,value in hand.items():
    score+=value
  return score

# ----------------------------------------------------------------------------------------------------

def drawPhase(current_deck,current_player_hand,current_dealer_hand):
  # Draw a new card for the player and delete that card from the deck. Then do the same for the dealer
  newplayercard=random.choice(list(current_deck))
  current_player_hand[newplayercard]=current_deck[newplayercard]
  current_player_hand[newplayercard]=current_deck[newplayercard]
  del current_deck[newplayercard]
  dealertotal=getScore(current_dealer_hand)
  # As a rule, the dealer does not draw any new cards if they have a score greater than 17
  if dealertotal<17:
    newdealercard=random.choice(list(current_deck))
    current_dealer_hand[newdealercard]=current_deck[newdealercard]
    del current_deck[newdealercard]
  return current_deck, current_player_hand, current_dealer_hand
  
# -----------------------------------------------------------------------------------------------------


def displayField(current_player_hand, current_dealer_hand):
  clear()
  playertotal=getScore(current_player_hand)
  print("\n\nYour hand is:", end="  ")
  # Convert player hand into a key:value tuples with items() method, create list of items in format card "of value" value ", " for nicer display, unpack that list with * and print the result
  print(*[card + ', value ' + str(value) + ", " for card,value in current_player_hand.items()])
  print(f"\nYour current score is: {playertotal}")
  dealertotal=getScore(current_dealer_hand)
  if dealertotal<17:
    # Create a dealer hand with the most recently drawn card facedown
    hidden_dealer_hand=list(current_dealer_hand.items())
    del hidden_dealer_hand[len(hidden_dealer_hand)-1]
    hidden_dealer_hand.append(("Facedown Card", "Hidden"))
    # Print the dealer hand with the most recently drawn card facedown
    print("\nThe dealer hand is:", end=" ")
    print(*[card + ", value " + str(value) + ", " for card,value in hidden_dealer_hand ])
    # Calculate a score, accounting for the fact that one card is face down
    hiddendealertotal=0
    for card,value in hidden_dealer_hand:
      if str(value).isdigit():
        hiddendealertotal+=value
    print(f"The dealer's current score is: {hiddendealertotal}")
  elif dealertotal>=17:
    print("\nThe dealer's final hand is:", end=" ")
    print(*[card + ", value " + str(value) + ", " for card,value in current_dealer_hand.items() ])
    print(f"The dealer's final score is: {dealertotal}")
  return

# -----------------------------------------------------------------------------------------------------

def bustCheck(current_player_hand):
  # Add up all the cards in the player's hand
  total=getScore(current_player_hand)
  # If the player's score is greater than 21, check for Aces valued at 11 in their hand, and if any are found change the value of the first one encountered to 1
  if total>21:
    aceExisted=False
    for card,value in current_player_hand.items():
      if value==11:
        current_player_hand[card]=1
        aceExisted=True
        break
    # If there are no aces to change value on and their score is still above 21, the player has busted
    if not aceExisted and total>21:
      return True
    # Check again if player busted after changing out first Ace
    if bustCheck(current_player_hand):
      return True
    else:
      return False
  # If the player's score is less than 21, they have not busted
  elif total<21:
    return False

# -----------------------------------------------------------------------------------------------------

def endGameScreen(playerBust,current_player_hand,current_dealer_hand):
  clear()
  playertotal=getScore(current_player_hand)
  dealertotal=getScore(current_dealer_hand)
  # Print final hands
  print("\n\nYour final hand is:", end="  ")
  print(*[card + ', value ' + str(value) + ", " for card,value in current_player_hand.items()])
  print(f"\nYour final score is: {playertotal}")
  print("\n\nThe dealer's final hand is:", end="  ")
  print(*[card + ', value ' + str(value) + ", " for card,value in current_dealer_hand.items()])
  print(f"The dealer's final score is: {dealertotal}")
  # If the player score is greater than 21, the player has busted and a game loss screen is printed. 
  if playerBust==True:
    print("\nYou lose!")
  # If neither the dealer nor the player has busted, check whether the player has won or drawn and print the appropriate screen.
  else:
    playertotal=getScore(current_player_hand)
    dealertotal=getScore(current_dealer_hand)
    if (playertotal>dealertotal and dealertotal<21) or (dealertotal>21):
      print("You win!")
    elif playertotal==dealertotal:
      print("It's a draw!")

# -----------------------------------------------------------------------------------------------------

def gameLoop():
  # Set up decks and hands to start game
  current_deck,current_player_hand,current_dealer_hand=initialSetup()
  # Draw two cards for player and for dealer to start the match.
  for carddraw in range(2):
    current_deck, current_player_hand, current_dealer_hand=drawPhase(current_deck, current_player_hand, current_dealer_hand)
  newRound=True
  # This loop allows the player to draw until they lose, the dealer loses or they choose to stay.
  while newRound:
    # Check if the player has busted
    playerBust=bustCheck(current_player_hand)
    displayField(current_player_hand, current_dealer_hand)
    # If the player has busted, end the game here.
    if playerBust:
      newRound=False
      endGameScreen(playerBust,current_player_hand,current_dealer_hand)
    # If the player has not busted, check if the dealer has busted instead.
    else:
      dealerBust=bustCheck(current_dealer_hand)
      # if the dealer has busted, end the game here.
      if dealerBust:
        newRound=False
        endGameScreen(playerBust,current_player_hand,current_dealer_hand)
      else:
        dealertotal=getScore(current_dealer_hand)
        playertotal=getScore(current_player_hand)
        # The dealer, as a rule, stops drawing cards if their total is between 17 and 21. Therefore, the player can win by default if the dealer's score is between 17 and 21 and the player has a greater score. This conditional automatically stops the game for the player in this situation. Similarly, if the player has exactly 21 the game is stopped regardless of what the dealer's score is.
        if (dealertotal>=17 and playertotal>dealertotal) or playertotal==21:
          newRound=False
          endGameScreen(playerBust, current_player_hand, current_dealer_hand)
        else:
          errorCheck=True
          # This loop validates player input.
          while errorCheck==True:
            hitMe=input("\nWould you like to draw another card or stay ?\nEnter draw or stay: ").lower()
            # When the player chooses to draw, a card is transferred from the deck to their hand. Unless the dealer's score is between 17 and 21, a card is also transferred from the deck to the dealer's hand.
            if hitMe=="draw":
              current_deck, current_player_hand, current_dealer_hand=drawPhase(current_deck, current_player_hand, current_dealer_hand)
              errorCheck=False
            # When the player chooses to stay, the game is ended and the dealer's facedown card is revealed.
            elif hitMe=="stay":
              errorCheck=False
              newRound=False
              endGameScreen(playerBust, current_player_hand, current_dealer_hand)
            else:
              print("Invalid input")
      
# -----------------------------------------------------------------------------------------------------



gameLoop()
