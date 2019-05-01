import re
regx = r'^(.{3}\.){3}.{3}'
s = '123.456.abc.def'
match = re.match(regx,s)
print 'match found: ',str(match).lower()
