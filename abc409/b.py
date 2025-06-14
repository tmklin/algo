N, Q = map(int, input().split())
X = list(map(int, input().split()))
box = [0] * N
result = []
for x in X:
    if x >= 1:
        box[x - 1] += 1
        result.append(x)
    else:
        min_count = min(box)
        for i in range(N):
            if box[i] == min_count:
                box[i] += 1
                result.append(i + 1)
                break

print(' '.join(map(str, result)))
