from random import randint

roshambo = ["rock", "paper", "scissors"]
player1 = input("Enter Player 1 name: ")
player2 = input("Enter Player 2 name: ")

lastvalue = len(roshambo) - 1

index1 = randint(0, lastvalue)
index2 = randint(0, lastvalue)

print(f"{player1}: {roshambo[index1]}\n" f"{player2}: {roshambo[index2]}\n") 

if index1 == 0 and index2 == lastvalue or index1 == lastvalue and index2 == 0:
    if index1 == 0:
        index1 = lastvalue + 1
    elif index2 == 0:
        index2 = lastvalue + 1

if index1 > index2:
    print(f"{player1} wins!")
elif index2 > index1:
    print(f"{player2} wins!")
else:
    print("It's a tie!")