# 蒙哥马利算法

#  a≡c (mod m) => a2≡c2 (mod m)  同余性质
# base变量表示第i-1位时计算出的模，通过递归能很容易地确定所有位的模。
# 如果第i位为1，即bi=1,则表示该位需要参与模运算，计算结果 result = (result*base) mod m;其中result为前i-1次的计算结果；若bi=0，则表示a的第i项为1，不必参与模运算

def mod(a,b,m):
    result = 1
    base = a
    while(b>0):
        x = bin(b)
        if (int(x[len(x)-1])&1 == 1):
            result = (result *base) % m
        
        base = (base * base) % m
        b = b >>1
    return result


print(mod(3,11,59))