n=int(input())
a=list(map(int, input().split()))
b=True
c=a[1]/a[0]
for i in range(n-1):
    if a[i]*c!=a[i+1]:
        b=False
print("Yes" if b else "No")