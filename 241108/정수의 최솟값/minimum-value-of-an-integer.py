def minimumInteger(a, b, c):
    return min(a, b, c)

a, b, c = map(int, input().split())
output = minimumInteger(a, b, c)
print(output)