from sys import exit
def gold_room():
 print 'this room is full of gold... how much do u take ??'
 next = int(raw_input("> "))
# if "0" in next or "1" in next:
#  how_much  = int(next)
# else:
#  dead("man,learn to type a number")
 if next < 50:
  print "nice u r not greedy for gold .... u win"
  exit(0)
 else:
  dead('get lost u greedy man ...')

def bear_room():
 a = """
 there is bear here,
 the bear has a bunch of honey,
 the fat bear is in front of another door.
 how are u going to move the bear?
 """
 print a
 bear_moved = False
 while True:
  next = raw_input("> ")
  if next == "take honey":
   dead('the bear looks at u and then slaps ur face off')
  elif next == "taunt bear" and not bear_moved:
   print 'the bear has moved from the door and u can go thru it now !!!'
   bear_moved = True
  elif next == "taunt bear" and bear_moved:
   dead('the bear gets pissed off and taunts u back and then comes to attack u...and says growl growl..')
  elif next == "open door" and bear_moved:
   gold_room()
  else:
   print 'i dont understand what u just wrote.. please use human language'

def cthulhu_room():
 print "Here you see the great evil Cthulhu."
 print "He, it, whatever stares at you and you go insane."
 print "Do you flee for your life or eat your head?"
 next = raw_input("> ")
 if 'flee' in next:
  start()
 elif 'head' in next:
  dead('well that was tasty...')
 else:
  cthulhu_room()

def dead(why):
 print why, 'good job!'
 exit(0)
def start():
 print "You are in a dark room."
 print "There is a door to your right and left."
 print "Which one do you take?"

 next = raw_input("> ")
 if next == 'left':
  bear_room()
 elif next == 'right':
  cthulhu_room()
 else:
  dead ('u stumble around the room until u starve')

start()
