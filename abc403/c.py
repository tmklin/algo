import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
degree = [0] * (N+1)

for _ in range(M):
    A, B = map(int, input().split())
    adj[A].append(B)
    adj[B].append(A)
    degree[A] += 1
    degree[B] += 1
if M != N:
    print("No")
    exit()
if not all(degree[i] == 2 for i in range(1, N+1)):
    print("No")
    exit()
visited = [False] * (N+1)
def dfs(v):
    visited[v] = True
    for u in adj[v]:
        if not visited[u]:
            dfs(u)
dfs(1)
if all(visited[1:]):
    print("Yes")
else:
    print("No")
