X, Y = map(int, input().split())

count = 0

for number in range(X, Y + 1):
    data = {}
    for i in range(len(str(number))):
        key = str(number)[i]
        if key in data:
            data[key] += 1
        else:
            data[key] = 1
    one, more = None, None
    is_interest = True
    for key in data:
        if data[key] == 1:
            if one:
                is_interest = False
                break
            one = data[key]
        if data[key] != 1:
            if more:
                is_interest = False
                break
            more = data[key]
    if one and more and is_interest:
        count += 1

print(count)


        