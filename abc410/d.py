import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

class Node:
    def __init__(self, parent=None, add=""):
        self.parent = parent
        self.add = add

    def build(self):
        res = []
        cur = self
        while cur:
            res.append(cur.add)
            cur = cur.parent
        return ''.join(reversed(res))

PC = [None] * (N + 1)
server = None

for _ in range(Q):
    query = input().split()
    if query[0] == '1':
        p = int(query[1])
        PC[p] = server
    elif query[0] == '2':
        p = int(query[1])
        s = query[2]
        PC[p] = Node(PC[p], s)
    elif query[0] == '3':
        p = int(query[1])
        server = PC[p]

print(server.build() if server else "")
