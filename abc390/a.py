a=list(map(int, input().split()))
b=[]
for i in range(5):
    if a[i]!=i+1:
        b.append(i+1)
if len(b)==2 and abs(b[0]-b[1])==1:
    print("Yes")
else:
    print("No")