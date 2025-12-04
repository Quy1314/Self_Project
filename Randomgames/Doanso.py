import random

Secret = random.randint(0, 100)
guess = -1

while True:
    try:
        guess = int(input("Guess your number: "))
    except ValueError:
        print("Guess your number please!!")
        continue
    if guess == Secret:
        print(f"Congratulations!! Your secret is: {Secret}")
        break  
    elif guess > Secret:
        print("Guess smaller")
    else:  
        print("Guess bigger")

    