N, K = map(int, input().split())
Q = int(input())
type_arr = []
i_arr = []
j_arr = []
for _ in range(Q):
    t, x, y = map(int, input().split())
    type_arr.append(t)
    i_arr.append(x)
    j_arr.append(y)

# Please write your code here.
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

head = [None] * (K + 1)
tail = [None] * (K + 1)
dict = {}
dict[1] = Node(1)
head[1] = dict[1]

for i in range(2, N + 1):
    node = Node(i)
    dict[i] = node
    node.prev = dict[i - 1]
    dict[i - 1].next = node

    if i == N:
        tail[1] = node

for i in range(Q):
    if type_arr[i] == 1:
        book = head[i_arr[i]]
        if book:
            if tail[j_arr[i]]:
                tail[j_arr[i]].next = book
            book.prev = tail[j_arr[i]]
            head[i_arr[i]] = book.next
            if head[i_arr[i]]:
                head[i_arr[i]].prev = None
            if not head[i_arr[i]]:
                tail[i_arr[i]] = None
            book.next = None
            if not head[j_arr[i]]:
                head[j_arr[i]] = book
            tail[j_arr[i]] = book
    if type_arr[i] == 2:
        book = tail[i_arr[i]]
        if book:
            if head[j_arr[i]]:
                head[j_arr[i]].prev = book
            book.next = head[j_arr[i]]
            head[j_arr[i]] = book
            tail[i_arr[i]] = book.prev
            if tail[i_arr[i]]:
                tail[i_arr[i]].next = None
            if book.prev == None:
                head[i_arr[i]] = None
            if not tail[j_arr[i]]:
                tail[j_arr[i]] = book
            book.prev = None
    if type_arr[i] == 3:
        if i_arr[i] == j_arr[i]:
            continue
        book = head[i_arr[i]]
        if book:
            if tail[i_arr[i]]:
                tail[i_arr[i]].next = head[j_arr[i]]
            if head[j_arr[i]]:
                head[j_arr[i]].prev = tail[i_arr[i]]
            head[j_arr[i]] = head[i_arr[i]]
            if not tail[j_arr[i]]:
                tail[j_arr[i]] = tail[i_arr[i]]
            head[i_arr[i]] = None
            tail[i_arr[i]] = None
    if type_arr[i] == 4:
        if i_arr[i] == j_arr[i]:
            continue
        book = head[i_arr[i]]
        if book:
            if tail[j_arr[i]]:
                tail[j_arr[i]].next = head[i_arr[i]]
            if head[i_arr[i]]:
                head[i_arr[i]].prev = tail[j_arr[i]]
            tail[j_arr[i]] = tail[i_arr[i]]
            if not head[j_arr[i]]:
                head[j_arr[i]] = head[i_arr[i]]
            head[i_arr[i]] = None
            tail[i_arr[i]] = None

for i in range(1, K + 1):
    books = []
    book = head[i]
    while book:
        books.append(book.data)
        book = book.next
    print(len(books), *books)