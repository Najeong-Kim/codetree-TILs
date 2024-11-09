def arithmetic_operator(a, o, c):
    a, c = int(a), int(c)
    if (o == '+'):
        return a + c
    if (o == '-'):
        return a - c
    if (o == '/'):
        return a // c
    if (o == '*'):
        return a * c
    return False

a, o, c = map(str, input().split())
if (arithmetic_operator(a, o, c)):
    print(a, o, c, '=', arithmetic_operator(a, o, c))
else:
    print(arithmetic_operator(a, o, c))