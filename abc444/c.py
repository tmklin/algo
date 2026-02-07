N = int(input())
A = list(map(int, input().split()))
A.sort()

def check(L):
    l, r = 0, N - 1
    while l < r:
        if A[r] == L:
            r -= 1
        else:
            if A[l] + A[r] != L:
                return False
            l += 1
            r -= 1
    if l == r:
        return A[l] == L
    return True
candidates = set()
candidates.add(A[-1])
candidates.add(A[0] + A[-1])
ans = []
for L in candidates:
    if check(L):
        ans.append(L)
ans.sort()
print(*ans)
