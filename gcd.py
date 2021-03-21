def gcd(a,b):
    if b ==0:
        return a
    else:
        print(str(a)+' = '+str(a//b)+' * '+ str(b) + ' + ' + str(a%b))
        return gcd(b,a%b)


print(gcd(27,21))