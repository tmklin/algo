from collections import deque

n=int(input())
q=deque()
for _ in range(n):
    a=input().split()
    if a[0] == '1':
        q.append(int(a[1]))
    else:
        print(q.popleft())
