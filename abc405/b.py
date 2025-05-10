N, M = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N + 1):
    prefix = A[:N - i]
    if set(prefix) != set(range(1, M + 1)):
        print(i)
        break
