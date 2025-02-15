n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
qi = {value: i for i, value in enumerate(q)}
c = [q[p[qi[i]] - 1] for i in range(1, n + 1)]
print(" ".join(map(str, c)))