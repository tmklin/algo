N, Q = map(int, input().split())
A = list(map(int, input().split()))

color = [0] * (N + 2)
black_blocks = 0
res = []

for a in A:
    if color[a] == 0:
        color[a] = 1
        if color[a - 1] == 0 and color[a + 1] == 0:
            black_blocks += 1
        elif color[a - 1] == 1 and color[a + 1] == 1:
            black_blocks -= 1
    else:
        if color[a - 1] == 0 and color[a + 1] == 0:
            black_blocks -= 1
        elif color[a - 1] == 1 and color[a + 1] == 1:
            black_blocks += 1
        color[a] = 0
    res.append(str(black_blocks))

print('\n'.join(res))
