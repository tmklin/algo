n = int(input())
l = []
g = 0
p = 0
min_stack = [0]
for _ in range(n):
    a = input().split()
    if a[0] == "1":
        l.append(a[1])
        if a[1] == "(":
            g += 1
        else:
            g -= 1
        min_stack.append(min(min_stack[-1], g))
    else:
        t = l.pop()
        if t == "(":
            g -= 1
        else:
            g += 1
        min_stack.pop()
    if g == 0 and min_stack[-1] >= 0:
        print("Yes")
    else:
        print("No")
