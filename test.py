import math

def gcd(a,b):
    if b ==0:
        return a
    else:
        return gcd(b,a%b)

print(math.pow(3,5)%5)

