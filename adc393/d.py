n = int(input())
s = input().strip()
index_list = [i for i, c in enumerate(s) if c == '1']
num_ones = len(index_list)
if num_ones == 0:
    print(0)
    exit()
median_index = index_list[num_ones // 2]
min_moves = sum(abs(index_list[i] - (median_index - num_ones // 2 + i)) for i in range(num_ones))
print(min_moves)
