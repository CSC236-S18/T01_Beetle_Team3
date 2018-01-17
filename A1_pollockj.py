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

def main():
    roll_dice()

main()
