import time,os


user_count = 0
def gamestart():
    print("Welcome to Rock, Paper, Scissors!")
    print("There will be three rounds between the player and computer.")
    os.system('clear')
   
def roundone():    
    user_choice = input("Choose one of the three options: \n1.) Rock \n2.) Paper \n3.) Scissors")
    if user_choice == "1":
        user_count =+ 1
        print("Computer choice = scissors")
        print("You won round one part one! \nPress enter to continue >")
    elif user_choice == "2":
        user_count = 0
        print("Computer choice = scissors")
        print("You lost round one part one. \nPress enter to continue >")
    elif user_choice == "3":
        user_count = 0
        print("Computer choice = scissors")
        print("You lost round one part one. \nPress enter to continue >")


    
