n = int(input())
arr = list(map(int, input().split()))

sorted_arr = list(set(sorted(arr)))

if len(sorted_arr) == 1:
    print(-1)
elif arr.count(sorted_arr[1]) > 1:
    print(-1)
else:
    print(arr.index(sorted_arr[1]) + 1)