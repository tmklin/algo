n = int(input())
if n == 2:
    print("##\n##")
else:
    r = [["#"] * n for _ in range(n)]
    char = "."
    for k in range(1, (n + 1) // 2):
        for i in range(k, n - k):
            r[k][i] = char
            r[n - k - 1][i] = char
            r[i][k] = char
            r[i][n - k - 1] = char
        char = "#" if char == "." else "."
    for row in r:
        print("".join(row))
