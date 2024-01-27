
import re 
data='''
vndkudfdfjdfhsyhdhsddsg,gsysteg01h734765ap 32 k 5667736euieap16k 989765'
'''
pattern='[Aa][Pp]?[0-3][1-9]?[A-Za-z]?[0-9]{4}'
data=re.findall(pattern,data)
print(data)