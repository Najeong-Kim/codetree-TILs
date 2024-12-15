import math

A, B, C = map(int, input().split())

result = 0

for i in range(math.ceil(C / A)):
    for j in range(math.ceil(C / B)):
        now = A * i + B * j
        if now > C:
            break
        result = max(result, now)

print(result)