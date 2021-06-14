#Exercise 6 (Q-V40)
# Make a Snake-Water-Gun game.
# Use For/While loop
# Game is played between user and pc.
# Pc will get a random value using "random module" .
# User will get 10 opportunity to play the game.
# Whoever makes max no. of win out of 10 times will be the winner.
# Also print no. of wins made by user and pc.




#-----------------------------My mistake program!! Just ignore this!-----------------------------#
# import random
# gl=["snake","water","gun"]
# pcc=random.choice(gl)
# print(pcc)
#
#
# No_of_rounds_left=10
# No_of_win_By_PC=0
# No_of_win_By_User=0
#
# while(No_of_rounds_left > 1):
#
#     No_of_rounds_left= No_of_rounds_left - 1
#     print("Number of rounds left= ", No_of_rounds_left)
#     uc=input("Select your choice:", "\n +snake+", "\n +water+", "\n +gun+")
#     if(uc=="snake" and pcc=="water")or(uc=="water" and pcc=="snake")or(uc=="gun" and pcc=="snake"):
#     	No_of_win_By_User=No_of_win_By_User+1
#     	print("Congrats u have won this round!!")
#         print("Number of win made by user= ",No_of_win_By_User )
#
#     elif(pcc=="snake" and uc=="water") or (pcc=="water" and uc=="snake") or (pcc=="gun" and uc=="snake"):
#         No_of_win_By_PC=No_of_win_By_PC+1
#         print("O!! You have lost this round!! Better luck next round..")
#         print("Number of win made by user= ", No_of_win_By_PC)
#     else:
#         continue
# if No_of_win_By_User>No_of_win_By_PC:
#     print("Hurray!! you are the winner of this game and  your total no. of wins =",No_of_win_By_User")
# elif No_of_win_By_User==No_of_win_By_PC:
#     print("It's a tie try again")
# else:
#     print("You have lost this game!! Better luck next time.. and the total no. of win by pc= ",No_of_win_By_PC")

#-----------------------------My mistake program!! Just ignore this!-----------------------------#








No_of_rounds_left=10
No_of_win_By_PC=0
No_of_win_By_User=0

while(No_of_rounds_left > 0):
    import random

    gl = ["snake", "water", "gun"]
    pcc = random.choice(gl)
    print("\nRandom choice made by pc= ",pcc)               #To check the choice made by pc

    print("\nNumber of rounds left= ", No_of_rounds_left)
    No_of_rounds_left= No_of_rounds_left - 1
    print("Select your choice:", "\n [+]snake", "\n [+]water", "\n [+]gun")
    uc = input("Enter= ")
    if(uc=="snake" and pcc=="water")or(uc=="water" and pcc=="gun")or(uc=="gun" and pcc=="snake"):
        No_of_win_By_User=No_of_win_By_User+1
        print("Congrats u have won this round!!", "\nNumber of win made by user= ", No_of_win_By_User)
        #print("Number of win made by user= ",No_of_win_By_User )

    elif(pcc=="snake" and uc=="water") or (pcc=="water" and uc=="gun") or (pcc=="gun" and uc=="snake"):
        No_of_win_By_PC=No_of_win_By_PC+1
        print("O!! You have lost this round!! Better luck next round..","\nNumber of win made by PC= ",No_of_win_By_PC)
        #print("Number of win made by PC= ", No_of_win_By_PC)
    else:
        print("Your choice is = Pc choice")
        continue

if No_of_win_By_User>No_of_win_By_PC:
    print("\nHurray!! you are the winner of this game")
elif No_of_win_By_User==No_of_win_By_PC:
    print("\nIt's a tie,... try again!")
else:
    print("\nYou have lost this game!! Better luck next time.. ")
print("Your total no. of wins =",No_of_win_By_User)
print("The total no. of win by pc= ",No_of_win_By_PC)




# print("Congrats u have won this round!!","\nNumber of win made by user= ",No_of_win_By_User , "pc choice=",pcc )

