# 初python！
# result: https://atcoder.jp/contests/abc124/submissions/7211139?lang=ja

s=input()

cnt_start0 = 0
cnt_start1 = 0
for i in range(len(s)):
    if i % 2 == 0:
        if s[i] == '0':
            cnt_start1 += 1
        if s[i] == '1':
            cnt_start0 += 1
    if i % 2 == 1:
        if s[i] == '0':
            cnt_start0 += 1
        if s[i] == '1':
            cnt_start1 += 1

print(min(cnt_start0, cnt_start1))
