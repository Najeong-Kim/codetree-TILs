N, L = map(int, input().split())
arr = list(map(int, input().split()))

for score in reversed(range(101)):
    count = 0
    plus = 0
    for elem in arr:
        if elem >= score:
            count += 1
        elif elem + 1 == score and L < plus:
            plus += 1
            count += 1
    if count >= score:
        print(score)
        break

