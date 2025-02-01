n, w = map(int, input().split())
xy = [map(int, input().split()) for _ in range(n)]
x, y = [list(i) for i in zip(*xy)]
q = int(input())
ta = [map(int, input().split()) for _ in range(q)]
t, a = [list(i) for i in zip(*ta)]
print(x,y)
