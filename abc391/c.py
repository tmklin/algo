from collections import defaultdict

n, q = map(int, input().split())
a = [input().split() for _ in range(q)]

# 各ボックスの要素を管理する辞書
b = defaultdict(set)
pos = {}  # 各要素の現在のボックス
last_move = {}  # x の最終的な移動先を記録

# 初期状態: 各要素は自分の番号のボックスに入っている
for i in range(1, n + 1):
    b[i].add(i)
    pos[i] = i

# クエリの処理
for i in a:
    if i[0] == "1":
        x, y = int(i[1]), int(i[2])
        last_move[x] = y  # x の最終的な移動先のみ記録
    else:
        # last_move に基づいてボックス更新
        for x, y in last_move.items():
            prev_box = pos[x]  # x の元の位置
            if prev_box in b:
                b[prev_box].discard(x)  # 古いボックスから削除
            b[y].add(x)  # 新しいボックスに追加
            pos[x] = y  # x の現在位置を更新
        
        last_move.clear()  # 移動適用済みなのでクリア

        # 2 のクエリを処理
        print(sum(len(v) >= 2 for v in b.values()))
