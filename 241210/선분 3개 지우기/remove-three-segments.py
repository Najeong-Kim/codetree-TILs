n = int(input())
lines = [list(map(int, input().split())) for _ in range(n)]
arr = [0] * 102

for line in lines:
    for i in range(line[0], line[1] + 1):
        arr[i] += 1

count = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            is_ok = True
            current_arr = arr[:]
            for a in range(lines[i][0], lines[i][1] + 1):
                current_arr[a] -= 1
            for a in range(lines[j][0], lines[j][1] + 1):
                current_arr[a] -= 1
            for a in range(lines[k][0], lines[k][1] + 1):
                current_arr[a] -= 1
            for elem in current_arr:
                if elem > 1:
                    is_ok = False
                    break
            if is_ok:
                count += 1

print(count)