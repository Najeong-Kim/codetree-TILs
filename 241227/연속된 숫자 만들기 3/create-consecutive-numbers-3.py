a, b, c = map(int, input().split())
arr = sorted([a, b, c])

print(max(b - a - 1, c - b - 1))