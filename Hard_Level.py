import sys
def trying_again():
    print("Do you want to try again ?")
    print("Type 'y' and hit enter for trying again !")
    print("Yype 'n' and hit enter for exiting !")
    ys = input("Enter your choice: ")
    if ys == "y" or ys == "Y":
        hard_level()
    elif ys == "n" or ys == "N":
        print("Exiting............")
        sys.exit()
    else:
        print("Sorry we didn't understood you! ")
        trying_again()
def hard_level():
    import random
    import string
    random_string = ""
    letters = string.ascii_lowercase
    print("\t\t\t\tWelcome To The Game!")
    for x in range(6):
        random_string = random_string + random.choice(letters)
    print("The string contains {} letters".format(len(random_string)))
    print("Hint the 1st letter is {}".format(random_string[0]))
    print("Hint the 2nd letter is {}".format(random_string[1]))
    print("Hint the 4th letter is {}".format(random_string[3]))
    print("Hint the 6th letter is {}".format(random_string[5]))
    print("You need to find the correct letter for 3rd and 5th letter! ")
    for x in range(100):
        user_input = input("Enter your guess: ")
        if len(user_input) < 6:
            print("Error !")
            print("You need to enter 6 letters by combining them with letter's that are given as hints, With your guessed letter's !")
            hard_level()            
        elif len(user_input) > 6:
            print("Error!")
            print("You need to enter 6 letters only !")
            hard_level()
        if user_input == random_string:
            print("Correct! You did it !")
            print("You do have a high level of I.Q !")
        elif user_input != random_string:
            print("Wrong !")
            print("Try again!")
    print("Out of tries !")
    print("Thank for trying !")
    trying_again()
hard_level()