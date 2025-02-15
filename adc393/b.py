s = input().strip()
a = s.find('A')
b = s.rfind('C')
if a == -1 or b == -1 or a > b:
    print(0)
    exit()
s = s[a:b + 1]
A_indices = [i + 1 for i, c in enumerate(s) if c == 'A']
B_indices = [i + 1 for i, c in enumerate(s) if c == 'B']
C_indices = set(i + 1 for i, c in enumerate(s) if c == 'C')
p = 0
for o in A_indices:
    for u in B_indices:
        if u <= o:
            continue
        g = 2 * u - o
        if g in C_indices:
            p += 1
print(p)