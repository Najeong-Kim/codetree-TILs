N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

max_area = 0

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            x1, y1 = arr[i]
            x2, y2 = arr[j]
            x3, y3 = arr[k]
            if (x1 == x2 and y1 == y3) or (x1 == x3 and y1 == y2) or (x2 == x1 and y2 == y3) or (x2 == x3 and y2 == y1) or (x3 == x2 and y3 == y1) or (x3 == x1 and y3 == y2):
                max_area = max(max_area,abs((x1*y2+x2*y3+x3*y1) - (x2*y1+x3*y2+x1*y3)))

print(max_area)