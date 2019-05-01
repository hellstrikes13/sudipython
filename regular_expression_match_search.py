import re
print bool(re.search(r'deep','sudeep'))
print bool(re.match(r'deep','sudeep'))
print '''
string:sudeep 
regex:deep

re.search will scan thru entire string hence its prints True

re.match will check only at the begining of string hence it print False
'''

