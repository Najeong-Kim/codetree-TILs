X, Y = map(int, input().split())

count = 0

for i in range(X, Y + 1):
    number = str(i)
    ok = True
    for j in range(len(number)//2):
        if number[j] != number[len(number)-1-j]:
            ok = False
            break
    if ok:
        count += 1

print(count)