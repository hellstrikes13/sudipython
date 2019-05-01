import urllib
import random

def download(url):
  name = random.randrange(1,1000)
  imgname = str(name) + ".jpg"
  urllib.urlretrieve(url,imgname)
download('http://cbs.umn.edu/sites/cbs.umn.edu/files/public/african_lion_king-wide_1.jpg')

