S, A, B, X = map(int, input().split())
cycle = A + B
full_cycles = X // cycle
remainder = X % cycle
run_time = full_cycles * A + min(A, remainder)
distance = run_time * S
print(distance)
