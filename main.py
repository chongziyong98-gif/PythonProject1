#CRAPS games

import random # pycharm's in-built random model

money = 1000

while money > 0:
    print(f"current amount: {money}")
    dept = int(input("enter your bid amount: "))
    if 0 <= dept <= money:
        first_point = random.randrange(1,7) + random.randrange(1,7)
        print(f"player roll {first_point} points")
        if first_point == 7 or first_point == 11:
            money += dept
            print("player wins")
        elif first_point == 2 or first_point == 3 or first_point == 12:
            money -= dept
            print("dealer wins")
        else:
            while True:
                second_point = random.randrange(1,7) + random.randrange(1,7)
                print(f"player roll {second_point} points")
                if second_point == 7:
                    money -= dept
                    print("dealer wins")
                    break
                elif second_point == first_point:
                    money += dept
                    print("player wins")
                    break

print("player bankruptcy, game over.")


