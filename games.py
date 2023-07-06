n = int(input())
teams = [list(map(int, input().split())) for _ in range(n)]

home_changes = 0

for i in range(n):
    for j in range(n):
        if i != j and teams[i][0] == teams[j][1]:
            home_changes += 1

print(home_changes)