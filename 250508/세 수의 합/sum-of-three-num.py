n, k = map(int, input().split())
arr = list(map(int, input().split()))

dict = {}
for i in range(n):
    if arr[i] in dict:
        dict[arr[i]] += 1
    else:
        dict[arr[i]] = 1

count = 0
for elem in dict:
    other = k - elem
    for elem2 in dict:
        elem3 = k - elem - elem2
        if elem3 in dict:
            if elem == elem2 == elem3:
                if dict[elem] < 3:
                    continue
                count += (dict[elem] * (dict[elem] - 1) * (dict[elem] - 2))
            elif elem == elem2:
                if dict[elem] < 2:
                    continue
                count += (dict[elem] * (dict[elem2] - 1)) * dict[elem3]
            elif elem2 == elem3:
                if dict[elem2] < 2:
                    continue
                count += (dict[elem2] * (dict[elem3] - 1)) * dict[elem]
            elif elem3 == elem:
                if dict[elem] < 2:
                    continue
                count += (dict[elem] * (dict[elem3] - 1)) * dict[elem2]
            else:
                count += dict[elem] * dict[elem2] * dict[elem3]

print(count // 6)