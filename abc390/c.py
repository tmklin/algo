n,m=map(int, input().split())
a=[input() for i in range(n)]
x=[]
y=[]
b=True
for i in range(n):
    for j in range(m):
        if a[i][j]=="#":
            y.append(i)
            x.append(j)
xl=min(x)
yh=min(y)
xr=max(x)
yl=max(y)
for i in range(yh, yl+1):
    for j in range(xl, xr+1):
        if a[i][j]==".":
            b=False
            break
    else:
        continue
    break
print("Yes" if b else "No")