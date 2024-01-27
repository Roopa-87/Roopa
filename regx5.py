import re
data='''
sjkhdfuise7449583uresi
kjfsioer7w895rdhvj fdxo;coxdfu8rgjdkxf
orfixhfndvue*&$*idjfkmvl
'''
pattern='[a-u]{5}'
data=re.findall(pattern,data)
print(data)
