import re
regx = r'^(\d\d\D){2}\d'
s='10a10.2015452254'
print (str(bool(re.search(regx,s))))
