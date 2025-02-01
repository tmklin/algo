a, b = map(int, input().split())
c = [input() for _ in range(a)]
d = [input() for _ in range(b)]
for i in range(a - b + 1):
    for j in range(a - b + 1):
        found = True
        for k in range(b):
            if c[i + k][j:j + b] != d[k]:
                found = False
                break
        if found:
            print(i+1, j+1)
            exit()
