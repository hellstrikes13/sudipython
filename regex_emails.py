import re
n = 6
emails = []
for i in range(6):
     name_email = raw_input('name email: ')
     emails.append(name_email)
print emails
'''
mailregex= '[a-z0-9A-z]+\@gmail\.com$'
lst = []
for i in emails:
    if re.search(mailregex,emails[i]):
        lst.append(i)
    else:
        print 'unfortunately ',i,' doesnt have gmail ID',email[i],'so GET LOST !!!!'
for i in sorted(lst):
    print i
'''
