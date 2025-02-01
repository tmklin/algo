a,b=map(int, input().split())
c=list(input() for _ in range(a))
d=list(input() for _ in range(b))
e=[]
for i in range(a-b+1):
    for j in c:
        p=j.find(d[0])
        if p!=-1:
            for k in range(1,b):
                q=c[j].find(d[k])
                if q!=p:
                    break
                e.append(i)
                e.append(p)        
print(e[0], e[1])