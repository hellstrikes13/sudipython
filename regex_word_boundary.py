import re
re_obj = re.compile(r'\bt.*?e\b')
a = re_obj.findall('time tame tune tone')
print a
