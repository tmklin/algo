A, B, C, D = map(int, input().split())
deadline = A * 60 + B
submit = C * 60 + D
if submit < deadline:
    print("Yes")
else:
    print("No")
