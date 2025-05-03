import string

S=input().strip()
for c in string.ascii_lowercase:
    if c not in S:
        print(c)
        break
