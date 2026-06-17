import random

while (True):
    choice = int(input("enter difficulty level (1/2/3) 4 for exit: "))
    if choice == 1:
        target_num = random.randint(1, 50)
        guesses = 0
        while (True):
            num = int(input("guess a number between 1 and 50: "))
            guesses = guesses + 1
            if num > target_num:
                print("too high")
            elif num < target_num:
                print("too low")
            else:
                print("congratulations")
                print(f"your total guesses were {guesses}")
                break
            
    elif choice == 2:
        target_num = random.randint(1, 100)
        guesses = 0
        while (True):
            num = int(input("guess a number between 1 and 100: "))
            guesses = guesses + 1
            if num > target_num:
                print("too high")
            elif num < target_num:
                print("too low")
            else:
                print("congratulations")
                print(f"your total guesses were {guesses}")
                break

    elif choice == 3:
        target_num = random.randint(1, 500)
        guesses = 0
        while (True):
            num = int(input("guess a number between 1 and 500: "))
            guesses = guesses + 1
            if num > target_num:
                print("too high")
            elif num < target_num:
                print("too low")
            else:
                print("congratulations")
                print(f"your total guesses were {guesses}")
                break


    elif choice == 4:
        break

    else:
        print("enter a valid choice")
        break

    