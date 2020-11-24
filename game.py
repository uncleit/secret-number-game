import random
secret = random.randint(1, 30)

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))

    if guess == secret:
        print("You've guessed it - congratulations! It's number 22.")
        break
    else:
        if (guess < secret):
          print("The secret number is higher that your guess.")
        else:
          print("The secret number is lower that your guess.")          
