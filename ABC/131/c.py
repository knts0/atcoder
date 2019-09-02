def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

import math

a, b, c, d = list(map(int,input().split()))

mul_c = math.floor(float(b) / c) - math.ceil(float(a) / c) + 1
mul_d = math.floor(float(b) / d) - math.ceil(float(a) / d) + 1

gcd_c_d = gcd(c, d)
lcm_c_d = gcd_c_d * (c / gcd_c_d) * (d / gcd_c_d)
print(lcm_c_d)
mul_c_d = b / lcm_c_d - math.ceil(float(a) / lcm_c_d) + 1

print(b - a + 1 - (mul_c + mul_d - mul_c_d))
