N = int(input())
arr = []

for _ in range(N):
    now = input()
    if 'push_back' in now:
        command, value = now.split()
        arr.append(value)
    elif 'get' in now:
        command, value = now.split()
        print(arr[int(value) - 1])
    elif 'size' in now:
        print(len(arr))
    elif 'pop_back' in now:
        arr = arr[:-1]
