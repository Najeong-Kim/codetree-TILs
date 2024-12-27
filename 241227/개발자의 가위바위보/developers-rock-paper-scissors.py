N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

result = 0
courses = [[1, 2, 3], [1, 3, 2]]

for course in courses:
    count = 0
    for j in range(len(arr)):
        first_number, second_number = arr[j]
        first, second = course.index(first_number), course.index(second_number)
        if (first == 0 and second == 1) or (first == 1 and second == 2) or (first == 2 and second == 0):
            count += 1
    result = max(result, count)

print(result)
