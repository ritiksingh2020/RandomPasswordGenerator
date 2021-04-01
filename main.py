import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# 0-Stands for Rock
# 1-Stands for Paper
# 2-Stands for Scissor
###############################################################################################################################
                                   ######## For User Instructions ###########
###############################################################################################################################
print("Let's Begin the Game\n\n\n")
print("                           RULES              \n\n")
print("1->Rock wins against scissors.\n\n2->Scissors win against paper.\n\n3->Paper wins against rock.\n\n")
print("0 or R-Stands for Rock")
print("1 or P-Stands for Paper")
print("2 or S-Stands for Scissor")
print("\n\nEnter your Choice")
player_choice=input()
computer_choice=random.randint(0,2)
###############################################################################################################################
                                   ######## Printing the choices by the players ###########
###############################################################################################################################
print("\nYour Choice")
if(player_choice in ['R','0']):
    print(rock)
elif(player_choice in ['P','1']):
    print(paper)
else:
    print(scissors)
print("\nComputer Choice")
if(computer_choice==0):
    print(rock)
elif(computer_choice==1):
    print(paper)
else:
    print(scissors)
###############################################################################################################################
                                   ######## User has selected the Rock ###########
###############################################################################################################################
if(player_choice=='0' or player_choice=='R'):
    if(computer_choice==0):
        print("DRAW")
    elif(computer_choice==1):
        print("You Lose the game")
    else:
        print("You Win the game")
###############################################################################################################################
                                   ######## User has selected the Paper ###########
###############################################################################################################################
elif(player_choice=='1' or player_choice=='P'):
    if(computer_choice==0):
        print("You Win the game")
    elif(computer_choice==1):
        print("DRAW")
    else:
        print("You Lose the game")
###############################################################################################################################
                                   ######## User has selected the Scissor ###########
###############################################################################################################################
else:
    if(computer_choice==0):
        print("You Lose the game")
    elif(computer_choice==1):
        print("You Win the game")
    else:
        print("DRAW")