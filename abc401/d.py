def solve(S, K):
    from itertools import combinations
    N = len(S)
    candidates = []
    for comb in combinations(range(N), K):
        valid = True
        for i in range(K - 1):
            if comb[i + 1] == comb[i] + 1:
                valid = False
                break
        if not valid:
            continue
        temp = list(S)
        for i in range(N):
            if temp[i] == '?':
                temp[i] = '.'
        for idx in comb:
            if S[idx] == '.':
                valid = False
                break
            temp[idx] = 'o'
        if not valid:
            continue
        if temp.count('o') != K or 'oo' in ''.join(temp):
            continue
        candidates.append(temp)
    result = []
    for i in range(N):
        chars = set(cand[i] for cand in candidates)
        if len(chars) == 1:
            result.append(chars.pop())
        else:
            result.append('?')
    print(''.join(result))
n, k = map(int, input().split())
s = input().strip()
solve(s, k)
