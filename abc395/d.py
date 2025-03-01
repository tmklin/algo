n, q = map(int, input().split())
pn = list(range(n + 1))
np = {i: {i} for i in range(1, n + 1)}
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        a, b = query[1], query[2]
        np[pn[a]].remove(a)
        np[b].add(a)
        pn[a] = b
    elif query[0] == 2:
        a, b = query[1], query[2]
        np[a], np[b] = np[b], np[a]
        for p in np[a]:
            pn[p] = a
        for p in np[b]:
            pn[p] = b
    else:
        print(pn[query[1]])
