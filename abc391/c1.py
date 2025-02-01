n, q = map(int, input().split())
a=[input().split() for _ in range(q)]
b=[]
for i in range(n):
    b.append([i+1])
for i in a:
    if i[0]=="2":
        t=0
        for o in b:
            if len(o) >= 2:
                t+=1
        print(t)
    else:
        for k in b:
            for l in k:
                if l==int(i[1]):
                    k.remove(l)
        b[int(i[2])-1].append(int(i[1]))