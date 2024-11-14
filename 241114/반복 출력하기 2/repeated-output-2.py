def repeat_hello_world(n):
    if n == 0:
        return
    print('HelloWorld')
    repeat_hello_world(n - 1)

N = int(input())
repeat_hello_world(N)