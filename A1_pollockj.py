
import random

def roll_dice():
   """
   Accesses a dictionary with the body parts as the values and prints the corresponding number on dice,
   which informs the player of their part
   :return: none
   """
   parts = {1: "body", 2: "head", 3: "two legs", 4: "eye", 5: "feeler", 6: "tail"}
   x = random.randint(1,6)  #A die has 6 sides so the number ranges from 1 to 6
   print("You rolled " + str(x)) #Informs the player of their number
   print(parts.get(x)) #Uses the dictionary to find the corresponding part and relays that information to the user
   return (parts .get(x))
def check(New_Part, Player):
    """
    :param Player: List of body parts already assigned
    :param New_Part: After the dice has been rolled and a new part is picked under the stipulations presented.
    :return: True or False based on the check
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



def addmethod(Check, New_part, playerlist):
    """Checks if the "check" is True. If it is it will append it to the player's part's list,
    if False, will end the players turn.
    :return: end_turn
    """

    if Check == True:
        playerlist.append(New_part) #Appends to the player's list
        print("You've collected a ", New_part)
        return True # Lets the player roll again
    else:
        return False # Ends the players turn



def is_complete (player):
    xlist = {"body", "head", "legs", "legs", "legs", "eye", "eye", "feeler","feeler", "tail"}
    if player == xlist:
        "You have all the beetle parts you have WON!!!!!"
        return True
    else:
        return False


def main():
    P1 = []
    P2 = []
    print("Welcome to BEETLE THE GAME\nThis is a one player game of luck to see if you can get all the beetle parts before the computer")
    x = input("type roll in order to roll the dice")
    if x == "roll":
        print("asdfasdfa")
main()
#nopey
