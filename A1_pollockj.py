import random
def roll_dice():
   """
   Accesses a dictionary with the body parts as the values and prints the corresponding number on dice,
   which informs the player of their part
   :return: none
   """
   parts = {1: "body", 2: "head", 3: "two legs", 4: "eye", 5: "feeler", 6: "tail"}
   x = random.randint(1,6)  #A die has 6 sides so the number ranges from 1 to 6
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
        return True # Lets the player roll again
    else:
        return False # Ends the players turn

def is_complete (player):
    xlist = {"body", "head", "two legs", "two legs", "two legs", "eye", "eye", "feeler","feeler", "tail"}
    if player == xlist:
        "You have all the beetle parts you have WON!!!!!"
        return True
    else:
        return False

def main():
    P1 = []
    P2 = []
    current_player = P1
    print("Welcome to BEETLE THE GAME\nThis is a one player game of luck to see if you can get all the beetle parts before the computer")
    while len(current_player) <10:
        if current_player == P1:
            x = input("type roll in order to roll the dice")
            if x == "roll":
                new_part = roll_dice()
                play_again = addmethod(check(new_part,P1), new_part, P1)
                print("you rolled a ",new_part)
                print("and your beetle currently has ", P1)
                if play_again == True:
                    current_player = P1
                elif play_again == False:
                    current_player = P2
        elif current_player == P2:
            p2_new_part = roll_dice()
            play_again = addmethod(check(p2_new_part,P2), p2_new_part, P2)
            print("the computer rolled a ", p2_new_part)
            print("the computer's beetle currently has ", P2)
            if play_again == True:
                    current_player = P2
            elif play_again == False:
                    current_player = P1
        is_complete (current_player)
#asdfasd
main()
