from collections import defaultdict

N, M = map(int, input().split())
turrets = [tuple(map(int, input().split())) for _ in range(M)]

wall_cover = [0] * (N + 2)
for l, r in turrets:
    wall_cover[l] += 1
    wall_cover[r + 1] -= 1

for i in range(1, N + 1):
    wall_cover[i] += wall_cover[i - 1]

res = 0
for l, r in turrets:
    for i in range(l, r + 1):
        if wall_cover[i] == 1:
            res += 1
            break

print(res)
