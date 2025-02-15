class FenwickTree:
    """Fenwick Tree（BIT）で空き位置の検索を高速化"""
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def add(self, i, x):
        """位置 i に x を加算（1-indexed）"""
        while i <= self.n:
            self.tree[i] += x
            i += i & -i

    def sum(self, i):
        """1 から i までの累積和を計算"""
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def find_kth(self, k):
        """k 番目の 0 の位置を求める（二分探索）"""
        l, r = 1, self.n
        while l < r:
            mid = (l + r) // 2
            if mid - self.sum(mid) >= k:
                r = mid
            else:
                l = mid + 1
        return l

n = int(input())
a = list(map(int, input().split()))

bit = FenwickTree(n)
res = [0] * (n + 1)  # 結果を格納する配列

for i in range(1, n+1):
    pos = bit.find_kth(a[i-1])  # a[i-1] 番目の 0 を探す
    res[pos] = i
    bit.add(pos, 1)  # その位置を埋める

print(" ".join(map(str, res[1:])))
