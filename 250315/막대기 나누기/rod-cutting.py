n = int(input())
profits = list(map(int, input().split()))
arr = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(len(profits)):
        profit = profits[j]
        if i - j - 1 >= 0:
            arr[i] = max(arr[i], arr[i - j - 1] + profit)

print(max(arr))
