import random
import time

print("Welcome to my guessing game! From a list of 25 numbers, guess the value of a number within 1 to 25.")
time.sleep(1)

def main():
    random_list = []
    for i in range(1, 26):
        random_number = random.randint(1, 26)
        random_list.append(random_number)

    play_game = input("Select the index of the number you want to guess.")

    if play_game.isdigit():
        play_game = int(play_game)

    if play_game > len(random_list):
        print("Invalid entry! Try again!")
        time.sleep(1)
        main()

    print("The number you're guessing is at index "+ str(play_game))
    number_guess = random_list[play_game-1]
    x = 1

    def guess(x):

        guess_num = input("Guess the number!")
        if guess_num.isdigit():
            guess_num=int(guess_num)

        if x == 10 and (guess_num > number_guess or guess_num < number_guess):
            print("Game over!")
        else:
            if guess_num > number_guess:
                print("Go lower! " + str(10-x) + " attempts left!")
                x += 1
                guess(x)

            if guess_num < number_guess:
                print("Go higher!"  + str(10-x) + " attempts left!")
                x += 1
                guess(x)

            if guess_num == number_guess:
                print("Congratulations! You've guessed the number!")
                print(random_list)
                play_again = input("Would you like to play again? (Y/N)")
                if play_again == "Y":
                    main()
                if play_again == "N":
                    print("Thank you for playing!")
    guess(x)
    
if __name__ == "__main__":
    main()
