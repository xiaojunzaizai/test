import math

def gcd(a,b):
    if b ==0:
        return a
    else:
        return gcd(b,a%b)

# d = []

# for i in range (26):
#     d.append(gcd(i,26))
# print(d)
# a = []
# shift = 0
# for i in range(10):
#     result = (i+shift)%5
#     #remain = (shift+i)//5
#     a.append(result)

# print(a)
# a = int('%.f'%(math.pow(3,50)))
# print(a%13)


# a = []
# for i in range(9):
#     if gcd(i,9) == 1:
#         a.append(i)
# print(len(a))
# print(a)

# print((21*17)%30)

# a = math.pow(3,50)
# print(a)
# print(a%13)

print(gcd(45,216))


print(96%17)

a = math.pow(2,192)
b = math.pow(10,20)
c = 4.73364*b
print((a/c)*18)