binary = input()
num = 0

for i in range(len(binary)):
    num = num * 2 + int(binary[i])

multiple_num = num * 17
digits = []

while True:
    if multiple_num < 2:
        digits.append(multiple_num)
        break
    
    digits.append(multiple_num % 2)
    multiple_num //= 2

for digit in digits[::-1]:
    print(digit, end="")