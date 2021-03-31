import random

number = random.randint(1,20)
guesses_taken = 0

print("What's your name? ")
my_name = input()
print(f"Well hi {my_name}, I'm thinking of a number between 1 and 20 \n Can you guess what that number is?")

label=1
while guesses_taken < 6:
    print ('Take a guess:')
    guess = int(input())
    guesses_taken += 1
    if guess < number:
        print("Your guess is lower than the number I have in mind")
        
    elif guess > number:
        print("Your guess is higher than the number I have in mind")

    elif guess == number:
        print(f"Good job, {my_name}! You guessed my number in just {guesses_taken} guesses!")
        print("Would you like to play again? (yes/no)")
        answer = input()
        if answer == "yes" or "y":
           print ("ok")
        elif answer == "no" or answer == "n":
            print("ok bye bye")
            break
       

print(f"I'm afraid you have run out of guesses {my_name}")
print("Would you like to play again? (yes/no)")
answer = input()
if answer == "yes" or answer == "y":
    print ("ok")
elif answer == "no" or "n":
    break
    print("ok bye bye")
    

