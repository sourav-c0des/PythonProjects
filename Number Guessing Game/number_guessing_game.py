n=18
no_of_guesses = 1
print("Welcome to the Number Guessing Game")
print("So Let's see whether you can guess the number or not!!!")
print("You Have 5 chances left")


while(no_of_guesses <= 5):
    number = int(input("Guess the number : \n "))
    if number < 16:
        print("You guessed a lesser number.Please guess a higher number ")
    elif number == 17:
        print("Pheww!!!You are very close")
    elif number == 19:
        print("Pheww!!!You are very close")
    elif number > 20:
        print("You guessed a higher number.Please guess a lower number ")
    elif number == 18:
        print("Congrats.You won the game!!!!!!")
        print("You have finished the game in",no_of_guesses,"attempt")
        break
    else :
        print("Enter a number only")

    print(5-no_of_guesses, "chance left")
    no_of_guesses = no_of_guesses + 1

if(no_of_guesses>5):
    print("The correct number was ",n,"." ,end = " " )
    print("Sorry,You Lost the game! Please try again!")


