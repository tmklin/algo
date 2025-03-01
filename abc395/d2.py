import sys

input = sys.stdin.read
data = input().split()
index = 0

n = int(data[index])
q = int(data[index + 1])
index += 2

pn = list(range(n + 1))
queries = []
track = set()

for _ in range(q):
    t = int(data[index])
    if t == 1:
        a, b = int(data[index + 1]), int(data[index + 2])
        queries.append((1, a, b))
        track.add(a)
        index += 3
    elif t == 2:
        a, b = int(data[index + 1]), int(data[index + 2])
        queries.append((2, a, b))
        index += 3
    else:
        a = int(data[index + 1])
        queries.append((3, a))
        index += 2

np = {}

for t, *args in queries:
    if t == 1:
        a, b = args
        pa = pn[a]
        if pa in np:
            np[pa].discard(a)
            if not np[pa]:
                del np[pa]
        if b not in np:
            np[b] = set()
        np[b].add(a)
        pn[a] = b
    elif t == 2:
        a, b = args
        if a != b:
            np[a], np[b] = np.get(b, set()), np.get(a, set())
            for p in np[a]:
                pn[p] = a
            for p in np[b]:
                pn[p] = b
    else:
        a = args[0]
        print(pn[a])
