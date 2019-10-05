def modpow(a, n, m):
    if n == 0: return 1
    half = modpow(a, n // 2, m)
    res = half * half % m
    if n & 1: res = res * a % m
    
    return res