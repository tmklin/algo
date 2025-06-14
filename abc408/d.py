def min_operations(S):
    N = len(S)
    total_ones = S.count('1')
    if total_ones <= 1:
        return 0

    min_ops = float('inf')
    ones_prefix = [0] * (N + 1)

    for i in range(N):
        ones_prefix[i + 1] = ones_prefix[i] + (S[i] == '1')

    left = 0
    for right in range(N + 1):
        while right - left > total_ones:
            left += 1
        ones_in_block = ones_prefix[right] - ones_prefix[left]
        zeros_in_block = (right - left) - ones_in_block
        ops = zeros_in_block + (total_ones - ones_in_block)
        min_ops = min(min_ops, ops)

    return min_ops


T = int(input())
results = []
for _ in range(T):
    N = int(input())
    S = input().strip()
    results.append(str(min_operations(S)))

print('\n'.join(results))
