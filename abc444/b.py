N, K = map(int, input().split())
S = str(N)
L = len(S)
dp = [[[0]*2 for _ in range(K+1)] for _ in range(L+1)]
dp[0][0][1] = 1
for pos in range(L):
    for s in range(K+1):
        for tight in range(2):
            if dp[pos][s][tight] == 0:
                continue
            limit = int(S[pos]) if tight else 9
            for d in range(limit + 1):
                if s + d > K:
                    continue
                ntight = tight and (d == limit)
                dp[pos+1][s+d][ntight] += dp[pos][s][tight]
ans = dp[L][K][0] + dp[L][K][1]
if K == 0:
    ans -= 1
print(ans)
