N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]

result = 0

for i in range(N):
    copy_P = P[:]
    copy_P[i] //= 2
    copy_P.sort()
    budget = 0
    for j in range(len(copy_P)):
        if budget + copy_P[j] <= B:
            budget += copy_P[j]
        else:
            result = max(result, j)

print(result)