import random

# get random int 1-3
Lov = [None, "rock", "paper", "scissors"]
while True:
    Cpu = random.randint(1, 3)
    user = input("1.rock, 2.paper, 3.scissors?\n>>> ")
    user = int(user)

    if user == Cpu:
        print("draw!")
    else:
        result = user - Cpu
        if (result) < 1:
            result += 3
        if result == 1:
            print("you win!", Lov[user], "beats", Lov[Cpu])
        else:
            print("you lose!", Lov[Cpu], "beats", Lov[user])