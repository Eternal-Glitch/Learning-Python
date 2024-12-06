import random 

guide = {0:"Rock", 1:"Paper", 2:"Scissor"}
game = [[0,2,1],[1,0,2],[2,1,0]]
P = 0
C = 0
while True:
    for i in range (0, 40):
        print("-", end = "")
    print("\nChoose your weapon:\n 1. Rock\n 2. Paper\n 3. Scissors\n 4. Exit")
    computer = random.randint(0,2)
    player = int(input()) - 1
    if player == 3:
        print("\nGame Over!")
        break
    ans = game[player][computer]
    print(f"Player chose {guide[player]}, Computer chose {guide[computer]}")
    if ans == 1:
        print("You win!")
        P += 1
    elif ans == 2:
        print("You lost")
        C += 1
    else:
        print("It's a tie!")
    print(f"\nScore:\nPlayer: {P}\nComputer: {C}")

