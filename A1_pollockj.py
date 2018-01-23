
import random
parts = {1:"body", 2:"head", 3:"two legs", 4:"eyes", 5:"feeler", 6:"tail"}


def roll_dice():
   """
   Accesses a dictionary with the body parts as the values and prints the corresponding number on dice,
   which informs the player of their part
   :return: none
   """
   x = random.randint(1,6)  #A die has 6 sides so the number ranges from 1 to 6
   print("You rolled " + str(x)) #Informs the player of their number
   print(parts.get(x)) #Uses the dictionary to find the corresponding part and relays that information to the user


def check(New_Part, Player):
    """
    :param Player:
    :param New_Part:
    :return:
    """
    if New_Part == "body":
        if "body" in Player:
            return False
        else:
            return True
    if "body" in Player:
        if New_Part == "head":
            if "head" in Player:
                return False
            else:
                return True
        if New_Part == "two legs":
            if Player.count("two legs") >= 3:
                return False
            else:
                return True
        if New_Part == "tail":
            if "tail" in Player:
                return False
            else:
                return True
    if "head" in Player:
        if New_Part == "eye":
            if Player.count("eye") >= 2:
                return False
            else:
                return True
        if New_Part == "feeler":
            if Player.count("feeler") >= 2:
                return False
            else:
                return True
    else:
        return False

print (check())


def addmethod(NewPart_String):
    """Checks if the "check" is True. If it is it will append it to the player's part's list,
    if False, will end the players turn.
    :return: end_turn
    """

    if check == True:
        playerlist.append(NewPart_String) #Appends to the players list
    else:
        return end_turn # Ends the players turn



def is_complete (player):
    xlist = {"body", "head", "legs", "legs", "legs", "eye", "eye", "feeler","feeler", "tail"}
    if player == xlist:
        is_complete = True
    else:
        is_complete = False


