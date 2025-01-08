import sys

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
index_arr = [[(k + m * j) for k in range(m)] for j in range(n)]
sum_arr = []

for i in range(n):
    for j in range(i + 1, n + 1):
        for k in range(m):
            for l in range(k + 1, m + 1):
                total = 0
                arr =  []
                for a in range(i, j):
                    for b in range(k, l):
                        total += grid[a][b]
                        arr.append(index_arr[a][b])
                sum_arr.append([total, arr])

result = -sys.maxsize

for i in range(len(sum_arr)):
    for j in range(i + 1, len(sum_arr)):
        first = sum_arr[i]
        second = sum_arr[j]
        if not len(set(first[1]) & set(second[1])):
            result = max(result, first[0] + second[0])

print(result)