A, B, C = map(int, input().split())

result = 0

for i in range(C // A):
    for j in range(C // B):
        now = A * i + B * j
        if now > C:
            break
        result = max(result, now)

print(result)