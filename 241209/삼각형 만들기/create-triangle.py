N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

max_area = 0

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            x1, y1 = arr[i]
            x2, y2 = arr[j]
            x3, y3 = arr[k]
            max_area = abs((x1*y2+x2*y3+x3*y1) - (x2*y1+x3*y2+x1*y3))

print(max_area)