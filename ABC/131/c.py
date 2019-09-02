# result: https://atcoder.jp/contests/abc131/submissions/7312393

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

import math

a, b, c, d = list(map(int,input().split()))

mul_c = b // c - (a - 1) // c
mul_d = b // d - (a - 1) // d

gcd_c_d = gcd(c, d)
lcm_c_d = gcd_c_d * (c // gcd_c_d) * (d // gcd_c_d)
mul_c_d = b // lcm_c_d - (a - 1) // lcm_c_d

print(b - a + 1 - (mul_c + mul_d - mul_c_d))
