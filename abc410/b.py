N = int(input())
D = list(map(int, input().split()))

sum = [0] * (N)
for i in range(1, N):
    sum[i] = sum[i-1] + D[i-1]

for i in range(N - 1):
    res = []
    for j in range(i + 1, N):
        d = sum[j] - sum[i]
        res.append(str(d))
    print(" ".join(res))
