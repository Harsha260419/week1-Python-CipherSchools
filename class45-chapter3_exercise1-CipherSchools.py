import random
winning_number = random.randint(0, 20)
print(winning_number)
guess = int(input("guess any number between 0 and 20: "))
if guess == winning_number:
    print("you win")
elif guess <= winning_number:
    print("oh your guess was too low")
else:
    print("oh your guess was too high")
# you can also solve this question by nested if else which is you can write if statement inside else statement
