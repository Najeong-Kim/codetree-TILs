def sumFrom1toN(N):
    sum = 0
    for i in range(1, N + 1):
        sum += i
    return sum // 10

input = int(input())
output = sumFrom1toN(input)
print(output)