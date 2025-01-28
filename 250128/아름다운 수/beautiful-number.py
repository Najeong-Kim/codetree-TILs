n = int(input())
text = ''
count = 0

def run():
    global text
    global count
    if len(text) > n:
        return
    if len(text) == n:
        count += 1
        return
    for i in range(1, 5):
        text += str(i) * i
        run()
        text = text[:-i]

run()
print(count)