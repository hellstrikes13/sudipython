from  selenium import webdriver
import sys
import argparse
import commands
import os
'''
PreRequisite for this script: 
 apt-get install phantomjs
 sudo pip install selinum
'''
print '''
this script will take entire screenshot of current webpage 
you can find the image under DIR: ~/screenshot
'''

w,h = commands.getoutput("xrandr | grep \* | awk '{print $1}'").split('x')
w = int(w)
h = int(h)
if len(sys.argv) < 2:
    print "ENTIRE URL missing..!!! e.g: http://google.com"
    sys.exit(0)
url = sys.argv[1]
driver = webdriver.PhantomJS()
url_name = url.split('.')[1]
driver.set_window_size(w, h)
driver.get(url)
d = dict(os.environ)
images = d['HOME']+'/screenshot/'
if os.path.isdir(images):
    pass
else:
   os.mkdir(images)
driver.save_screenshot(images+url_name+'.png')
