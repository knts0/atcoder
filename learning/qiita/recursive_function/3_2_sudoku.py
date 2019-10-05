import copy

# 数独ソルバー
field = [[-1] * 9 for _ in range(9)]
for i in range(9):
    line = input()
    for j in range(9):
        if line[j] == "*":
            continue
        
        field[i][j] = int(line[j])

res = []

def rec():
    # 空きマスを探す
    emptyi, emptyj = -1, -1
    for i in range(9):
        for j in range(9):
            if emptyi == -1 and emptyj == -1 and field[i][j] == -1:
                emptyi = i
                emptyj = j
                break
    
    # ベースケース（全て埋めて空きマスがない）
    if emptyi == -1 or emptyj == -1:
        res.append(copy.deepcopy(field))
        return

    # 空きマスに入れられる数字を求める
    canuse = [True] * 10
    for i in range(9):
        # 同じ列に同じ数字はだめ
        if field[emptyi][i] != -1:
            canuse[field[emptyi][i]] = False
        
        # 同じ行に同じ数字はだめ
        if field[i][emptyj] != -1:
            canuse[field[i][emptyj]] = False
        
        # 同じブロックに同じ数字はだめ
        bi = emptyi // 3 * 3 + 1
        bj = emptyj // 3 * 3 + 1
        for di in range(bi - 1, bi + 2):
            for dj in range(bj - 1, bj + 2):
                if field[di][dj] != -1:
                    canuse[field[di][dj]] = False
        
    # 再帰的に探索
    for v in range(1, 10):
        if not canuse[v]:
            continue
        field[emptyi][emptyj] = v
        rec()
    
    # 数値を置いていた空きマスを元の空きマスに戻す
    field[emptyi][emptyj] = -1

rec()
if len(res) == 0:
    print("no solutions.")
elif len(res) > 1:
    print("more than one solution.")
else:
    ans = res[0]
    for i in range(9):
        for j in range(9):
            print(str(ans[i][j]) + " ", end="")
        print("")
            