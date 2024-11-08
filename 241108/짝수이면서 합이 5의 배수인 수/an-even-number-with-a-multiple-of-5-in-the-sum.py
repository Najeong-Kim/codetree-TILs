def is_even_and_multiple_5(n):
    sum_of_digits = n % 10 + n // 10
    result = n % 2 == 0 and sum_of_digits % 5 == 0
    return 'Yes' if result else 'No'

input = int(input())
output = is_even_and_multiple_5(input)
print(output)