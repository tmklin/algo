n=int(input())
a=map(int,input().split())
c=0
r=0
for i in a:
    if c >=i:
        r+=1
    c=i
print("No" if r!=0 else "Yes")
