import re
n = 6
emails = {}
for i in range(6):
     name,email = raw_input('name email: ').split(' ')
     emails[name] = email
print emails
mailregex= '[a-z0-9A-z]+\@gmail\.com$'
lst = []
for i in emails:
    if re.search(mailregex,emails[i]):
        lst.append(i)
    else:
        print 'unfortunately ',i,' doesnt have gmail ID',email[i],'so GET LOST !!!!'
for i in sorted(lst):
    print i

