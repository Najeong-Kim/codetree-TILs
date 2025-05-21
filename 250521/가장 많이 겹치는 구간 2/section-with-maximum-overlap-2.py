n = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(n)]

points = []

for i in intervals:
    points.append((i[0], 1))
    points.append((i[1], -1))

points.sort()

count = 0
value = 0
for point in points:
    value += point[1]
    count = max(count, value)

print(count)