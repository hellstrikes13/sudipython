import calendar
dys = {
0:"Monday",
1:"Tuesday",
2:"Wednesday",
3:"Thursday",
4:"Friday",
5:"Saturday",
6:"Sunday"
}
s = '''
Hey der,
	You wanna know on which day of the week u were born irrepective of the year !!!
Following the below prompt and enter appropriate info.. cya 
Thanks sudi
'''
print s
name = raw_input('whats ur name buddy: ')

bd = map(int,raw_input("enter ur b'day in DD MM YYYY(date month year e.g 26 07 1989) space separated: ").split(' '))
month,day,year = bd[1],bd[0],bd[2]
dy = calendar.weekday(year,month,day)
print '\n'
for i in dys:
  if i == dy:
   print 'hey ',name,' were born on:',dys[i],'congrats..!!'
