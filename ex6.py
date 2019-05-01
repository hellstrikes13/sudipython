# a variable x that has another string fomatter embeeded into it
x = " there are %d types of ppl " %10

bin = 'binary'
do_not = "don't"
#variable y which has 2 string formatters
y = "Those who know %s and those who %s."  %(bin,do_not)
print x
print y
print "i said: %r." %x
print "i also said: '%s'." % y
# %r raw string used for debugging   and in var y we explcitely mentioned single quoute inside string formatter

hilarious = False
#this will print string joke_eval even if boolean value hilarious evalues to false coz we have %r that means print raw data no matter what conditions are applied
joke_eval = "Isn't that joke so funny?! %r"
#this shall print string value of joke_eval and boolean value false
print joke_eval % hilarious
'''
hila = False
jv = "Isn't that joke so funny?!"
print j % v
^^^ it wont print the line of jv since hila is false
'''
w = 'this is the left side of ...'
e = 'a string with a right side..'
print w  + e
