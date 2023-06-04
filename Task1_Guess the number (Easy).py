Game = True
while Game:
    points = 100
    import random
    name_user = input("Enter your name: ")
    low = int(input("Enter the lower range: "))
    high = int(input("Enter the higher range: "))
    random_no = random.randint(low,high)
    control = True
    while control:
        guess_user = int(input("Enter your guess: "))
        if guess_user > random_no:
            print("Too high")
            points -= 5
            print(f"Your points are: {points}")
        elif guess_user == random_no:
            print("Your guess is correct! You win") 
            print("GAME OVER!!!")
            control = False
            k = input("would you like to play again?(YES or NO): ")
            if k == "NO":
                Game = False  
        else:
            print("Too low")
            points -= 5
            print(f"Your points are: {points}")
        if points == 0:
            control = False

    
