n = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(n)]

points = []

for i in range(len(intervals)):
    points.append((intervals[i][0], 1, i))
    points.append((intervals[i][1], -1, i))

points.sort()

s = set()

count = 0
for point in points:
    x, v, index = point
    if v == 1:
        if not len(s):
            count += 1
        s.add(index)
    else:
        s.remove(index)

print(count)