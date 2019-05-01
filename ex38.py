ten_things = "Apples Oranges Crows Telephone Light Sugar"
print "Wait theres not 10 things in that list lets fix it.."
stuff = ten_things.split(' ')
more_stuff = ["Day","Night","song","Frisbee","Corn","Banana","Girl","Boy" ]
while len(stuff) != 10:
 next_one = more_stuff.pop()
 print 'adding ' , next_one
 stuff.append(next_one)
 print 'there is %d items now' % len(stuff)
print 'there we go' , stuff
print 'lets do something with stuff',stuff
print stuff[1]
print stuff[-1]
print stuff.pop()
# ' '.join adds space in stuff list here space act as delimiter
print ' '.join(stuff)
# # acts as a delimiter between chars that are there in lists
print '#'.join(stuff[3:5])
