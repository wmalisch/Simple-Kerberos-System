
val = 1024
token = 5689898
x = 8

valn = val.to_bytes(16, byteorder='big')
print(valn)
xn = x.to_bytes(16, byteorder='big')
print(xn)

tokn = token.to_bytes(14, byteorder='big')
print(tokn)
print(int.from_bytes(valn,byteorder='big'))
print(int.from_bytes(xn,byteorder='big'))
print(int.from_bytes(tokn,byteorder='big'))
