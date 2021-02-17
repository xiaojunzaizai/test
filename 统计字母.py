#单线程 统计字母
S = 'Orubkiusvazkxyioktikgtjvxobgie'
S = S.lower()
d = {}
for i in S:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

items = d.items()
backS = [[v[1],v[0]] for v in items]
backS.sort(reverse= True)

for i in backS:
    print(i[1] + ':', end =' ')
    print(i[0], end= ', ')