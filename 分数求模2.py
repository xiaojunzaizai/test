def power(x, y, mod):
    r = 1
    while( y ):
        if y & 1:
            r = (r * x) % mod
        x = (x * x) % mod
        y >>= 1
 
    return r
# (3/2) 对7 求模
x = 5
y = 1
# mod = 100000000 + 7
# 利用费马小定理求与（分母）逆元
mod = 24
inv = power(y, mod - 2, mod)
# 再求x分子乘以逆元取模
ans = x * inv % mod
print(ans )