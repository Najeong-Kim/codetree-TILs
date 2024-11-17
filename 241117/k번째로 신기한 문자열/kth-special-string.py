n, k, T = map(str, input().split())
arr = []

for i in range(int(n)):
    arr.append(input())

arr.sort()

def function():
    for i in range(len(arr)):
        if arr[i].startswith(T):
            return i

print(arr[function() + int(k) - 1])