def I_degree_sequence(d, i,j):
    i = i-1
    j = j-1
    m = 100000000000
    for k in range(i,j+1):
        sum = 0
        for l in range(i,j+1):
            sum = sum + abs(d[k] - d[l])
        if sum < m:
            m = sum
    return m


def DA(d,i,k,I):
    if i <2*k:
        return I[i-1]
    else:
        min = 10000000000000
        for t in range(k,i-k+1):
            sum = DA(d,t,k,I) + I_degree_sequence(d,t+1,i)
            if sum < min:
                min = sum
        if min <= I[i-1]:
            return min
        else:
            return I[i-1]
    

nodes = [7,6,6,5,5,4,2,2,1]

I = []
for i in range(1,len(nodes)+1):
    I.append(I_degree_sequence(nodes,1,i))
da = []
for i in range(1,len(nodes)+1):
    da.append(DA(nodes,i,3,I))    

print(I)
print(da)

