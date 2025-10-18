N, K = map(int, input().split())
S = str(input())
cd = {}
for i in range(N - K + 1):
    a = S[i:i+K]
    cd[a] = cd.get(a, 0) + 1
b = max(cd.values())
l = sorted([k for k, v in cd.items() if v == b])
print(b)
print(" ".join(l))