import sys
from collections import deque

sys.setrecursionlimit(1 << 25)
input = sys.stdin.readline

H, W = map(int, input().split())
grid = [list(input().strip()) for _ in range(H)]

has_path = any('.' in row for row in grid)
has_exit = any('E' in row for row in grid)

if not has_path or not has_exit:
    for row in grid:
        print(''.join(row))
    exit()

dirs = [(-1, 0, 'v'), (1, 0, '^'), (0, -1, '>'), (0, 1, '<')]
dist = [[-1] * W for _ in range(H)]
arrow = [['' for _ in range(W)] for _ in range(H)]

q = deque()

for i in range(H):
    for j in range(W):
        if grid[i][j] == 'E':
            q.append((i, j))
            dist[i][j] = 0

while q:
    y, x = q.popleft()
    for dy, dx, arrow_char in dirs:
        ny, nx = y + dy, x + dx
        if 0 <= ny < H and 0 <= nx < W:
            if grid[ny][nx] == '.' and dist[ny][nx] == -1:
                dist[ny][nx] = dist[y][x] + 1
                arrow[ny][nx] = arrow_char
                q.append((ny, nx))

output = []
for i in range(H):
    row = []
    for j in range(W):
        if grid[i][j] == '.':
            row.append(arrow[i][j])
        else:
            row.append(grid[i][j])
    output.append(''.join(row))

print('\n'.join(output))
