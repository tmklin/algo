s=str(input())
l=[]
d={')': '(','>': '<',']': '['}
for i in s:
    if i in "([<":
        l.append(i)
    else:
        if not l or l[-1]!=d[i]:
            print("No")
            exit()
        l.pop()
print("Yes" if not l else "No")