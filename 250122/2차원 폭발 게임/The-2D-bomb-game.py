n, m, k = map(int, input().split())
numbers_2d = [list(map(int, input().split())) for _ in range(n)]

# Write your code here!
def bomb():
    arr = [[] for _ in range(n)]
    for i in range(n):
        prev = [numbers_2d[j][i] for j in reversed(range(n))]
        next = []
        now = -1
        count = 0
        for index, value in enumerate(prev):
            if value == 0:
                break
            elif now == value:
                count += 1
            else:
                if count < m:
                    for _ in range(count):
                        next.append(now)
                now = value
                count = 1
        if count < m:
            for _ in range(count):
                next.append(now)
        while len(next) < n:
            next.append(0)
        for j in range(n):
            arr[j].append(next[n - 1 - j])
    return arr

def rotate():
    global numbers_2d
    arr = [[] for _ in range(n)]
    for i in reversed(range(n)):
        prev = numbers_2d[i]
        next = []
        for j in reversed(range(n)):
            if prev[j] != 0:
                next.append(prev[j])
        while len(next) < n:
            next.append(0)
        for j in range(n):
            arr[j].append(next[n - 1 - j])
    numbers_2d = arr

for i in range(k):
    while True:
        next = bomb()
        if numbers_2d == next:
            break
        else:
            numbers_2d = next
    rotate()

while True:
    next = bomb()
    if numbers_2d == next:
        break
    else:
        numbers_2d = next

result = 0
for i in range(n):
    for j in range(n):
        if numbers_2d[i][j] != 0:
            result += 1

print(result)