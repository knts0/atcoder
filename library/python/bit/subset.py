n = 10
a = (1 << 2) | (1 << 3) | (1 << 5) | (1 << 7)

bit = a
while True:
    s = []

    for i in range(n):
        if bit & (1 << i):
            s.append(i)

    print(str(bit) + ": {", end="")
    for i in range(len(s)):
        print(str(s[i]) + " ", end="")
    print("}")

    if not bit:
        break

    bit = (bit - 1) & a