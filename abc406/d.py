from sys import stdin, stdout
from collections import defaultdict

def solve(H, W, N, trash_list, Q, queries):
    row_cnt = [0] * (H + 1)
    col_cnt = [0] * (W + 1)
    row_cells = defaultdict(set)
    col_cells = defaultdict(set)

    for x, y in trash_list:
        row_cnt[x] += 1
        col_cnt[y] += 1
        row_cells[x].add(y)
        col_cells[y].add(x)

    used_row = [False] * (H + 1)
    used_col = [False] * (W + 1)
    results = []

    for t, v in queries:
        if t == 1:
            if used_row[v]:
                results.append('0')
                continue
            results.append(str(row_cnt[v]))
            used_row[v] = True
            for y in row_cells[v]:
                if not used_col[y]:
                    col_cnt[y] -= 1
                    col_cells[y].discard(v)
            row_cells[v].clear()
        else:
            if used_col[v]:
                results.append('0')
                continue
            results.append(str(col_cnt[v]))
            used_col[v] = True
            for x in col_cells[v]:
                if not used_row[x]:
                    row_cnt[x] -= 1
                    row_cells[x].discard(v)
            col_cells[v].clear()

    return results

input = stdin.readline
H, W, N = map(int, input().split())
trash_list = [tuple(map(int, input().split())) for _ in range(N)]
Q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(Q)]
stdout.write('\n'.join(solve(H, W, N, trash_list, Q, queries)) + '\n')
