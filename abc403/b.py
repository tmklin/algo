def r(g):
    N=len(g)
    return [''.join(g[N - j - 1][i] for j in range(N)) for i in range(N)]

def a(S, T):
    m = float('inf')
    for rc in range(4):
        c = sum(
            1 for i in range(len(S)) for j in range(len(S))
            if S[i][j] != T[i][j]
        )
        t = c + rc
        m = min(m,t)
        S = r(S)
    return m
N = int(input())
S = [input().strip() for _ in range(N)]
T = [input().strip() for _ in range(N)]

print(a(S, T))
