n,m=map(int,input().split())
edges=set()
d=0
for _ in range(m):
    a, b = map(int, input().split())
    if a == b:
        d += 1
        continue
    edge = (min(a, b), max(a, b))
    if edge in edges:
        d += 1
    else:
        edges.add(edge)
print(d)
