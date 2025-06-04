word, k = input().split()
k = int(k)

start = 0
end = 0

alphabet = 'abcdefghijklmnopqrstuvwxyz'
arr = [0] * 26

arr[alphabet.index(word[start])] += 1
count = 1
result = 1

while end != len(word) - 1:
    if arr[alphabet.index(word[end + 1])] == 0 and len(list(filter(lambda x: x > 0, arr))) >= k:
        if start == end:
            arr[alphabet.index(word[start])] -= 1
            start += 1
            end += 1
            arr[alphabet.index(word[end])] += 1
        else:
            arr[alphabet.index(word[start])] -= 1
            start += 1
            count -= 1
    else:
        end += 1
        arr[alphabet.index(word[end])] += 1
        count += 1
    result = max(result, count)

print(result)
