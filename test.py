def gcd(a,b):
    if b ==0:
        return a
    else:
        return gcd(b,a%b)

d = []

for i in range (26):
    d.append(gcd(i,26))
print(d)
a = []
shift = 0
for i in range(10):
    result = (i+shift)%5
    #remain = (shift+i)//5
    a.append(result)

print(a)


