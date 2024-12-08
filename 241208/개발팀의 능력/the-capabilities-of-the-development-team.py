arr = list(map(int, input().split()))

min_diff = 5001

for i in range(5):
    for j in range(i + 1, 5):
        for k in range(j + 1, 5):
            for l in range(k + 1, 5):
                sub = [i, j, k, l]
                sum_sub = sum([arr[index] for index in sub])
                for m in range(4):
                    for n in range(m + 1, 4):
                        first = arr[sub[m]] + arr[sub[n]]
                        second = sum_sub - first
                        third = sum(arr) - first - second
                        if first == second or second == third or third == first:
                            continue
                        max_team = max(first, second, third)
                        min_team = min(first, second, third)
                        min_diff = min(min_diff, max_team - min_team)

if min_diff == 5001:
    print(-1)
else:
    print(min_diff)