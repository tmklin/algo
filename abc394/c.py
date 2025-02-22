s=str(input())
r = []
wc=0
for c in s:
    if c == 'W':
        wc+=1
    elif c == 'A' and wc > 0:
        r.append('AC' + 'C' * (wc - 1))
        wc=0
    else:
        if wc > 0:
            r.append('W' * wc)
            wc=0
        r.append(c)
if wc > 0:
    r.append('W' * wc)
print(''.join(r))
