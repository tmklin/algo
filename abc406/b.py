N, K = map(int, input().split())
A = list(map(int, input().split()))
value = 1
limit = 10 ** K
for a in A:
    value *= a
    if value >= limit:
        value = 1
print(value)
