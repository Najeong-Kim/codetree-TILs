n = int(input())

A, B = 0, 0
winner = 'C'
count = 0

for i in range(n):
    c, s = input().split()
    if c == 'A':
        A += int(s)
    else:
        B += int(s)
    if A > B and winner != 'A':
        winner = 'A'
        count += 1
    elif A == B and winner != 'C':
        winner = 'C'
        count += 1
    elif A < B and winner != 'B':
        winner = 'B'
        count += 1

print(count)