n = int(input())
string = input()

count = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if string[i] == 'C' and string[j] == 'O' and string[k] == 'W':
                count += 1

print(count)