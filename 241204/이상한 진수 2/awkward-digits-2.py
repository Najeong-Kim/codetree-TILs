N = input()

if '0' in N:
    N = N.replace('0', '1', 1)
else:
    N = N[:-1] + '0'

result = 0

for i in range(len(N)):
    result += int(N[i]) * (2 ** (len(N) - 1 - i))

print(result)