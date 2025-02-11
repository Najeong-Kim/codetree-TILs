expression = input()
arr = list(expression)
result = 0
alphabets = 'abcdef'

def calculate():
    global result
    now = arr[0]
    for i in range(len(arr)):
        if arr[i] == '+':
            now += arr[i + 1]
        elif arr[i] == '-':
            now -= arr[i + 1]
        elif arr[i] == '*':
            now *= arr[i + 1]
    result = max(result, now)

def run(index):
    if index == 6:
        calculate()
        return
    alphabet = alphabets[index]

    if alphabet in expression:
        check = []
        for i in range(len(arr)):
            if alphabet == arr[i]:
                check.append(i)
        for j in range(1, 5):
            for k in check:
                arr[k] = j
            run(index + 1)
            for k in check:
                arr[k] = alphabet
    else:
        run(index + 1)

run(0)
print(result)