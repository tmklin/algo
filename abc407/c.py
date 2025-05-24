def min_operations_to_match(S: str) -> int:
    S = S[::-1]
    n = len(S)
    b = 0
    steps = 0

    for i in range(n):
        digit = int(S[i])
        current = (0 + b) % 10
        diff = (digit - current + 10) % 10
        b += diff
        steps += 1 + diff

    return steps

S=input()
print(min_operations_to_match(S))
