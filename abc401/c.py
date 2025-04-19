def compute_A_N(N, K):
    MOD = 10**9
    if N < K:
        return 1
    A = [0] * (N + 1)
    prefix_sum = [0] * (N + 2)
    for i in range(K):
        A[i] = 1
        prefix_sum[i + 1] = prefix_sum[i] + A[i]
    for i in range(K, N + 1):
        A[i] = (prefix_sum[i] - prefix_sum[i - K]) % MOD
        prefix_sum[i + 1] = (prefix_sum[i] + A[i]) % MOD
    return A[N]
N,K=map(int, input().split())
print(compute_A_N(N, K))
