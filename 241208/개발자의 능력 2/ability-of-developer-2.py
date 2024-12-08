import sys

arr = list(map(int, input().split()))

min_diff = sys.maxsize

for i in range(6):
    for j in range(i + 1, 6):
        for k in range(j + 1, 6):
            for l in range(k + 1, 6):
                sub = [i, j, k, l]
                sum_sub = sum([arr[index] for index in sub])
                for m in range(4):
                    for n in range(m + 1, 4):
                        first = arr[sub[m]] + arr[sub[n]]
                        second = sum_sub - first
                        third = sum(arr) - first - second
                        max_team = max(first, second, third)
                        min_team = min(first, second, third)
                        min_diff = min(min_diff, max_team - min_team)

print(min_diff)