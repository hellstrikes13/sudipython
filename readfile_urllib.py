import urllib
def getpage(url):
 '''
 retrieve the contents of a web page
 contents are converted to a string before returning it
 '''
 soc = urllib.urlopen(url)
 data  = str(soc.read())
 soc.close()
 return data
txt = getpage('http://www.directi.com/business-units.html')
print txt
