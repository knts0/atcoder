def next_combination(sub):
    x = sub & -sub
    y = sub + x
    return (((sub & ~y) // x) >> 1) | y

n = 5
k = 3

bit = (1 << k) - 1
while bit < (1 << n):
    s = []
    for i in range(n):
        if bit & (1 << i):
            s.append(i)
    
    print(str(bit) + ": {", end="")
    for i in range(len(s)):
        print(str(s[i]) + " ", end="")
    print("}")

    bit = next_combination(bit)