
import random
parts = {1:"body", 2:"head", 3:"legs", 4:"eyes", 5:"feeler", 6:"tail"}


def roll_dice():
   """
   Accesses a dictionary with the body parts as the values and prints the corresponding number on dice,
   which informs the player of their part
   :return: none
   """
   x =random.randint(1,6)  #A die has 6 sides so the number ranges from 1 to 6
   print("You rolled " + str(x)) #Informs the player of their number
   print(parts.get(x)) #Uses the dictionary to find the corresponding part and relays that information to the user

def is_complete (player):
    xlist = {"body", "head", "legs", "legs", "legs", "eye", "eye", "feeler","feeler", "tail"}
    if player == xlist:
        is_complete = True
    else:
        is_complete = False


def main():
    roll_dice()
    is_complete()

def addmethod(NewPart_String):
    """Checks if the "check" is True. If it is it will append it to the player's part's list,
    if False, will end the players turn.
    :return: end_turn
    """
    if check == True:
        playerlist.append(NewPart_String) #Appends to the players list
    else:
        return end_turn # Ends the players turn



main()
