n=int(input())
p=list(map(int,input().split()))
q=list(map(int,input().split()))
c=[]
for i in range(1,n+1):
    a=q.index(i)
    b=p[a]
    c.append(q[b-1])
d=""
for i in c:
    d+=str(i)+" "
print(d.rstrip())