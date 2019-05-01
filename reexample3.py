import re
s='122 23 56'
regx=r'^\S?(\S{2}\s){2}\S{2}$'
print str(bool(re.search(regx,s)))
'''
\S denotes non whitespace char  AB
\s denotes whitespace char such A \r\nB
'''
