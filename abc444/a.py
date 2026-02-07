N = int(input())
a = N //100
b = (N%100) //10
c = (N%100) %10
if a==b==c:
    print("Yes")
else:
    print("No")
    