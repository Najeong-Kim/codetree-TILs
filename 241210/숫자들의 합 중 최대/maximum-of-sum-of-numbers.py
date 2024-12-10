X, Y = input().split()

result = 0

for i in range(int(X), int(Y) + 1):
    count = 0
    for j in range(len(str(i))):
        count += int(str(i)[j])
    result = max(result, count)

print(result)
