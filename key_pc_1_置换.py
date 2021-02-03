def create_key(position_1):
    k = ['0']*64
    for i in position_1:
        k[i-1] = '1'
    return ''.join(k)

def substitution(key):
    pc_1 = [57,49,41,33,25,17,9,
            1,58,50,42,34,26,18,
            10,2,59,51,43,35,27,
            19,11,3,60,52,44,36,
            63,55,47,39,31,23,15,
            7,62,54,46,38,30,22,
            14,6,61,53,45,37,29,
            21,13,5,28,20,12,4]
    a = []
    for i in pc_1:
        a.append(key[i-1])
    b = ''.join(a)
    return b

l = [7,8,40]
k = create_key(l)
print(k)
k1 = substitution(k)
print(k1)






