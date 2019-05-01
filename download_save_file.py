import calendar
import requests
'''
This program downloads files from mailing list of FAI 
The mailist list has downloadable file kept in proper order year and month wise
this simple script achives it with no worries
#author : sudi
'''
years = [x for x in range(2000,2018)]
months = [ m for m in calendar.month_name]
months.remove("")
url = "https://lists.uni-koeln.de/pipermail/linux-fai/"
location = "/home/sudeep/faidata/"
fnames = []
#loop for generating file names
for yr in years:
    for mn in months:
        fnames.append(str(yr)+'-'+mn+'.txt.gz')
#loop for downloading file
for fn in fnames:
    data = requests.get(url+fn)
    if data.status_code == 200:
        with open(location+fn,"w") as fo:
            fo.write(data.content)
        print fn," downloaded at /home/sudeep/faidata"
    else:
        print "File not found:",fn," ",data.status_code
