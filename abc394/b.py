n=int(input())
a=[str(input()) for _ in range(n)]
d={len(i): i for i in a}
r=""
for k in sorted(d.keys()):
    r+=d[k]
print(r)