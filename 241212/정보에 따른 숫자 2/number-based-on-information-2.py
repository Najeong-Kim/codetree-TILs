T, a, b = map(int, input().split())
arr = [''] * 1001

for _ in range(T):
    c, x = input().split()
    arr[int(x)] = c

def find_distance(c, x):
    now = 0
    while True:
        if (x + now <= 1000 and arr[x + now] == c) or (x - now >= 0 and arr[x - now] == c):
            return now
        else:
            now += 1

count = 0

for i in range(a, b + 1):
    d1 = find_distance('S', i)
    d2 = find_distance('N', i)
    if d1 <= d2:
        count += 1

print(count)