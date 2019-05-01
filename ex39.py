state = {
'Maharashtra': 'mh',
'Kerla':'kr',
'Sikkim':'sk',
'Punjab':'pn'
}

st = state.get('Texas', None)
if st is None:
 print 'sorry no texas'

cities  = {
'mh' : 'mumbai',
'pn' : 'amritsar'
}

cities['go'] = 'goa'
print '-' * 10
print 'printing some states'
print 'Maharashtra abbr is ' ,state['Maharashtra']
print 'Kerla abbr is',state['Kerla']
print '-' * 10
print 'print cites of states'
print 'maharahtra has ', cities[state['Maharashtra']]
print 'Punjab has ', cities[state['Punjab']]
print '- ' * 10
for state, abbrev in state.items():
 print "%s is abbreviated %s" % (state, abbrev)

print '- ' * 10
for abbrev, city in cities.items():
 print "%s has the city %s" % (abbrev, city)

print '- ' * 10
# safely get an abbreviation by state that might not be there


# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city

