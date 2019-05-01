import re
regx=r'((\w{3,4}?\W{1,3}\w{3}\W[\w]+\W\w{3}\.\w{3,4}?\W{1,3})?w{3}\W[\w]+\W\w{2,3}\W?)?[\S]+'
s='http://www.wikipedia.com.http://www.hackerrank.com'
#s='www.cisco.com'
#s='132.__________.co_'
print (str(bool(re.search(regx,s))))
