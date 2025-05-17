def count_tilde_sequences(P):
    N = len(P)

    up_len = [0] * N
    for i in range(1, N):
        if P[i - 1] < P[i]:
            up_len[i] = up_len[i - 1] + 1
    right_up_len = [0] * N
    for i in range(N - 2, -1, -1):
        if P[i] < P[i + 1]:
            right_up_len[i] = right_up_len[i + 1] + 1

    ans = 0
    i = 1
    while i < N - 1:
        if P[i - 1] < P[i] and P[i] > P[i + 1]:
            j = i + 1
            while j < N - 1 and P[j] > P[j + 1]:
                j += 1
            if j < N - 1 and P[j - 1] > P[j] and P[j] < P[j + 1]:
                left = up_len[i]
                right = right_up_len[j]
                if left > 0 and right > 0:
                    ans += left * right
            i = j
        else:
            i += 1

    return ans
N = int(input())
P = list(map(int, input().split()))
print(count_tilde_sequences(P))
