n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

def delete_blocks(s, e):
    global blocks
    new = []
    for i, v in enumerate(blocks):
        if not s <= i + 1 <= e:
            new.append(v)
    blocks = new

delete_blocks(s1, e1)
delete_blocks(s2, e2)

print(len(blocks))
for block in blocks:
    print(block)