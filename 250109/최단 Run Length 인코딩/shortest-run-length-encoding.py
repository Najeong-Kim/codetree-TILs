A = input()

result = 100

def encoding(word):
    result = ''
    count = 1
    now = word[0]
    for i in range(1, len(word)):
        if now == word[i]:
            count += 1
        else:
            result += (now + str(count))
            now = word[i]
            count = 1
    result += (now + str(count))
    return result

for i in range(len(A)):
    A = A[-1] + A[:-1]
    result = min(result, len(encoding(A)))

print(result)