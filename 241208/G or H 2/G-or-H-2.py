N = int(input())
arr = [''] * 101

for _ in range(N):
    position, alphabet = input().split()
    arr[int(position)] = alphabet

alphabets = []
positions = []
for idx, elem in enumerate(arr):
    if elem:
        alphabets.append(elem)
        positions.append(idx)

checklist = []

for idx, elem in enumerate(alphabets):
    for i in range(idx + 1, len(alphabets)):
        if elem != alphabets[i]:
            if idx != i - 1:
                checklist.append([idx, i - 1])
            break
    
    count = {
        'G': 0,
        'H': 0
    }
    max_index = idx
    for i in range(idx, len(alphabets)):
        count[alphabets[i]] += 1
        if count['G'] == count['H']:
            max_index = i
    if max_index != idx:
        checklist.append([idx, max_index])

result = 0

for elem in checklist:
    result = max(result, positions[elem[1]] - positions[elem[0]])

print(result)