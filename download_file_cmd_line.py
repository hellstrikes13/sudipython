import urllib
import sys
if len(sys.argv) >= 2:
 url = sys.argv[1]
 def download(urlpara):
  sp = url.split('/')
  name = sp[-1]
  print 'downloading file: %s ..'%name
  res = urllib.urlretrieve(url,name)
  print 'File Downloaded : %s in ur pwd' %name
 download(url)
else:
 print 'URL missing as argument to this script'
 
