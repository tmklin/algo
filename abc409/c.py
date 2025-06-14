N, Q = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(Q)]

A = list(range(1, N + 1))
offset = 0
res = []

for query in a:
    if query[0] == 1:
        _, p, x = query
        real_p = (p - 1 + offset) % N
        A[real_p] = x
    elif query[0] == 2:
        _, p = query
        real_p = (p - 1 + offset) % N
        res.append(str(A[real_p]))
    elif query[0] == 3:
        _, k = query
        offset = (offset + k) % N

print('\n'.join(res))
