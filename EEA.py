def EEA(r0,r1):
    s=[1,0]
    t = [0,1]
    r = [r0,r1]
    q = [0]
    i = 1
    while(r[i]!=0):
        i +=1
        r.append(r[i-2]%r[i-1])
        q.append((r[i-2]-r[i])/(r[i-1]))
        s.append(s[i-2]-(q[i-1] * s[i-1]))
        t.append(t[i-2] - (q[i-1]*t[i-1]))
    new_t = t.copy()
    flag = 1
    print('i     qi-1     ri     si      ti')
    del q[0]
    del r[:2]
    del s[:2]
    del t[:2]
    print('------------------------------------')
    for j,k,l,m in zip(q,r,s,t):
        flag +=1
        print(str(flag) + '     '+str(j)+'      '+ str(k)+'     '+ str(l)+'     '+str(m))
        print('------------------------------------')
    return new_t[i-1]
    
    
print(EEA(640,49))