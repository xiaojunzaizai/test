import math

def gcd(a,b):
    if b ==0:
        return a
    else:
        return gcd(b,a%b)

# print(math.pow(3,13)%59)
print(35*3*48 % 59)
