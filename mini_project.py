# Mini Project Of stone , paper ,scissor game

comp_win = 0
player_win = 0
num = 1

import random

#user choice
def choose():
    user_choice=(input("choose Rock🧱, Paper📝, scissor✂️:"))
    if user_choice in ["r", "R", "rock", "Rock", "ROCK"]:
        user_choose="r"
    elif user_choice in ["p", "P", "Paper", "paper", "PAPER"]:
        user_choice= "p"
    elif user_choice in ["s", "S", "Scissor", "scissor", "SCISSOR"]:
       user_choice= "s"
    else:
       print("Invalid Input. TRY AGAIN")
       choose()
    return(user_choice)

#computer return

def comp_option():
    comp_choice=random.randint(1,3)
    if comp_choice== 1:
        comp_choice="r"
    elif comp_choice== 2:
        comp_choice="p"
    else:
       comp_choice="s"
    return(comp_choice)


while True:
    print("*****************************************************************************")
    print("TURN: "+str(num))
    num +=1;
    user_choice = choose()
    comp_choice = comp_option()
    print("")
    if user_choice == "r":
        if comp_choice == "r":
            print("You entered rock🧱.Computer also choose rock🧱.so, The match is TIE")
        elif comp_choice == "p":
             print("You entered rock🧱.Computer choose paper📝.")
             comp_win += 1
        elif comp_choice == "s":
             print("You entered rock🧱.Computer choose scissor✂️.")
             player_win += 1
    elif user_choice == "p":
        if comp_choice == "r":
          print("You entered paper📝.Computer choose rock🧱.")
          player_win += 1
        elif comp_choice == "p":
          print("You entered paper📝.Computer also choose paper📝.so, The match is TIE")
        elif comp_choice == "s":
          print("You entered paper📝.Computer  choose Scissor✂️.")
          comp_win += 1
    elif user_choice == "s":
        if comp_choice == "r":
            print("You entered Scissor✂️.Computer choose rock🧱.")
            comp_win += 1
        elif comp_choice == "p":
           print("You entered Scissor✂️.Computer choose paper📝.")
           player_win += 1
        elif comp_choice == "s":
          print("You entered Scissor✂️.Computer also choose Scissor✂️.so, The match is TIE.")
    print("🧍‍ Player score:"+str(player_win))
    print("🖥️ Computer score:"+str(comp_win))
    user_choice=(input("Do you want to play again 🤔? (y/n)"))
    if user_choice in ["y", "Y", "YES", "yes", "Yes"]:
       pass
    elif user_choice in ["n", "N", "No" , "NO", "no"]:
        print("*****************************************************************************")
        print("🤞🏻 🤞🏻Final Result is:")
        if player_win>comp_win:
           print("Congratulation🎉🎉You Won The Match")
           print("Your Score is:"+str(player_win))
        elif player_win == comp_win :
           print("Match is TIE🎊🎊.")
        else:
           print("You Losses The Match😭😭.")
        break
    else:
       print("*****************************************************************************")
       print("🤞🏻 🤞🏻Final Result is:")
       if player_win>comp_win:
          print("Congratulation🎉🎉 You Won The Match")
          print("Your Score is:"+str(player_win))
       elif player_win == comp_win :
          print("Match is TIE🎊🎊.")
       else:
          print("You Losses The Match 😭😭.")
       break
