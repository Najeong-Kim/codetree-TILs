n = int(input())
arr = list(map(int, input().split()))

check = [[10 ** 9] * (10 ** 5 + 1) for _ in range(n + 1)]
total = sum(arr)
check[0][0] = total

def cal_min(now):
    return abs(now - (total - now))

for i in range(n):
    for j in range(len(check[0])):
        if check[i][j] != 10 ** 9:
            check[i + 1][j] = min(check[i + 1][j], check[i][j])
            check[i + 1][j + arr[i]] = min(check[i + 1][j + arr[i]], cal_min(j + arr[i]))

print(min(check[-1]))
