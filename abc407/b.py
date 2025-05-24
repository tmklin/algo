X,Y= map(int,input().split())

total = 0
for a in range(1, 7):
    for b in range(1, 7):
        if a + b >= X or abs(a - b) >= Y:
            total += 1
p = total / 36
print(p)
