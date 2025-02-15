n,m=map(int,input().split())
a=set(map(int,input().split()))
b=set()
for i in range(1,n+1):
    b.add(i)
a=b-a
a=list(a)
print(len(a))
a.sort()
c=""
for i in a:
    c+=str(i)+" "
print(c.rstrip())