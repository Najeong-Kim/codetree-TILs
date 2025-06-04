word = input()
arr = []

start = 0
end = 0

arr.append(word[start])
result = 1

while end != len(word) - 1:
    if word[end + 1] in arr:
        if start == end:
            arr.remove(word[start])
            start += 1
            end += 1
            arr.append(word[end])
        else:
            arr.remove(word[start])
            start += 1
    else:
        end += 1
        arr.append(word[end])
    result = max(result, len(arr))

print(result)            
