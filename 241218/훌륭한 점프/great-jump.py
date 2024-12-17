n, k = map(int, input().split())
arr = list(map(int, input().split()))

def is_possible(max_val):
    available_indices = []
    for i, elem in enumerate(arr):
        if elem <= max_val:
            available_indices.append(i)

    for i in range(1, len(available_indices)):
        dist = available_indices[i] - available_indices[i - 1]
        if dist > k:
            return False

    return True


for a in range(max(arr[0], arr[-1]), max(arr) + 1):
    if is_possible(a):
        print(a)
        break
