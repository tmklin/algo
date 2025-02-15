from collections import deque
n=int(input())
a=list(map(int,input().split()))
d=deque()
for i in range(1,n+1):
    d.insert(a[i-1]-1,i)
print(" ".join(map(str, d)))