n = int(input())
words = [input() for _ in range(n)]

dict = {}
for word in words:
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1

result = 0
for elem in dict:
    result = max(result, dict[elem])

print(result)