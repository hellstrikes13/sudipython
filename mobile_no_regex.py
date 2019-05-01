import re
tc = input()
for i in range(tc):
    reg = raw_input()
    if re.search(r"([789])([0-9]{9})",reg):
        print "YES"
    else:
        print "NO"
