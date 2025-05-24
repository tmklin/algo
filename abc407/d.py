def max_xor_score_bruteforce(H, W, A):
    pairs = []
    for i in range(H):
        for j in range(W):
            if j + 1 < W:
                pairs.append(((i, j), (i, j + 1), A[i][j] ^ A[i][j + 1]))
            if i + 1 < H:
                pairs.append(((i, j), (i + 1, j), A[i][j] ^ A[i + 1][j]))

    total_xor = 0
    for i in range(H):
        for j in range(W):
            total_xor ^= A[i][j]

    max_result = total_xor

    def dfs(index, used, basis, current_xor):
        nonlocal max_result
        if index == len(pairs):
            max_result = max(max_result, current_xor)
            return

        (i1, j1), (i2, j2), val = pairs[index]

        dfs(index + 1, used, basis, current_xor)

        if used[i1][j1] or used[i2][j2]:
            return

        x = val
        for b in basis:
            x = min(x, x ^ b)
        if x:
            new_basis = basis + [x]
            used_copy = [row[:] for row in used]
            used_copy[i1][j1] = used_copy[i2][j2] = True
            new_xor = current_xor
            for b in new_basis:
                new_xor = max(new_xor, new_xor ^ b)
            dfs(index + 1, used_copy, new_basis, new_xor)

    used_init = [[False] * W for _ in range(H)]
    dfs(0, used_init, [], total_xor)
    return max_result

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
print(max_xor_score_bruteforce(H, W, A))
