
char_to_ind = {chr(ord('a')+i):i for i in range(26)} 
ind_to_char = {v:k for k,v in char_to_ind.items()}

def encrypt(text, ind):
    encrypt = []
    for i in text:
        encrypted = ind_to_char[(char_to_ind[i]+(ind))%26]
        encrypt.append(encrypted)
    return ''.join(encrypt)

def calculate_key(max_freq_letter, target_letter):
    key = char_to_ind[target_letter] -char_to_ind[max_freq_letter]
    if key < 0:
        key += 26
    return key



def count_w(S):
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
    temp = backS[0][0]
    d = []
    for i in backS:
        if i[0] > temp:
            temp = i[0]
        if i[0] == temp:
            d.append(i[1])
            temp = i[0]
            
            
    return d


S = 'Orubkiusvazkxyioktikgtjvxobgie'
S = S.lower()
target = 'e'
high_frequent_w = count_w(S)
m = []
for i in high_frequent_w:
    key = calculate_key(i,target)
    message = encrypt(S,key)
    m.append([message,key,i])
print(m)

d = []
for i in S:
   d.append(char_to_ind[i])
print(d)

e = []
for i in m[0][0]:
    e.append(char_to_ind[i])
print(e)