import random

l1 = [1, 2, 3, 4, 5, 6]
l2 = [1, 2, 3, 4, 5, 6]
li=[]
for i in l1:
    for j in l2:
        li.append((i, j))
# print(li)

probability = {}
for i in range(2, 13):
    count=0
    for j in li:
        if i == j[0]+j[1]:
            count+=1
    probability[str(i)] = count/len(li)

user = int(input("Enter no of rounds:- ").strip())

p1wins = 0
p2wins = 0

for i in range(user):
    p1d1, p1d2 = random.randint(1,6), random.randint(1,6)
    p2d1, p2d2 = random.randint(1,6), random.randint(1,6)

    sum_p1 = p1d1 + p1d2
    sum_p2 = p2d1 + p2d2

    prob1 = probability[str(sum_p1)]
    prob2 = probability[str(sum_p2)]

    print(f"Round {i+1}:")
    print(f"  Player 1 rolls: {p1d1}, {p1d2} → Sum = {sum_p1} (Probability: {prob1:.2%})")
    print(f"  Player 2 rolls: {p2d1}, {p2d2} → Sum = {sum_p2} (Probability: {prob2:.2%})")

    if prob1 < prob2:
        p1wins+=1
        print("player 1 wins this round")
    elif prob2 < prob1:
        p2wins+=1
        print("player 2 wins this round")
    else:
        print("Draw")

print("Final win: ")
if p1wins > p2wins:
    print("player 1 wins")
elif p2wins > p1wins:
    print("player 2 wins")
else:
    print("Draw")





