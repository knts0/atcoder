s = input()
print("Heisei" if int(s[0:4] + s[5:7] + s[8:10]) <= 20190430 else "TBD")