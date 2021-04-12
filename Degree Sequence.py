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

def new_I_degree_sequence(d,i,j):
    i = i-1
    j = j-1
    sum = 0
    for l in range(i,j+1):
        sum = sum + abs(d[i] - d[l])

    return sum

def DA(d,i,k,I):
    if i <2*k:
        return I[i-1]
    else:
        min = 10000000000000
        for t in range(k,i-k+1):
            sum = DA(d,t,k,I) + new_I_degree_sequence(d,t+1,i)
            if sum < min:
                min = sum
        if min <= I[i-1]:
            return min
        else:
            return I[i-1]
    

def result (nodes,k):
    I = []
    for i in range(1,len(nodes)+1):
        I.append(new_I_degree_sequence(nodes,1,i))
    da = []

    for i in range(1,len(nodes)+1):
        da.append(DA(nodes,i,k,I))  
    
    return I, da 



if __name__ == "__main__":

    nodes = [10,9 ,9, 8, 7, 7, 7, 7, 6, 6]

    k =3

    I,da = result(nodes,k)

    print('I(1,i): ', end = ' ')
    print(I)
    print('Da(1,i): ', end = ' ')
    print(da)

