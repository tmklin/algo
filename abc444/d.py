import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
maxA = max(A)
diff = [0] * (maxA + 1)
for a in A:
    diff[0] += 1
    diff[a] -= 1
cnt = [0] * maxA
cur = 0
for j in range(maxA):
    cur += diff[j]
    cnt[j] = cur
res = []
carry = 0
for j in range(maxA):
    total = cnt[j] + carry
    res.append(str(total % 10))
    carry = total // 10
while carry:
    res.append(str(carry % 10))
    carry //= 10
print(''.join(res[::-1]))
