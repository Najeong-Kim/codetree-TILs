import sys

N, S = map(int, input().split())
arr = list(map(int, input().split()))

difference = sys.maxsize

for i in range(N - 1):
    for j in range(i + 1, N):
        sum_arr = 0
        for k in range(len(arr)):
            if k == i or k == j:
                continue
            sum_arr += arr[k]
        difference = min(difference, abs(S - sum_arr))

print(difference)