N = int(input())
A = list(map(int, input().split()))

total_sum = sum(A)
squared_sum = sum(a * a for a in A)

result = (total_sum * total_sum - squared_sum) // 2
print(result)
