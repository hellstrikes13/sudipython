print 'u enter a dark room with 2 doors . do u go thru door #1 or door #2'
door = raw_input("> ")
if door == "1":
 print 'there is a gaint beer eating a cheese cake what do u do ?'
 print '1:take the cake'
 print '2.scream at the bear'
 bear = raw_input("> ")
 if bear == '1':
  print 'the bear gives u shabasi saying .. good job u r a brave person.. u thougt of taking food away . but i shall make u as my food now'
 elif bear == '2':
  print 'bear bhai says .. u scared me off dude.. lemme eat in patience'
 else:
  print 'well , doing %s is probaly better bear runs away' % bear

elif door == "2":
 print "You stare into the endless abyss at Cthulhu's retina."
 print "1: blueberries"
 print "2: blackberries"
 print "3: brownberries"
 insanity = raw_input("> ")
 if insanity == "1" or insanity == "2":
  print "Your body survives powered by a mind of jello. Good job!"
 else:
  print "The insanity rots your eyes into a pool of muck. Good job!"

else:
 print 'u stumble around and fall on a knief and die...god job..!'
 
