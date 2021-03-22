import math


def ex_gcd(dividend, divisor):
    if 0 == divisor:
        # 易证明：当除数等于0时，可得 X = 1， Y = 0。假设最大公因数为被除数。
        # 注意：数学上，0和自然数没有最大公因数，此处是为了方便理解。
        return 1, 0, dividend
 
    # 得到 X2 和 Y2 的值，并且将求最大公因数的步骤混入其中了
    x2, y2, remainder = ex_gcd(divisor, dividend % divisor)
 
    # 得到 X1 和 Y1 的值
    temp = x2
    x1 = y2
    y1 = temp - int(math.floor(dividend / divisor)) * y2
 
    return x1, y1, remainder

# 求 （4/3）对1000000007取模：取模结果为333333337
mod = 29
x = 1
y = 28
inv, b, c = ex_gcd(y, mod)
# print(a,b,c)
ans = (x * inv) % mod
print(ans)