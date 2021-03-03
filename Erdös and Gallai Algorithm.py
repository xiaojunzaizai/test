def algorithm(d):
    l = len(d)
    s1 = []
    s2 = []
    sum1 = 0
    for i in range(l):
        sum1 = sum1+ d[i]
        s1.append(sum1)
        sum2 = i*(i+1)
        for j in range(i+1,l):
            if i+1<=d[j]:
                sum2 = sum2+i+1
                print(i+1,end = ' + ')
            else:
                sum2 = sum2+d[j]
                print(d[j],end = ' + ')
        print()
        s2.append(sum2)
    result = True
    for k in range(len(s1)):
        if s1[k] > s2[k]:
            result = False
            break
    return s1,s2,result



nodes = [9,8,8,8,8,7,6,5,3,2]
s1,s2,result = algorithm(nodes)

print(s1)
print(s2)
print(result)
