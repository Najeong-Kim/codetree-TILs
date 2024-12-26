A, B, x, y = map(int, input().split())

first = B - A
second = abs(A - x) + abs(B - y)
third = abs(A - y) + abs(B - x)

print(min(first, second, third))