s = input()
print(s[0].upper() + s[1:].lower() if len(s) > 1 else s[0].upper())