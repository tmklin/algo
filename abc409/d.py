from collections import defaultdict, deque

N, M = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))

dist = [-1] * (N + 1)
xor_to = [0] * (N + 1)
basis = [0] * 61
dist[1] = 0
q = deque([1])

while q:
    u = q.popleft()
    for v, w in graph[u]:
        x = xor_to[u] ^ w
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            xor_to[v] = x
            q.append(v)
        else:
            loop = xor_to[v] ^ x
            for i in reversed(range(61)):
                if loop >> i & 1:
                    if basis[i] == 0:
                        basis[i] = loop
                        break
                    loop ^= basis[i]

res = xor_to[N]
for i in reversed(range(61)):
    if res >> i & 1:
        res ^= basis[i]

print(res if dist[N] != -1 else -1)
