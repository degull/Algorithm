dice = list(map(int, input().split()))

if dice[0] == dice[1]==dice[2]:
    prize = 10000+dice[0]*1000
elif dice[0]==dice[1] or dice[0]==dice[2] or dice[1]==dice[2]:
    same = max(dice[0], dice[1], dice[2], key=dice.count)
    prize = 1000+same*100
else:
    prize=max(dice)*100
    
print(prize)