def print_squre(n):
    digit = 1
    for _ in range(n):
        for i in range(n):
            print(digit, end=" ") if i != n - 1 else print(digit)
            digit = 1 if digit == 9 else digit + 1

num = int(input())
print_squre(num)