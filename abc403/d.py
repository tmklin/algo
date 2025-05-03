import sys
from collections import defaultdict
from itertools import product

sys.setrecursionlimit(1000000)

N, M = map(int, input().split())
C = list(map(int, input().split()))
animal_to_zoos = []
for _ in range(M):
    data = list(map(int, input().split()))
    A = [a - 1 for a in data[1:]]
    animal_to_zoos.append(A)
zoo_visits = defaultdict(int)

for zoos in animal_to_zoos:
    sorted_zoos = sorted(zoos, key=lambda x: C[x])
    if len(sorted_zoos) == 1:
        zoo_visits[sorted_zoos[0]] += 2
    else:
        zoo_visits[sorted_zoos[0]] += 1
        zoo_visits[sorted_zoos[1]] += 1

greedy_cost = sum(C[i] * zoo_visits[i] for i in zoo_visits)
best_cost = greedy_cost
zoo_count = [0] * N
def is_ok():
    for zoos in animal_to_zoos:
        count = sum(zoo_count[z] for z in zoos)
        if count < 2:
            return False
    return True
def dfs(i, current_cost):
    global best_cost

    if current_cost >= best_cost:
        return

    if i == N:
        if is_ok():
            best_cost = current_cost
        return

    for visit in (0, 1, 2):
        zoo_count[i] += visit
        dfs(i + 1, current_cost + visit * C[i])
        zoo_count[i] -= visit
dfs(0, 0)
print(best_cost)
