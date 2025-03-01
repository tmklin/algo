n = int(input())
a = list(map(int, input().split()))
l = {}
m = float("inf")
for i, num in enumerate(a):
    if num in l:
        m = min(m, i - l[num] + 1)
    l[num] = i
print(m if m != float("inf") else -1)
