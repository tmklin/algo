from collections import defaultdict
N=int(input())
P=list(map(int, input().split()))
a=[]
for i in range(N-1):
    if P[i] > P[i+1]:
        a.append(0)
    elif P[i] == P[i+1]:
        a.append(1)
    else:
        a.append(2)
r=0
for i in range(N-3):
    if a[i] != 2:
        break
    if a[i+1] != 0:
        break
    c=i+2
    d=0
    while(c<N):
        if a[c]==2:
            break
        if a[c] ==0:
            c+=1
            continue
    if c==N-1:
        break
    b=0
    while (a[c+1]==2):
        b+=1
        c+=1
    f=0
    e=i-1
    while (e>=0 and a[e]==2):
        f+=1
        e+=1
    d=(b+1) * (f+1)
    r+=d
print(r)