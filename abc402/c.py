from collections import defaultdict
import sys
input = sys.stdin.readline
n,m=map(int, input().split())
r=[]
l=list([] for _ in range(n+1))
for i in range(m):
    d=list(map(int, input().split()))
    a=d[1:]
    r.append(a)
    for o in a:
        l[o].append(i)
c=[len(b) for b in r]
v=list(map(int, input().split()))
result=[]
e=0
for b in v:
    for m in l[b]:
        c[m] -= 1
        if c[m] == 0:
            e+=1
    result.append(e)
print('\n'.join(map(str, result)))
