num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

m1, d1, m2, d2 = map(int, input().split())
A = input()

first_day = sum(num_of_days[:m1]) + d1
second_day = sum(num_of_days[:m2]) + d2

count = (second_day - first_day) // 7
if (week.index(A) <= ((second_day - first_day) % 7)):
    count += 1

print(count)