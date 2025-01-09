n, m, q = map(int, input().split())

# Create 2D array for building state
a = [list(map(int, input().split())) for _ in range(n)]

# Process wind queries
winds = [tuple(map(int, input().split())) for _ in range(q)]

def rotate(x1, y1, x2, y2):
    temp = a[x1][y1]
    for i in range(x1, x2):
        a[i][y1] = a[i + 1][y1]
    for i in range(y1, y2):
        a[x2][i] = a[x2][i + 1]
    for i in reversed(range(x1, x2)):
        a[i + 1][y2] = a[i][y2]
    for i in reversed(range(y1, y2)):
        a[x1][i + 1] = a[x1][i]
    a[x1][y1 + 1] = temp

for wind in winds:
    raw_x1, raw_y1, raw_x2, raw_y2 = wind
    x1, y1, x2, y2 = raw_x1 - 1, raw_y1 - 1, raw_x2 - 1, raw_y2 - 1
    rotate(x1, y1, x2, y2)
    new_a = []
    for i in range(n):
        new_line = []
        for j in range(m):
            if x1 <= i <= x2 and y1 <= j <= y2:
                value = a[i][j]
                count = 1
                if i > 0:
                    value += a[i - 1][j]
                    count += 1
                if i < n - 1:
                    value += a[i + 1][j]
                    count += 1
                if j > 0:
                    value += a[i][j - 1]
                    count += 1
                if j < m - 1:
                    value += a[i][j + 1]
                    count += 1
                new_line.append(value // count)
            else:
                new_line.append(a[i][j])
        new_a.append(new_line)
    a = new_a
                

for elem in a:
    print(*elem)