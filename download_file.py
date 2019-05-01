import urllib
def download(csv_url):
# retrieve the contents of url in response object
  res = urllib.urlopen(csv_url)

# copy the contents of response object in a variable
  csv = res.read()

# type cast  variable in to string type
  csv_str = str(csv)

#split the string ending in new line char
  lines = csv_str.split('\\n')

#create a raw file
  dest_file = r'fb.csv'

#open that file in write mode having f as file object
  f = open(dest_file,'w')

#loop thru string variable lines
  for line in lines:

#copy the lines into a file
    f.write(line + '\n')

#close the file connection obj
    f.close()

#make a function call with argument as url u wanna retrieve
download('http://real-chart.finance.yahoo.com/table.csv?s=FB&d=1&e=1&f=2016&g=d&a=4&b=18&c=2012&ignore=.csv')
