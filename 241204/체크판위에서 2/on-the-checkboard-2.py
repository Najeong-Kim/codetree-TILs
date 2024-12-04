R, C = map(int, input().split())
arr = []

for _ in range(R):
    arr.append(list(map(str, input().split())))

start_color = arr[0][0]
end_color = arr[R - 1][C - 1]

count = 0

for i in range(1, R - 2):
    for j in range(1, C - 2):
        for k in range(i + 1, R - 1):
            for l in range(j + 1, C - 1):
                if arr[i][j] == end_color and arr[k][l] == start_color:
                    count += 1

print(count)