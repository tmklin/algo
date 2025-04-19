def count_errors(n, operations):
    logged_in = False
    errors = 0
    for op in operations:
        if op == "login":
            logged_in = True
        elif op == "logout":
            logged_in = False
        elif op == "private":
            if not logged_in:
                errors += 1
        elif op == "public":
            pass
    return errors
n=int(input())
s=[str(input()) for _ in range(n)]
print(count_errors(n,s))