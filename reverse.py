def rev_vowel(st):
    temp=' '
    for i in st:
        if i in 'aeiouAEIOU':
            temp+=i 
    j=-1
    out=' '
    for k in st:
        if k in 'aeiouAEIOU':
           out+=temp[j]
           j+=-1
        else:
           out+=k
    return out
print(rev_vowel('hello'))
       