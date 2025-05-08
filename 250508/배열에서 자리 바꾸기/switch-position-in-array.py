N = int(input())
Q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(Q)]
a, b, c, d = zip(*queries)
a, b, c, d = list(a), list(b), list(c), list(d)

# Please write your code here.
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def connect(s, e):
    # s와 e를 이어줌
    if s is not None:
        s.next = e
    if e is not None:
        e.prev = s

dict = {}

for i in range(1, N + 1):
    dict[i] = Node(i)

for i in range(1, N):
    connect(dict[i], dict[i + 1])

head = dict[1]

for query in queries:
    a, b, c, d = query
    a_prev, b_next, c_prev, d_next = dict[a].prev, dict[b].next, dict[c].prev, dict[d].next
    if dict[b].next and dict[b].next.data == dict[c].data:
        connect(a_prev, dict[c])
        connect(dict[b], d_next)
        connect(dict[d], dict[a])
    else:
        connect(a_prev, dict[c])
        connect(dict[b], d_next)
        connect(c_prev, dict[a])
        connect(dict[d], b_next)

    if head.data == dict[a].data:
        head = dict[c]
    elif head.data == dict[c].data:
        head = dict[a]

for i in range(N):
    print(head.data, end=' ')
    head = head.next
